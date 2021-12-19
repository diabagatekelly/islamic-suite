import unittest, os, shutil, json
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.use_cases.choose_rule_maps_to_create import ChooseRuleMapsToCreate
from src.factory import Factory

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/idhaar_mock_input.txt')
ENTITIES_DIR = os.path.join(ROOT, 'fixtures/mock_fixtures/entities')
OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'create_outputs', 'specs')

FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': ENTITIES_DIR,
	'outputs_dir': OUTPUTS_DIR
}

mock_factory = Factory()
create_rule_maps = CreateRulesMaps(mock_factory, FILES_SYS)
choose_rules_to_create = ChooseRuleMapsToCreate(mock_factory, FILES_SYS)

class TestCreateRulesMaps(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.makedirs(OUTPUTS_DIR)

  @classmethod
  def tearDownClass(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'create_outputs'))

  def test_create_rule_maps(self):
    rules_to_create = choose_rules_to_create.get_list_of_rule_maps_to_create()
    create_rule_maps.create_rule_maps(rules_to_create)
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'idghaam_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'idhaar_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'ikhfa_shafawi.json')))