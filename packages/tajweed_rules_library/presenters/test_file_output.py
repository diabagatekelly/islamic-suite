import unittest, os
from presenters.file_output import FileOutput

ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
RELATIVE_DIR = 'specs'

file_output = FileOutput(ROOT_DIR, RELATIVE_DIR)

class TestFileOutput(unittest.TestCase):
  @classmethod
  def tearDownClass(cls):
    absolute_path = os.path.join(ROOT_DIR, RELATIVE_DIR, 'test.json')
    os.remove(os.path.join((absolute_path)))
  
  def test_create_absolute_output_path(self):
    absolute_path = file_output.create_absolute_output_path('test')
    self.assertEqual(absolute_path, 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\specs\\test.json')

  def test_write_to_output_file(self):
    absolute_path = file_output.create_absolute_output_path('test')
    file_output.write_to_output_file('{I was written in this file}', absolute_path)
    self.assertTrue(os.path.exists(absolute_path))
