from src.entities.entities_map import EntitiesMap

class CreateRulesMaps():
  def __init__(self, factory):
    self
    self.factory = factory
    self.input_to_map_gateway = self.factory.get_input_to_map_gateway()
    self.input_system = self.factory.get_input_system()

  def create_rule_maps(self):
    rule_names = self._get_rule_names()

    for rule_name in rule_names:
      class_name = self._get_class_from_rule_name(rule_name)
      self._create_single_rule_map(rule_name, class_name)
  
  def _get_rule_names(self):
    rule_names = self.input_to_map_gateway.get_rule_names()
    return rule_names

  def _get_class_from_rule_name(self, rule_name):
    class_name = self.input_to_map_gateway.get_rule_class_from_name(rule_name) 
    return class_name

  def _create_single_rule_map(self, rule_name, class_name):
    entities_map = EntitiesMap()
    all_rules_locations = []

    quran = self.input_system.read_file_by_lines()

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
    output_file = self.input_system.create_absolute_output_path(rule_name)
    self.input_system.write_to_file(content_for_rule, output_file)

   
    