import unittest
from controllers.file_input import FileInput

IDHAAR_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\specs\\idhaar_test_input.txt'
OTHER_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\specs\\other_rules_test_input.json'

idhaar_file_input = FileInput(IDHAAR_RULES_INPUT_FILE)
others_file_input = FileInput(OTHER_RULES_INPUT_FILE)

class TestFileInput(unittest.TestCase):
  
  def test_save_file_content_for_others(self):
    all_rules = others_file_input.save_file_content()
    self.assertIsInstance(all_rules, dict)
    self.assertIsInstance(all_rules['data'], list)

  def test_parse_quran_script(self):
    quran = idhaar_file_input.open_quran_file()
    for line in quran:
      parsed_first_line = idhaar_file_input.parse_quran_script(line)
      self.assertTrue(parsed_first_line['surah_number'], 2)
      self.assertTrue(parsed_first_line['ayah_number'], 1)
      self.assertTrue(parsed_first_line['ayah_text'], 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ الٓمٓ')
      return
    quran.close()
