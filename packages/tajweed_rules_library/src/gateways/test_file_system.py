import unittest
import os
import shutil
import json
from src.gateways.file_system import FileSystem

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/partial_quran_input.txt')
ENTITIES_DIR = os.path.join(ROOT, 'fixtures/mock_fixtures/entities')
OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs')

FILES_SYS = {
  'root': ROOT,
  'input_file': INPUT_FILE,
  'entities_dir': ENTITIES_DIR,
  'outputs_dir': os.path.join(OUTPUTS_DIR, 'specs')
}

mock_file_system = FileSystem()

class TestFileSystem(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.mkdir(OUTPUTS_DIR)
      os.mkdir(os.path.join(OUTPUTS_DIR, 'specs'))
      os.mkdir(os.path.join(OUTPUTS_DIR, 'dist'))
  
  def setUp(cls):
    if not os.path.exists(os.path.join(OUTPUTS_DIR, 'specs')):
      os.mkdir(os.path.join(OUTPUTS_DIR, 'specs'))
      
  @classmethod
  def tearDownClass(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs'))

  def test_get_files_in_nested_directory(self):
    filenames = mock_file_system.get_files_in_directory(ENTITIES_DIR)
    self.assertTrue(type(filenames), list)
    self.assertIsInstance(filenames[0], dict)
    self.assertTrue({'name': 'meem_saakin_rules.py', 'absolute_path': os.path.join(ENTITIES_DIR, 'meem_saakin_rules', 'meem_saakin_rules.py')} in filenames)
    self.assertTrue({'name': 'noon_saakin_rules.py', 'absolute_path': os.path.join(ENTITIES_DIR, 'noon_saakin_rules', 'noon_saakin_rules.py')} in filenames)

  def test_get_files_in_flat_directory(self):
    content = {'test': 'I am some test content', }
    path = mock_file_system.create_absolute_path(FILES_SYS, 'test')
    mock_file_system.write_json_to_file(content, path)

    filenames = mock_file_system.get_files_in_directory(os.path.join(OUTPUTS_DIR, 'specs'))
    self.assertTrue(type(filenames), list)
    self.assertIsInstance(filenames[0], dict)
    self.assertTrue({'name': 'test.json', 'absolute_path': os.path.join(OUTPUTS_DIR, 'specs', 'test.json')} in filenames)

  def test_final_files_list_has_no_tests_or_init(self):
    filenames = mock_file_system.get_files_in_directory(ENTITIES_DIR)
    names_only = [rule['name'] for rule in filenames]
    self.assertFalse('__init__.py' in names_only)
    self.assertFalse('test_meem_saakin_rules.py' in names_only)
    self.assertTrue('meem_saakin_rules.py' in names_only)

  def test_read_file_by_lines(self):
    file_content = mock_file_system.read_file_by_lines(INPUT_FILE)
    first_line = file_content[0].strip('\n')
    last_line = file_content[len(file_content)-1].strip('/n')
    self.assertEqual(first_line, '105|4|تَرْمِيهِم بِحِجَارَةٍ مِّن سِجِّيلٍ')
    # self.assertEqual(last_line, '111|4|وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ')

  def test_create_absolute_path(self):
    absolute_path = mock_file_system.create_absolute_path(FILES_SYS, 'test')
    self.assertEqual(os.path.join(OUTPUTS_DIR, 'specs', 'test.json'), absolute_path)

  def test_write_json_to_file(self):
    content = {'test': 'I am some test content', }
    path = mock_file_system.create_absolute_path(FILES_SYS, 'test')
    mock_file_system.write_json_to_file(content, path)
    with open(os.path.join(OUTPUTS_DIR, 'specs', 'test.json')) as input_file:
      entire_file = json.load(input_file)
      self.assertEqual(entire_file, content)
    input_file.close()
      

  def test_copy_file_from_original_to_target_dir(self):
    content = {'test': 'I am some test content'}
    path = mock_file_system.create_absolute_path(FILES_SYS, 'test')
    mock_file_system.write_json_to_file(content, path)
    original = os.path.join(OUTPUTS_DIR, 'specs', 'test.json')
    mock_file_system.copy_file_from_original_to_target_dir(original, os.path.join(OUTPUTS_DIR, 'dist', 'test.json'))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'dist', 'test.json')))
    with open(os.path.join(OUTPUTS_DIR, 'dist', 'test.json')) as input_file:
      entire_file = json.load(input_file)
      self.assertEqual(entire_file, content)
    input_file.close()
      
  def test_empty_directory(self):
    dist_dir = os.path.join(OUTPUTS_DIR, 'dist')
    mock_file_system.empty_directory(dist_dir)
    self.assertEqual(len(os.listdir(dist_dir)), 0)
      
  def test_delete_directory(self):
    specs_dir = os.path.join(OUTPUTS_DIR, 'specs')
    mock_file_system.delete_directory(specs_dir)
    self.assertFalse(os.path.exists(specs_dir))