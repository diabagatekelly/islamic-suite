import unittest, os, shutil
from unittest.mock import patch
from src.controllers.prod_controller import ProdController
from src.use_cases.create_rules_maps import CreateRulesMaps

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
LOCAL_OUTPUTS = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs', 'specs')
PROD_OUTPUTS = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dist', 'specs')

FILES_SYS = {
	'root': ROOT,
	'local_outputs': LOCAL_OUTPUTS,
	'outputs_dir': PROD_OUTPUTS
}

class TestProdController(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(PROD_OUTPUTS):
      os.makedirs(PROD_OUTPUTS)
    if not os.path.exists(LOCAL_OUTPUTS):
      os.makedirs(LOCAL_OUTPUTS)

  @classmethod
  def tearDownClass(cls):
    if PROD_OUTPUTS:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dist'))
    if LOCAL_OUTPUTS:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs'))

  def test_init_controller_with_prod_factory(self):
    prod_file_controller = ProdController(files=FILES_SYS)
    self.assertEqual(prod_file_controller.factory.env, 'prod')

  @patch.object(CreateRulesMaps, 'create_rule_maps')
  def test_create_rule_maps_called(self, mock):
    local_file_sys = ProdController(files=FILES_SYS)
    local_file_sys.create_rule_maps()
    mock.assert_called()