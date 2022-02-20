import unittest, os, shutil
import asyncio
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.use_cases.choose_rule_maps_to_create import ChooseRuleMapsToCreate
from src.factory import Factory

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/idhaar_mock_input.txt')
MOCK_ENTITIES_DIR = os.path.join(ROOT, 'fixtures/mock_fixtures/entities')
ENTITIES_DIR = os.path.join(ROOT, 'entities')
OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_outputs', 'specs')

MOCK_FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': MOCK_ENTITIES_DIR,
	'outputs_dir': OUTPUTS_DIR
}

FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': ENTITIES_DIR,
	'outputs_dir': OUTPUTS_DIR
}

mock_factory = Factory()
mock_create_rule_maps = CreateRulesMaps(mock_factory, MOCK_FILES_SYS)
mock_choose_rules_to_create = ChooseRuleMapsToCreate(mock_factory, MOCK_FILES_SYS)

create_rule_maps = CreateRulesMaps(mock_factory, FILES_SYS)
choose_rules_to_create = ChooseRuleMapsToCreate(mock_factory, FILES_SYS)

class TestChooseRuleMapsToCreate(unittest.TestCase):
  @classmethod
  def setUp(cls):
    if not os.path.exists(OUTPUTS_DIR):
      os.makedirs(OUTPUTS_DIR)

  @classmethod
  def tearDown(cls):
    if OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_outputs'))

  async def remove_file(self):
    return os.remove(os.path.join(OUTPUTS_DIR, 'idghaam_shafawi.json'))

  async def evaluate_rules_after_deletion(self):
    removed = await self.remove_file()
    partial_rules_to_create = choose_rules_to_create.get_list_of_rule_maps_to_create()
    return partial_rules_to_create

  async def update_file(self):
    idhaar_rules_def = open(os.path.join(MOCK_ENTITIES_DIR, 'meem_saakin_rules', 'idhaar_shafawi.py'), 'a')
    idhaar_rules_def.write('# I am a randomly added comment\n')
    idhaar_rules_def.close()

  async def evaluate_rules_after_update(self):
    updated = await self.update_file()
    idhaar_rule_to_create = mock_choose_rules_to_create.get_list_of_rule_maps_to_create()
    return idhaar_rule_to_create

  def remove_added_line_from_file(self):
    readFile = open(os.path.join(MOCK_ENTITIES_DIR, 'meem_saakin_rules', 'idhaar_shafawi.py'))
    lines = readFile.readlines()
    readFile.close()

    w = open(os.path.join(MOCK_ENTITIES_DIR, 'meem_saakin_rules', 'idhaar_shafawi.py'), 'w')
    w.writelines([item for item in lines[:-1]])

    w.close()

  def test_get_list_of_rule_maps_to_create(self):
    rules_to_create = choose_rules_to_create.get_list_of_rule_maps_to_create()
    self.assertTrue('idghaam_shafawi' in rules_to_create)
    self.assertTrue('idhaar_shafawi' in rules_to_create)
    self.assertTrue('ikhfa_shafawi' in rules_to_create)

  def test_get_rule_map_with_existing_maps_with_no_update(self):
    all_rules_to_create = choose_rules_to_create.get_list_of_rule_maps_to_create()
    create_rule_maps.create_rule_maps(all_rules_to_create)
    partial_rules_to_create = asyncio.run(self.evaluate_rules_after_deletion())
    self.assertTrue('idghaam_shafawi' in partial_rules_to_create)
    self.assertFalse('idhaar_shafawi' in partial_rules_to_create)
    self.assertFalse('ikhfa_shafawi' in partial_rules_to_create)

  def test_get_rule_map_with_existing_maps_with_update(self):
    all_rules = mock_choose_rules_to_create.get_list_of_rule_maps_to_create()
    mock_create_rule_maps.create_rule_maps(all_rules)
    idhaar_rule_to_create = asyncio.run(self.evaluate_rules_after_update())
    self.assertFalse('idghaam_shafawi' in idhaar_rule_to_create)
    self.assertFalse('ikhfa_shafawi' in idhaar_rule_to_create)
    self.assertTrue('idhaar_shafawi' in idhaar_rule_to_create)

    self.remove_added_line_from_file()