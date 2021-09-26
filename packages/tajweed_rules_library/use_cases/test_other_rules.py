from use_cases.other_rules import OtherRules
from use_cases.rule import Rule
from controllers.input_factory import InputFactory
from presenters.output_factory import OutputFactory
import unittest, os, json

class TestOtherRules(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    file_input_factory = InputFactory('').get_input()
    file_output_factory = OutputFactory('').get_output()

    OTHER_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\specs\\other_rules_test_input.json'
    others_file_input = file_input_factory(OTHER_RULES_INPUT_FILE)

    cls.ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
    cls.RELATIVE_DIR = 'specs'

    file_output = file_output_factory(cls.ROOT_DIR, cls.RELATIVE_DIR)

    cls.other_rules = OtherRules(others_file_input, file_output)

  def test_extract_rule_data(cls):
    absolute_specs_path = os.path.join(cls.ROOT_DIR, cls.RELATIVE_DIR)
    ghunnah_file = os.path.join(absolute_specs_path, 'ghunnah.json')
    cls.ghunnah_file_content = {}

    cls.other_rules.generate_rule_files()
    cls.other_rules.extract_rule_data('ghunnah')

    with open(ghunnah_file) as ghunnah:
      cls.ghunnah_file_content = json.load(ghunnah)
      ghunnah.close()

    cls.assertIsInstance(cls.ghunnah_file_content['ghunnah'], list)
    # cls.assertEqual(cls.ghunnah_file_content['ghunnah'][0], {"ayah": 3, "surah": 2, "start": 63, "end": 66})
