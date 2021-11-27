import unittest, os, shutil
from unittest.mock import patch
from src.controllers.local_file_system_controller import LocalFileSystemController

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

class TestLocalFileSystemController(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.makedirs(OUTPUTS_DIR)

  @classmethod
  def tearDownClass(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs'))

  def test_init_controller_with_custom_file_sys(self):
    custom_file_system_controller = LocalFileSystemController(file_system=FILES_SYS)
    controller_factory = custom_file_system_controller.factory
    local_file_system = controller_factory.get_input_system()
    self.assertEqual(local_file_system.input_file, os.path.join(ROOT, 'fixtures/mock_fixtures/idhaar_mock_input.txt'))

  @patch.object(LocalFileSystemController, 'set_up_mapper')
  def test_set_up_mapper_called_on_init(self, mock):
    LocalFileSystemController(file_system=FILES_SYS)
    mock.assert_called()

    
  