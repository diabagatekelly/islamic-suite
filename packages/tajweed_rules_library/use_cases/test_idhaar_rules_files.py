import unittest, os, json, shutil
from use_cases.idhaar import Idhaar
from controllers.input_factory import InputFactory
from presenters.output_factory import OutputFactory

SINGLE_RULE_CLASS_INPUT = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\tajweed_hafs_uthmani_pause_sajdah.json'
IDHAAR_RULES_CLASS_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\quran-uthmani.txt'
ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
RELATIVE_DIR = 'use_cases\\idhaar_specs'

class TestIdhaarRuleFiles(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    file_input_factory = InputFactory().get_input()
    file_output_factory = OutputFactory().get_output()

    IDHAAR_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\mock_fixtures\\idhaar_mock_input.txt'
    idhaar_file_input = file_input_factory(IDHAAR_INPUT_FILE)

    file_output = file_output_factory(ROOT_DIR, RELATIVE_DIR)

    cls.idhaar_rules = Idhaar(idhaar_file_input, file_output)

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

    with open(idhaar_file) as idhaar:
      cls.idhaar_file_content = json.load(idhaar)
      idhaar.close()

    cls.assertIsInstance(cls.idhaar_file_content['idhaar'], list)
    cls.assertEqual(cls.idhaar_file_content['idhaar'][0], {"surah": 1, "ayah": 7, "start": 20, "end": 22})


  # def test_idhaar_shafawi_file_content_is_extracted_rule_data(cls):
  #   absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
  #   idhaar_shafawi_file = os.path.join(absolute_specs_path, 'idhaar_shafawi.json')
  #   cls.idhaar_shafawi_file_content = {}

  #   with open(idhaar_shafawi_file) as idhaar_shafawi:
  #     cls.idhaar_shafawi_file_content = json.load(idhaar_shafawi)
  #     idhaar_shafawi.close()

  #   cls.assertIsInstance(cls.idhaar_shafawi_file_content['idhaar_shafawi'], list)
  #   cls.assertEqual(cls.idhaar_shafawi_file_content['idhaar_shafawi'][0], {"surah": 1, "ayah": 2, "start": 5, "end": 7})

    
    