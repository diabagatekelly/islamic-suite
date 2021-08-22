MASTER_RULES_INPUT = '../../entities/input_master_fixture/tajweed.hafs.uthmani-pause-sajdah.json'
import json, os

class SingleRuleFiles():

  def __init__(self, input_file, root_dir, relative_dir):
    self
    self.input_file = input_file
    self.root_dir = root_dir
    self.relative_dir = relative_dir
    self.all_rules = {}
    self.rules = ["ghunnah", "idghaam_ghunnah", "idghaam_no_ghunnah", "idghaam_mutajanisayn",
    "idghaam_mutaqaribayn", "idghaam_shafawi", "ikhfa", "ikhfa_shafawi", "idhaar",
    "idhaar_shafawi", "iqlab", "madd_246", "madd_muttasil", "madd_munfasil", "madd_6", "qalqalah"]
    self.save_file_content()
  
  def save_file_content(self):
    with open(self.input_file) as input_file:
      file_content = json.load(input_file)
      self.all_rules["data"] = file_content
      input_file.close()

  def generate_rule_files(self):
    for rule in self.rules:
      content_for_rule = self.extract_rule_data(rule)
      output_file = self.create_absolute_output_path(rule)
      self.write_to_output_file(content_for_rule, output_file)

      
  def extract_rule_data(self, rule):
    rules_locations = {}
    rules_locations[rule] = []

    for ayah in self.all_rules['data']:
      for rule_in_ayah in ayah['annotations']:
        if rule_in_ayah['rule'] == rule:
          ayah_rule_info = self.parse_rule_location_details(ayah['surah'], ayah['ayah'], rule_in_ayah['start'], rule_in_ayah['end'])
          rules_locations[rule].append(ayah_rule_info)
          
    return rules_locations
  
  
  def parse_rule_location_details(self, surah, ayah, start_index, end_index):
    ayah_rule_info = {}
    ayah_rule_info["surah"] = surah
    ayah_rule_info["ayah"] = ayah
    ayah_rule_info["start"] = start_index
    ayah_rule_info["end"] = end_index

    return ayah_rule_info
    

  def create_absolute_output_path(self, rule):
    relative_path = os.path.join(self.relative_dir, f'{rule}.json')
    absolute_path = os.path.join(self.root_dir, relative_path)
    return absolute_path

  def write_to_output_file(self, content, path):
    with open(path, "w") as outfile:
      json.dump(content, outfile)
      outfile.close()

