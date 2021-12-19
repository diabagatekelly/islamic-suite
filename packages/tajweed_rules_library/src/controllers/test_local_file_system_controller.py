import unittest, os, shutil
from unittest.mock import patch
from src.controllers.local_file_system_controller import LocalFileSystemController
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.use_cases.choose_rule_maps_to_create import ChooseRuleMapsToCreate

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

class TestLocalFileSystemController(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.makedirs(OUTPUTS_DIR)

  @classmethod
  def tearDownClass(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs'))

  def test_init_controller_with_local_factory(self):
    local_file_controller = LocalFileSystemController(files=FILES_SYS)
    self.assertEqual(local_file_controller.factory.env, 'local')

  @patch.object(CreateRulesMaps, 'create_rule_maps')
  def test_create_rule_maps_called(self, mock):
    local_file_sys = LocalFileSystemController(files=FILES_SYS)
    local_file_sys.create_rule_maps()
    mock.assert_called()

    
  