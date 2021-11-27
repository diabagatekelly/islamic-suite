import unittest, os, shutil, json
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.factory import Factory

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

mock_factory = Factory(file_system=FILES_SYS)
create_rule_maps = CreateRulesMaps(mock_factory)

class TestCreateRulesMaps(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.makedirs(OUTPUTS_DIR)

  @classmethod
  def tearDownClass(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputs'))

  def test_create_rule_maps(self):
    create_rule_maps.create_rule_maps()
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'idghaam_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'idhaar_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'ikhfa_shafawi.json')))