import unittest, os, shutil
from unittest.mock import patch
from src.controllers.local_controller import LocalController
from src.use_cases.create_rules_maps import CreateRulesMaps

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/partial_quran_input.txt')
ENTITIES_DIR = os.path.join(ROOT, 'fixtures/mock_fixtures/entities')
OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs', 'specs')

MOCK_FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': ENTITIES_DIR,
	'outputs_dir': OUTPUTS_DIR
}

class TestLocalController(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.makedirs(OUTPUTS_DIR)

  @classmethod
  def tearDownClass(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs'))

  def test_init_controller_with_local_factory(self):
    local_file_controller = LocalController(files=MOCK_FILES_SYS)
    self.assertEqual(local_file_controller.factory.env, 'local')

  @patch.object(CreateRulesMaps, 'create_rule_maps')
  def test_create_rule_maps_called(self, mock):
    local_file_sys = LocalController(files=MOCK_FILES_SYS)
    local_file_sys.create_rule_maps()
    mock.assert_called()