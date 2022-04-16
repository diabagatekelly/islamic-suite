from src.entities_helpers.entities_map import EntitiesMap

class CreateRulesMaps():
  """Create Rules Maps
  
  The entities folder contains entity modules, each defining the following for a single tajweed rule:
    1. how to find that rule in the quran
    2. save all the locations of that rule as a map
  
  Given a list of rules that need new maps created, this module uses each rule name to:
    - fetch its entity module and use it to parse the Qur'an for that rule
    - create a map of all locations in the Qur'an for that rule
    - save that map to the appropriate directory (DEV --> 'outputs', PROD --> 'dist')
  
  Constructor:
    *files_and_dir: object containing relevant directories
    *factory: dev or prod factory

  Factory methods: 
    *_file_to_rule_maps (private) - gets file_to_map gateway from factory
    *_file_system (private) - gets file_system from factory

  Module methods:
    *_get_class_from_rule_name - uses factory method to get a rule's ClassName from its name
    *_copy_file_to_prod_output - in PROD, copy json map from 'outputs' to 'dist'
    *_create_single_rule_map - uses entity module for a rule to parse the Qur'an and create its map
    *_parse_quran_script - for each Qur'an line, get its surah number, ayah number, and ayah text
    *_save_rules_map - create absolute path for created map and write map content to file

    *create_rule_maps (public) - given a list of rule names, create new maps and save them in 'outputs' in DEV, or copy existing maps from local outputs
    to 'dist' in PROD
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
  def create_rule_maps(self, rule_maps_to_create):
    """Given a list of rule names, create new maps and save them in 'outputs' in DEV, or copy existing maps from local outputs
      to 'dist' in PROD
      - parameters: list of string (DEV) or objects {name: 'name', absolute_path: 'path.json'}
    """
    for rule in rule_maps_to_create:
      if self.factory.env == 'local':
        self._create_single_rule_map(rule)
      elif self.factory.env == 'prod':
        print(rule['name'])
        target_path = self._file_system().create_absolute_path(self.files_and_dirs, rule['name'])
        self._copy_file_to_prod_output(rule['absolute_path'], target_path)
  
  def _get_class_from_rule_name(self, rule_name):
    """Uses factory method to get a rule's ClassName from its name
      - parameters: rule_name (idghaam_shafawi)
      - returns: class name for rule (IdghaamShafawi)
    """
    class_name = self._file_to_rule_maps().get_rule_class_from_name(rule_name) 
    return class_name

  def _copy_file_to_prod_output(self, original, target):
    """In PROD, copy json map from 'outputs' to 'dist'
    """
    return self._file_system().copy_file_from_original_to_target_dir(original, target)

  def _create_single_rule_map(self, rule_name):
    """Given a rule name, creates a new instance of its entity class and use it to parse the Qur'an 
      and create a JSON map of all the locations for that rule in the Qur'an
      - parameters: rule_name as string ('idghaam')
    """
    class_name = self._get_class_from_rule_name(rule_name)
    entities_map = EntitiesMap()
    all_rules_locations = []

    quran = self._file_system().read_file_by_lines(self.files_and_dirs['input_file'])

    for line in quran:
      parsed_line = self._parse_quran_script(line)
      surah_number = parsed_line['surah_number']
      ayah_number = parsed_line['ayah_number']
      ayah_text = parsed_line['ayah_text']

      rule_map = entities_map.fetch_entity(class_name)(surah_number, ayah_number, ayah_text)
      
      rule_locations = rule_map.get_all_rule_locations()
      all_rules_locations = all_rules_locations + rule_locations

      self._save_rules_map(rule_name, all_rules_locations)
    
  def _parse_quran_script(self, line):
    """For each Qur'an line, get its surah number, ayah number, and ayah text
      - parameters: quran line as string
      - returns: object { 'surah_number': surah_number, 'ayah_number': ayah_number, 'ayah_text': ayah_text }
    """
    segments = line.split('|')
    surah_number = int(segments[0])
    ayah_number = int(segments[1])
    ayah_text = segments[2].strip()

    parsed_line = {
      'surah_number': surah_number,
      'ayah_number': ayah_number,
      'ayah_text': ayah_text
    }

    return parsed_line

  def _save_rules_map(self, rule_name, rule_locations):
    """Create absolute path for created map and write map content (rule_locations) to file
      - parameters: rule_name, rule_locations list of objects [{"surah": 2, "ayah": 10, "start": 13, "end": 17}]
    """
    content_for_rule = {}
    content_for_rule[rule_name] = rule_locations
    output_file = self._file_system().create_absolute_path(self.files_and_dirs, rule_name)
    self._file_system().write_to_file(content_for_rule, output_file)