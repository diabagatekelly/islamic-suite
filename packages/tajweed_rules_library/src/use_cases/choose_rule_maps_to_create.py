class ChooseRuleMapsToCreate():
  """Choose Rule Maps To Create
  
  The entities folder contains entity modules, each defining the following for a single tajweed rule:
    1. how to find that rule in the quran
    2. save all the locations of that rule as a map
  
  This module chooses which tajweed rules need their map created.
  DEV: depends on whether there have been updates to that rule's entity file, 
  or if it doesn't already have a map in the 'outputs' directory.
  PROD: depends on whether there have been updates to that rule's DEV map 
  in the outputs directory, or if it doesn't already have a map in the 'dist' directory
  
  Constructor:
    *files_and_dir: object containing relevant directories
    *factory: dev or prod factory

  Factory methods: 
    *_file_to_rule_maps (private) - gets file_to_map gateway from factory
    *_file_system (private) - gets file_system from factory

  Module methods:
    *_get_rule_name_from_file - uses factory method to extract a rule's name from an entity's file name.extension
    *_transform_rules_file_info - transform file info by changing the rule's name from a filename (rule.ext) to just the name
    *_get_all_existing_rules_file_info - get list of files in dev 'outputs' or prod 'dist' directory
    *_get_all_rule_definitions_file_info - get list of all files in dev 'entities_dir' or prod 'outputs' directory
    *_get_existing_rules_file_last_update - get last update date for a pre-existing rule in dev 'outputs' or in prod 'dist'
    *_get_rule_definition_file_last_update - get last update for a entity in dev 'entities_dir' or prod 'outputs'
    *_rule_definition_has_recent_updates - returns true or false depending on whether a rule file in dev 'entities_dir' or prod 'outputs'
    has more recent updates than when its map was last created
    *_get_existing_rules_with_no_updates - return list of pre-existing maps in dev 'outputs' or prod 'dist' for which there have been
    no recent updates for the equivalent rule definitions in dev 'entities_dir' or prod 'outputs'
    *_get_all_rule_names - returns list of rule names in dev 'entities_dir' or prod 'outputs'
    *_remove_non_rule_definitions_files_and_duplicates - clean up all_rule_names list by removing init.py and duplicates

    *get_list_of_rule_maps_to_create (public) - get list of rules that need new maps depending on whether its entity (in dev) 
    or its pre-existing map in 'outputs' (prod) has had recent changes
  """
  def __init__(self, factory, files_and_dirs):
    self
    self.factory = factory
    self.files_and_dirs = files_and_dirs
  
  # Methods from factory
  def _file_to_rule_maps(self):
    """Returns file_to_map gateway from pre-initialized dev or prod factory"""
    return self.factory.get_file_to_map_gateway()

  def _file_system(self):  
    """Returns file_system gateway from pre-initialized dev or prod factory"""
    return self.factory.get_file_system()

  # Module methods
  def get_list_of_rule_maps_to_create(self):
    """In DEV, gets list of all rules in 'entities_dir' and generate list of rules with pre-existing maps
      whose rules have no recent updates, then compares both lists and returns the rules that are in the first list
      but not the second (in other words, the rules that have no pre-existing map, or have a pre-existing map whose rules
      have recent updates).
      In PROD, gets list of rules with pre-existing maps in 'outputs' and generate list of rules with pre-existing prod maps
      found in 'dist'. It then compares both lists and returns the rules that are in the first list
      but not the second (in other words, the rules that have no pre-existing prod map, or have a pre-existing map whose equivalent
      local output has been updated).
			- returns: array of rule names (dev) or array of rule objects {name: 'name', absolute_path: 'path.json'}
    """
    if self.factory.env == 'local':
      existing_rules_with_no_updates = self._get_existing_rules_with_no_updates()
      all_rules = self._get_all_rule_names()
      return [rule for rule in all_rules if rule not in existing_rules_with_no_updates]
    elif self.factory.env == 'prod':
      existing_prod_rules_with_no_updates = self._get_existing_rules_with_no_updates()
      all_files = self._get_all_rule_definitions_file_info()
      all_local_rules_outputs = self._transform_rules_file_info(all_files)
      return [rule for rule in all_local_rules_outputs if rule['name'] not in existing_prod_rules_with_no_updates]

  def _get_all_rule_names(self):
    """Gets rule data for all the rules in dev 'entities_dir' or prod 'outputs'.
      Then, extracts each rule's name from its data.
      - returns: list of rule names ['idghaam', 'ghunnah']
    """
    all_files = self._get_all_rule_definitions_file_info()
    all_rule_names = [rule['name'] for rule in self._transform_rules_file_info(all_files)]
    return self._remove_non_rule_definitions_files_and_duplicates(all_rule_names)

  def _remove_non_rule_definitions_files_and_duplicates(self, name_list):
    """Cleans up list of rule names by removing init.py and duplicates
      - parameters: name_list --> ['__init__', 'ighaam', 'ghunnah', 'idghaam']
      - returns: list of rule names ['idghaam', 'ghunnah']
    """
    filtered_list = [name for name in name_list if name not in ('__init__')]
    final_list = list(set(filtered_list))
    return final_list
  
  def _get_existing_rules_with_no_updates(self):
    """Gets list of pre-existing maps in dev 'outputs' or prod 'dist' and check if their equivalent 
      rule definitions in dev 'entities_dir' or prod 'outputs' has had recent updates. Compiles list of 
      rules with no recent updates.
      - returns: list of rule names ['idghaam', 'ghunnah']
    """
    existing_rules_with_no_updates = []
    files = self._get_all_existing_rules_file_info()
    all_existing_rules = [file["name"] for file in self._transform_rules_file_info(files)]
    for rule in all_existing_rules:
      if self._rule_definition_has_recent_updates(rule) == False:
        existing_rules_with_no_updates.append(rule)
    return existing_rules_with_no_updates
  
  def _rule_definition_has_recent_updates(self, rule_name):
    """Given a rule name, checks the last update date for that rule in DEV 'entities_dir' vs 'outputs' 
    or PROD 'outputs' vs 'dist'. Returns true if the source (definition) 's update date >= generated map (existing) update date
      - parameters: rule_name as string
      - returns: boolean
    """
    last_rule_definition_file_update = self._get_rule_definition_file_last_update(rule_name)
    last_existing_rule_file_update = self._get_existing_rules_file_last_update(rule_name)
    return last_rule_definition_file_update >= last_existing_rule_file_update

  def _get_rule_definition_file_last_update(self, rule_name):
    """For a given rule name, get its last update date in dev 'entities_dir' or prod 'outputs'
      - parameters: rule_name as string
      - returns: date as float
    """
    all_files = self._get_all_rule_definitions_file_info()
    rule_definition_file_path = [file["absolute_path"] for file in self._transform_rules_file_info(all_files) if file["name"] == rule_name]
    return self._file_system().get_file_last_update_date(rule_definition_file_path[0])

  def _get_existing_rules_file_last_update(self, rule_name):
    """For a given rule name, get its last update date in dev 'outputs' or prod 'dist'
      - parameters: rule_name as string
      - returns: date as float
    """
    files = self._get_all_existing_rules_file_info()
    existing_rule_file_path = [file["absolute_path"] for file in self._transform_rules_file_info(files) if file["name"] == rule_name]
    return self._file_system().get_file_last_update_date(existing_rule_file_path[0])

  def _get_all_rule_definitions_file_info(self):
    """In DEV, get rule data for all the files in 'entities_dir';
    In PROD, get rule data for all the files in 'outputs'
      - returns: array of objects [{name: 'name.ext', absolute_path: 'path.json'}]
    """
    if self.factory.env == 'local':
      return self._file_system().get_files_in_directory(self.files_and_dirs['entities_dir'])
    elif self.factory.env == 'prod':
      return self._file_system().get_files_in_directory(self.files_and_dirs['local_outputs'])

  def _get_all_existing_rules_file_info(self):
    """In DEV, get rule data for all the files in 'outputs';
    In PROD, get rule data for all the files in 'dist'
      - returns: array of objects [{name: 'name.ext', absolute_path: 'path.json'}]
    """
    if self.factory.env == 'local':
      return self._file_system().get_files_in_directory(self.files_and_dirs['outputs_dir'])
    elif self.factory.env == 'prod':
      return self._file_system().get_files_in_directory(self.files_and_dirs['outputs_dir'])

  def _transform_rules_file_info(self, rule_data_list):
    """Transforms rule data by changing the rule's name from a filename (rule.ext) to just the name
      - parameters: rule_data_list [{name: 'name.ext', absolute_path: 'path.json'}]
      - returns: [{name: 'name', absolute_path: 'path.json'}]
    """
    for rule_data in rule_data_list:
      rule_data['name'] = self._get_rule_name_from_file(rule_data['name'])
    return rule_data_list
  
  def _get_rule_name_from_file(self, file_name):
    """Uses factory method to extract a rule's name from an entity's file name.extension
      - parameters: file_name as string (name.ext)
      - returns: rule name as string (name)
    """
    return self._file_to_rule_maps().get_name_from_file(file_name)