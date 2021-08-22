import unittest, os, json, shutil
from use_cases.idhaar_rule_files import IdhaarRuleFiles
from use_cases.idhaar_rules_factory import IdhaarRulesFactory

SINGLE_RULE_CLASS_INPUT = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\tajweed_hafs_uthmani_pause_sajdah.json'
IDHAAR_RULES_CLASS_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\quran-uthmani.txt'
ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
RELATIVE_DIR = 'use_cases\\specs'

class TestIdhaarRuleFiles(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    if not os.path.exists(absolute_specs_path):
      os.makedirs(absolute_specs_path)

    cls.idhaar_factory = IdhaarRulesFactory('idhaar', IDHAAR_RULES_CLASS_INPUT_FILE, ROOT_DIR, RELATIVE_DIR)
    cls.idhaar_rule_files = IdhaarRuleFiles(cls.idhaar_factory)

    cls.idhaar_shafawi_factory = IdhaarRulesFactory('idhaar_shafawi', IDHAAR_RULES_CLASS_INPUT_FILE, ROOT_DIR, RELATIVE_DIR)
    cls.idhaar_shafawi_rule_files = IdhaarRuleFiles(cls.idhaar_shafawi_factory)

  @classmethod
  def tearDownClass(cls):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    shutil.rmtree(absolute_specs_path)

  def test_create_idhaar_individual_rule_files(cls):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
       
    cls.assertTrue(os.path.exists(os.path.join(absolute_specs_path, 'idhaar.json')))
    cls.assertTrue(os.path.exists(os.path.join(absolute_specs_path, 'idhaar_shafawi.json')))
    

  def test_idhaar_file_content_is_extracted_rule_data(cls):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    idhaar_file = os.path.join(absolute_specs_path, 'idhaar.json')
    cls.idhaar_file_content = {}

    with open(idhaar_file) as idhaar:
      cls.idhaar_file_content = json.load(idhaar)
      idhaar.close()

    cls.assertIsInstance(cls.idhaar_file_content['idhaar'], list)
    cls.assertEqual(cls.idhaar_file_content['idhaar'][0], {"surah": 1, "ayah": 7, "start": 20, "end": 22})


  def test_idhaar_shafawi_file_content_is_extracted_rule_data(cls):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    idhaar_shafawi_file = os.path.join(absolute_specs_path, 'idhaar_shafawi.json')
    cls.idhaar_shafawi_file_content = {}

    with open(idhaar_shafawi_file) as idhaar_shafawi:
      cls.idhaar_shafawi_file_content = json.load(idhaar_shafawi)
      idhaar_shafawi.close()

    cls.assertIsInstance(cls.idhaar_shafawi_file_content['idhaar_shafawi'], list)
    cls.assertEqual(cls.idhaar_shafawi_file_content['idhaar_shafawi'][0], {"surah": 1, "ayah": 2, "start": 5, "end": 7})

    
    