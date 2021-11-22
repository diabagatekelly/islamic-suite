import unittest, os, json, shutil

ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
RELATIVE_SPECS_DIR = 'entities\\specs_fixtures'
# RELATIVE_OUTPUT_DIR = 'entities\\output_files'
RELATIVE_OUTPUT_DIR = 'use_cases\\idhaar_specs'
RULES = ["ghunnah", "idghaam_ghunnah", "idghaam_no_ghunnah", "idghaam_mutajanisayn",
    "idghaam_mutaqaribayn", "idghaam_shafawi", "ikhfa", "ikhfa_shafawi", "idhaar",
    "idhaar_shafawi", "iqlab", "madd_246", "madd_muttasil", "madd_munfasil", "madd_6", "qalqalah", "idhaar", "idhaar_shafawi"]

class TestOutputFixtures(unittest.TestCase):

  # def test_all_output_fixture_equal_all_specs(self):
  #   absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_SPECS_DIR)
  #   absolute_output_path = os.path.join(ROOT_DIR, RELATIVE_OUTPUT_DIR)

  #   # for rule in RULES:
  #   specs_file = 'tajweed.idhaar.json'
  #   with open(os.path.join(absolute_specs_path, specs_file)) as input_file:
  #     spec_content = json.load(input_file)
  #     input_file.close()

  #   output_file = 'idhaar.json'
  #   with open(os.path.join(absolute_output_path, output_file)) as input_file:
  #     output_content = json.load(input_file)
  #     input_file.close()

  #   self.assertEqual(spec_content, output_content)


  def test_ghunna_spec_equals_ghunnah_spec(self):
    absolute_specs_path = os.path.join(ROOT_DIR, RELATIVE_SPECS_DIR)

    with open(os.path.join(absolute_specs_path, 'tajweed.ghunnah.json')) as input_file:
      ghunnah = json.load(input_file)
      input_file.close()

    with open(os.path.join(absolute_specs_path, 'tajweed.ghunnah2.json')) as input_file:
      ghunnah2 = json.load(input_file)
      input_file.close()

    self.assertEqual(ghunnah, ghunnah2)