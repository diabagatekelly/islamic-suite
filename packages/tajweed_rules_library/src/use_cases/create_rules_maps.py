from src.tajweed_rules_helpers.tajweed_rules_map import TAJWEED_RULES

class CreateRulesMaps():
  """Create Rules Maps

  The entities folder contains entity modules, each defining the following for a single tajweed rule or a type of rule:
    1. how to find that rule in the quran
    2. save all the locations of that rule as a JSON map

  Given a list of tajweed rule types or rules that need new maps created, this module uses each rule name to:
    - fetch its entity module and use it to parse the Qur'an for that rule
    - create a map of all locations in the Qur'an for that rule
    - save that map to the appropriate directory (DEV --> 'outputs', PROD --> 'dist')

  Constructor:
    *files_and_dir: object containing relevant directories
    *factory: dev or prod factory

  Factory methods: 
    *_file_system (private) - gets file_system from factory

  Module methods:
    *_reset_output_folder - Clears out the outpur folder (output (DEV) or dist(PROD))
    *_create_single_rule_map - uses entity module for a rule to parse the Qur'an and create its map
    *_get_details_from_quran_line - for each Qur'an line, get its surah number, ayah number, and ayah text
    *_save_rules_map - create absolute path for created map and write map content to file
    *_copy_file_to_prod_output - in PROD, copy json map from 'outputs' to 'dist'

    *create_rule_maps (public) - given a list of rule names, create new maps and save them in 'outputs' in DEV, or copy existing maps from local outputs
    to 'dist' in PROD
  """

  def __init__(self, factory, files_and_dirs):
    self
    self.factory = factory
    self.files_and_dirs = files_and_dirs

  # Methods from factory
  def _file_system(self):
    """Returns file_system gateway from pre-initialized dev or prod factory"""
    return self.factory.get_file_system()

  # Module methods
  def create_rule_maps(self, list_of_rules_that_need_new_maps):
    """Given a list of rule names, create new maps and save them in 'outputs' in DEV, or copy existing maps from local outputs
      to 'dist' in PROD
      - parameters: list of string (DEV) or objects {name: 'name', absolute_path: 'path.json'}
    """
    if self.factory.env == 'prod':
      self._reset_output_folder(self.files_and_dirs['outputs_dir'])
    
    for rule in list_of_rules_that_need_new_maps:
      if self.factory.env == 'local':
        self._create_single_rule_map(rule)
      elif self.factory.env == 'prod':
        target_path = self._file_system().create_absolute_path(self.files_and_dirs, rule['name'])
        self._copy_file_to_prod_output(rule['absolute_path'], target_path)

  def _reset_output_folder(self, target):
    """Clears out the outpur folder (output (DEV) or dist(PROD))
    """
    self._file_system().empty_directory(target)

  def _create_single_rule_map(self, rule_name):
    """Given a rule name, use its module to parse the Qur'an 
      and create a JSON map of all the locations for that rule in the Qur'an
      - parameters: rule_name as string ('idghaam')
    """
    
    # We create a new instance of the rule
    # by calling the class retrieved from the
    # TAJWEED_RULES enum
    rule_type = TAJWEED_RULES[rule_name]()

    quran = self._file_system().read_file_by_lines(self.files_and_dirs['input_file'])
    
    all_rules_for_this_rule_type = rule_type.rules
        
    for rule in all_rules_for_this_rule_type:
      all_rules_locations = []
      print(f'Mapping rule {rule}.....')

      for line in quran:
        verse_details = self._get_details_from_quran_line(line)
        surah_number = verse_details['surah_number']
        ayah_number = verse_details['ayah_number']
        ayah_text = verse_details['ayah_text']
        
        rule_type.surah_number = surah_number
        rule_type.ayah_number = ayah_number
        rule_type.ayah_text = ayah_text
        
        rule_locations = rule_type.get_all_rule_locations(rule)
        all_rules_locations = all_rules_locations + rule_locations

      print(f'Finished mapping rule {rule}.')
      self._save_rules_map(rule, all_rules_locations)
      
  def _get_details_from_quran_line(self, line):
    """For each Qur'an line, get its surah number, ayah number, and ayah text
      - parameters: quran line as string
      - returns: object { 'surah_number': surah_number, 'ayah_number': ayah_number, 'ayah_text': ayah_text }
    """
    segments = line.split('|')
    surah_number = int(segments[0])
    ayah_number = int(segments[1])
    ayah_text = segments[2].strip()

    verse_details = {
      'surah_number': surah_number,
      'ayah_number': ayah_number,
      'ayah_text': ayah_text
    }

    return verse_details
  
  def _save_rules_map(self, rule_name, rule_locations):
    """Create absolute path for created map and write map content (rule_locations) to file
      - parameters: rule_name, rule_locations list of objects [{"surah": 2, "ayah": 10, "start": 13, "end": 17}]
    """
    content_for_rule = {}
    content_for_rule[rule_name] = rule_locations
    output_file = self._file_system().create_absolute_path(self.files_and_dirs, rule_name)
    self._file_system().write_json_to_file(content_for_rule, output_file)
      
  def _copy_file_to_prod_output(self, original, target):
    """In PROD, copy json map from 'outputs' to 'dist'
    """
    return self._file_system().copy_file_from_original_to_target_dir(original, target)