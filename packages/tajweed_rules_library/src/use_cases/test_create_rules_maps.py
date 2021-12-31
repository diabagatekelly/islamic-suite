import unittest, os, shutil, json
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.use_cases.choose_rule_maps_to_create import ChooseRuleMapsToCreate
from src.factory import Factory

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/idhaar_mock_input.txt')
ENTITIES_DIR = os.path.join(ROOT, 'fixtures/mock_fixtures/entities')
OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'create_outputs')

LOCAL_FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': ENTITIES_DIR,
	'outputs_dir': os.path.join(OUTPUTS_DIR, 'specs')
}

PROD_FILES_SYS = {
	'root': ROOT,
	'local_outputs': os.path.join(OUTPUTS_DIR, 'specs'),
	'outputs_dir': os.path.join(OUTPUTS_DIR, 'dist')
}

local_mock_factory = Factory('local')
local_create_rule_maps = CreateRulesMaps(local_mock_factory, LOCAL_FILES_SYS)
local_choose_rules_to_create = ChooseRuleMapsToCreate(local_mock_factory, LOCAL_FILES_SYS)

prod_mock_factory = Factory('prod')
prod_create_rule_maps = CreateRulesMaps(prod_mock_factory, PROD_FILES_SYS)
prod_choose_rules_to_create = ChooseRuleMapsToCreate(prod_mock_factory, PROD_FILES_SYS)

class TestCreateRulesMaps(unittest.TestCase):
  @classmethod
  def setUp(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.mkdir(OUTPUTS_DIR)
      os.mkdir(os.path.join(OUTPUTS_DIR, 'specs'))
      os.mkdir(os.path.join(OUTPUTS_DIR, 'dist'))

  @classmethod
  def tearDown(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'create_outputs'))

  def test_create_rule_maps_for_local(self):
    rules_to_create = local_choose_rules_to_create.get_list_of_rule_maps_to_create()
    local_create_rule_maps.create_rule_maps(rules_to_create)
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'specs', 'idghaam_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'specs', 'idhaar_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'specs', 'ikhfa_shafawi.json')))

  def test_create_rule_maps_for_prod(self):
    rules_to_create = local_choose_rules_to_create.get_list_of_rule_maps_to_create()
    local_create_rule_maps.create_rule_maps(rules_to_create)
    rules_to_create = prod_choose_rules_to_create.get_list_of_rule_maps_to_create()
    prod_create_rule_maps.create_rule_maps(rules_to_create)
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'dist', 'idghaam_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'dist', 'idhaar_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'dist', 'ikhfa_shafawi.json')))