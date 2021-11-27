import unittest, os, shutil, json
from src.gateways.file_to_map_gateway import FileToMapGateway
from src.gateways.local_file_system import LocalFileSystem

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/idhaar_mock_input.txt')
ENTITIES_DIR = os.path.join(ROOT, 'entities')
OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs', 'specs')

FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': ENTITIES_DIR,
	'outputs_dir': OUTPUTS_DIR
}

mock_file_system = LocalFileSystem(FILES_SYS)
mock_file_to_map_gateway = FileToMapGateway(mock_file_system)

class TestFileToMapGateway(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.makedirs(OUTPUTS_DIR)

  @classmethod
  def tearDownClass(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs'))

  def test_get_rule_names(self):
    rule_names = mock_file_to_map_gateway.get_rule_names()
    self.assertTrue(type(rule_names), list)
    # self.assertIn('madd_6', rule_names)
    self.assertIn('idhaar_shafawi', rule_names)
    # self.assertIn('qalqalah', rule_names)
    # self.assertIn('ikhfa', rule_names)
    # self.assertIn('ghunnah', rule_names)
    self.assertNotIn('__init__', rule_names)
    self.assertNotIn('entities_map', rule_names)

  # def test_get_rule_class_from_name(self):
  #   madd = mock_file_to_map_gateway.get_rule_class_from_name('madd_6')
  #   qalqalah = mock_file_to_map_gateway.get_rule_class_from_name('qalqalah')
    
  #   self.assertEqual(madd, 'Madd6')
  #   self.assertEqual(qalqalah, 'Qalqalah')
 