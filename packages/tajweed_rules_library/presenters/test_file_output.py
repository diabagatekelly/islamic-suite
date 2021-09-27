import unittest, os, shutil, json
from presenters.output_factory import OutputFactory

ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
RELATIVE_DIR = 'presenters\\specs'

test_output_factory = OutputFactory().get_output()

class TestFileOutput(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    absolute_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    os.mkdir(absolute_path)

  @classmethod
  def tearDownClass(cls):
    absolute_dir_path = os.path.join(ROOT_DIR, RELATIVE_DIR)
    shutil.rmtree(absolute_dir_path)
  
  def test_create_absolute_output_path(self):
    output_file = test_output_factory(ROOT_DIR, RELATIVE_DIR)
    absolute_path = output_file.create_absolute_output_path('test')
    self.assertEqual(absolute_path, 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\presenters\\specs\\test.json')

  def test_write_to_output_file(self):
    output_file = test_output_factory(ROOT_DIR, RELATIVE_DIR)
    absolute_path = output_file.create_absolute_output_path('test')
    random_json = {"test": 'I was written in this file'}
    output_file.write_to_output_file(random_json, absolute_path)
    
    with open(absolute_path) as test_file:
      line = json.load(test_file)
      self.assertEqual(line, random_json)
      test_file.close()
