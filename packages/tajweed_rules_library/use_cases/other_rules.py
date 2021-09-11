
from use_cases.rule import Rule
from controllers.input_factory import InputFactory
from presenters.output_factory import OutputFactory

class OtherRules(Rule):

  def __init__(self, input_factory, output_factory):
    self
    self.input = input_factory
    self.output = output_factory
    self.rules = ["ghunnah", "idghaam_ghunnah", "idghaam_no_ghunnah", "idghaam_mutajanisayn",
    "idghaam_mutaqaribayn", "idghaam_shafawi", "ikhfa", "ikhfa_shafawi", "idhaar",
    "idhaar_shafawi", "iqlab", "madd_246", "madd_muttasil", "madd_munfasil", "madd_6", "qalqalah"]

  def generate_rule_files(self):
    for rule in self.rules:
      content_for_rule = self.extract_rule_data(rule)
      output_file = self.output.create_absolute_output_path(rule)
      self.output.write_to_output_file(content_for_rule, output_file)

      
  def extract_rule_data(self, rule):
    rules_locations = {}
    rules_locations[rule] = []
    all_rules = {}

    input_file_content = self.input.save_file_content()
    all_rules = input_file_content

    for ayah in all_rules['data']:
      for rule_in_ayah in ayah['annotations']:
        if rule_in_ayah['rule'] == rule:
          ayah_rule_info = self.construct_rule_location_map(ayah['surah'], ayah['ayah'], rule_in_ayah['start'], rule_in_ayah['end'])
          rules_locations[rule].append(ayah_rule_info)
          
    return rules_locations

other_rules = OtherRules(InputFactory('others_file'), OutputFactory('file'))
