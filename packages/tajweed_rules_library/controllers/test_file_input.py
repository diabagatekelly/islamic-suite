import unittest
from controllers.input_factory import InputFactory

IDHAAR_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\mock_fixtures\\idhaar_mock_input.txt'
OTHER_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\mock_fixtures\\other_rules_mock_input.json'

idhaar_file_factory = InputFactory().get_input()
others_file_factory = InputFactory().get_input()

class TestFileInput(unittest.TestCase):
  
  def test_save_file_content_for_others(self):
    others_file_input = others_file_factory(OTHER_RULES_INPUT_FILE)
    all_rules = others_file_input.save_file_content()
    self.assertIsInstance(all_rules, dict)
    self.assertIsInstance(all_rules['data'], list)

  def test_read_quran_file(self):
    idhaar_file_input = idhaar_file_factory(IDHAAR_RULES_INPUT_FILE)
    quran = idhaar_file_input.read_quran_file()
    self.assertTrue(quran, list)

  def test_parse_quran_script(self):
    idhaar_file_input = idhaar_file_factory(IDHAAR_RULES_INPUT_FILE)
    quran = idhaar_file_input.read_quran_file()
    for line in quran:
      parsed_first_line = idhaar_file_input.parse_quran_script(line)
      self.assertTrue(parsed_first_line['surah_number'], 2)
      self.assertTrue(parsed_first_line['ayah_number'], 1)
      self.assertTrue(parsed_first_line['ayah_text'], 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ الٓمٓ')