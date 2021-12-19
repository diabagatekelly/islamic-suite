import unittest, os, shutil, json
from src.gateways.file_to_map_gateway import FileToMapGateway
from src.gateways.file_system import FileSystem

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/idhaar_mock_input.txt')
ENTITIES_DIR = os.path.join(ROOT, 'fixtures/mock_fixtures/entities')
OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs', 'specs')

FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': ENTITIES_DIR,
	'outputs_dir': OUTPUTS_DIR
}

mock_file_to_map_gateway = FileToMapGateway()

class TestFileToMapGateway(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.makedirs(OUTPUTS_DIR)

  @classmethod
  def tearDownClass(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs'))

  def test_get_name_from_file(self):
    rule_name = mock_file_to_map_gateway.get_name_from_file('idhaar_shafawi.py')
    self.assertEqual('idhaar_shafawi', rule_name)

  def test_get_rule_class_from_name(self):
    madd = mock_file_to_map_gateway.get_rule_class_from_name('madd_6')
    qalqalah = mock_file_to_map_gateway.get_rule_class_from_name('qalqalah')
    
    self.assertEqual(madd, 'Madd6')
    self.assertEqual(qalqalah, 'Qalqalah')
 