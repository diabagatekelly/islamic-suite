import unittest, os, json, shutil
from use_cases.single_rule_files import SingleRuleFiles
from use_cases.idhaar_rule_files import IdhaarRuleFiles
from use_cases.idhaar_rules_factory import IdhaarRulesFactory

INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\tajweed_hafs_uthmani_pause_sajdah.json'
ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
RELATIVE_DIR = 'use_cases\\specs'
IDHAAR_RULES_CLASS_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\quran-uthmani.txt'

class TestSingleRuleFiles(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.single_rule_files = SingleRuleFiles(INPUT_FILE, ROOT_DIR, RELATIVE_DIR)

  @classmethod
  def tearDownClass(cls):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    shutil.rmtree(absolute_specs_path)

  def test_file_content_saved_on_class_init(cls):
    cls.assertEqual(cls.single_rule_files.input_file, 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\tajweed_hafs_uthmani_pause_sajdah.json')
    cls.assertEqual(cls.single_rule_files.rules[0], 'ghunnah')
    cls.assertIsInstance(cls.single_rule_files.all_rules, dict)
    cls.assertTrue(len(cls.single_rule_files.all_rules) > 0)
    
    partial_file_content = {'annotations': [{'end': 8, 'rule': 'hamzat_wasl', 'start': 7}, {'end': 16, 'rule': 'hamzat_wasl', 'start': 15}, {'end': 17, 'rule': 'lam_shamsiyyah', 'start': 16}, {'end': 25, 'rule': 'madd_2', 'start': 24}, {'end': 29, 'rule': 'hamzat_wasl', 'start': 28}, {'end': 30, 'rule': 'lam_shamsiyyah', 'start': 29}, {'end': 36, 'rule': 'madd_246', 'start': 35}], 'ayah': 1, 'surah': 1}
    cls.assertEqual(cls.single_rule_files.all_rules['data'][0], partial_file_content)

  def test_create_individual_rule_files(cls):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    if not os.path.exists(absolute_specs_path):
      os.makedirs(absolute_specs_path)
    
    cls.single_rule_files.generate_rule_files()
   
    cls.assertEqual(len(cls.single_rule_files.rules), len(os.listdir(absolute_specs_path)))
    cls.assertTrue(os.path.exists(os.path.join(absolute_specs_path, 'ghunnah.json')))
    cls.assertTrue(os.path.exists(os.path.join(absolute_specs_path, 'madd_muttasil.json')))
    

  def test_file_content_is_extracted_rule_data(cls):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    ghunnah_file = os.path.join(absolute_specs_path, 'ghunnah.json')
    cls.ghunnah_file_content = {}

    with open(ghunnah_file) as ghunnah:
      cls.ghunnah_file_content = json.load(ghunnah)
      ghunnah.close()

    cls.assertIsInstance(cls.ghunnah_file_content['ghunnah'], list)
    cls.assertEqual(cls.ghunnah_file_content['ghunnah'][0], {"ayah": 3, "surah": 2, "start": 63, "end": 66})
