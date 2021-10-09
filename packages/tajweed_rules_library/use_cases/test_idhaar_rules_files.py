import unittest, os, json, shutil
from use_cases.idhaar_rule import IdhaarRule
from controllers.input_factory import InputFactory
from presenters.output_factory import OutputFactory

ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
RELATIVE_DIR = 'use_cases\\idhaar_specs'
IDHAAR_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\mock_fixtures\\idhaar_mock_input.txt'


class TestIdhaarRuleFiles(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    file_input_factory = InputFactory().get_input()
    file_output_factory = OutputFactory().get_output()

    idhaar_file_input = file_input_factory(IDHAAR_INPUT_FILE)

    file_output = file_output_factory(ROOT_DIR, RELATIVE_DIR)

    cls.idhaar_rules = IdhaarRule(idhaar_file_input, file_output)

  # @classmethod
  # def tearDownClass(cls):
  #   absolute_dir_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
  #   shutil.rmtree(absolute_dir_path)

  def test_extract_rule_data(cls):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    if not os.path.exists(absolute_specs_path):
      os.makedirs(absolute_specs_path)
      
    idhaar_file = os.path.join(absolute_specs_path, 'idhaar.json')
    
    cls.idhaar_file_content = {}
    cls.idhaar_rules.generate_rule_file()

    noon_or_tanween = 'ٌٍن'
    idhaar_letters = 'هءأإحعخغ'

    with open(idhaar_file) as idhaar:
      cls.idhaar_file_content = json.load(idhaar)
      idhaar.close()

    cls.assertIsInstance(cls.idhaar_file_content['idhaar'], list)

    quran_file = open(IDHAAR_INPUT_FILE, 'r', encoding='utf-8')
    for line in quran_file.readlines():
      segments = line.split('|')
      ayah_number = int(segments[1])
      ayah_text = segments[2].strip()

      starts_for_line = [rule['start'] for rule in cls.idhaar_file_content['idhaar'] if rule['ayah'] == ayah_number]

      for start in starts_for_line:
        cls.assertTrue(ayah_text[start] or ayah_text[start+1] in noon_or_tanween)

      ends_for_line = [rule['end'] for rule in cls.idhaar_file_content['idhaar'] if rule['ayah'] == ayah_number]

      for end in ends_for_line:
        cls.assertTrue(ayah_text[end] in idhaar_letters)
    quran_file.close()
 

    
    