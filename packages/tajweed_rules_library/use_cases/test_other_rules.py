import unittest, os, shutil
from use_cases.other_rules import OtherRules
from controllers.input_factory import InputFactory
from presenters.output_factory import OutputFactory

class TestOtherRules(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    file_input_factory = InputFactory().get_input()
    file_output_factory = OutputFactory().get_output()

    OTHER_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\mock_fixtures\\other_rules_mock_input.json'
    others_file_input = file_input_factory(OTHER_RULES_INPUT_FILE)

    cls.ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
    cls.RELATIVE_DIR = 'use_cases\\other_specs'

    file_output = file_output_factory(cls.ROOT_DIR, cls.RELATIVE_DIR)

    cls.other_rules = OtherRules(others_file_input, file_output)

  @classmethod
  def tearDownClass(cls):
    absolute_dir_path = os.path.join(cls.ROOT_DIR, cls.RELATIVE_DIR)
    shutil.rmtree(absolute_dir_path)

  def test_extract_rule_data_with_single_instance(cls):
    cls.madd_246_file_content = {}

    rules_location = cls.other_rules.extract_rule_data('madd_246')
    cls.madd_246_file_content = rules_location

    cls.assertIsInstance(cls.madd_246_file_content['madd_246'], list)
    cls.assertEqual(len(cls.madd_246_file_content['madd_246']), 1)
    cls.assertEqual(cls.madd_246_file_content['madd_246'][0], {"ayah": 1, "surah": 1, "start": 35, "end": 36})

  def test_extract_rule_data_with_multiple_instances(cls):
    cls.hamzat_wasl_file_content = {}

    rules_location = cls.other_rules.extract_rule_data('hamzat_wasl')
    cls.hamzat_wasl_file_content = rules_location

    cls.assertIsInstance(cls.hamzat_wasl_file_content['hamzat_wasl'], list)
    cls.assertEqual(len(cls.hamzat_wasl_file_content['hamzat_wasl']), 3)
    cls.assertEqual(cls.hamzat_wasl_file_content['hamzat_wasl'], [{"ayah": 1, "surah": 1, "start": 7, "end": 8},{"ayah": 1, "surah": 1, "start": 15, "end": 16}, {"ayah": 1, "surah": 1, "start": 28, "end": 29}])

  def test_generate_rule_files(cls):
    absolute_specs_path = os.path.join(cls.ROOT_DIR, cls.RELATIVE_DIR)
    if not os.path.exists(absolute_specs_path):
      os.makedirs(absolute_specs_path)

    cls.other_rules.generate_rule_files()
    cls.assertTrue(os.path.exists(os.path.join(absolute_specs_path, 'ghunnah.json')))
    cls.assertTrue(os.path.exists(os.path.join(absolute_specs_path, 'idghaam_mutajanisayn.json')))
    cls.assertFalse(os.path.exists(os.path.join(absolute_specs_path, 'idhaar.json')))
    cls.assertFalse(os.path.exists(os.path.join(absolute_specs_path, 'idhaar_shafawi.json')))
