from src.entities.entities_map import EntitiesMap

class CreateRulesMaps():
  def __init__(self, factory, files_and_dirs):
    self
    self.factory = factory
    self.files_and_dirs = files_and_dirs

  # Methods from factory
  def _file_to_rule_maps(self):
    return self.factory.get_file_to_map_gateway()

  def _file_system(self):  
    return self.factory.get_file_system()

  def create_rule_maps(self, rule_maps_to_create):
    for rule in rule_maps_to_create:
      if self.factory.env == 'local':
        class_name = self._get_class_from_rule_name(rule)
        self._create_single_rule_map(rule, class_name)
      elif self.factory.env == 'prod':
        print(rule['name'])
        target_path = self._file_system().create_absolute_path(self.files_and_dirs, rule['name'])
        self._copy_file_to_prod_output(rule['absolute_path'], target_path)
  
  def _get_class_from_rule_name(self, rule_name):
    class_name = self._file_to_rule_maps().get_rule_class_from_name(rule_name) 
    return class_name

  def _copy_file_to_prod_output(self, original, target):
    return self._file_system().copy_file_from_original_to_target_dir(original, target)

  def _create_single_rule_map(self, rule_name, class_name):
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
    content_for_rule = {}
    content_for_rule[rule_name] = rule_locations
    output_file = self._file_system().create_absolute_path(self.files_and_dirs, rule_name)
    self._file_system().write_to_file(content_for_rule, output_file)
   
    