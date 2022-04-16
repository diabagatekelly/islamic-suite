import unittest, os, shutil
import asyncio
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.use_cases.choose_rule_maps_to_create import ChooseRuleMapsToCreate
from src.factory import Factory

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/idhaar_mock_input.txt')
TEMP_MOCK_ENTITIES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_entities')
MOCK_ENTITIES_DIR = os.path.join(ROOT, 'fixtures/mock_fixtures/entities')
MOCK_OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_outputs', 'specs')

MOCK_FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': TEMP_MOCK_ENTITIES_DIR,
	'outputs_dir': MOCK_OUTPUTS_DIR
}

mock_factory = Factory()
mock_create_rule_maps = CreateRulesMaps(mock_factory, MOCK_FILES_SYS)
mock_choose_rules_to_create = ChooseRuleMapsToCreate(mock_factory, MOCK_FILES_SYS)


class TestChooseRuleMapsToCreate(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(MOCK_OUTPUTS_DIR):
      os.makedirs(MOCK_OUTPUTS_DIR)
    if not os.path.exists(TEMP_MOCK_ENTITIES_DIR):
      shutil.copytree(MOCK_ENTITIES_DIR, TEMP_MOCK_ENTITIES_DIR)

  @classmethod
  def tearDown(cls):
    if MOCK_OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_outputs'))
      os.makedirs(MOCK_OUTPUTS_DIR)

  @classmethod
  def tearDownClass(cls):
    if MOCK_OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_outputs'))
    if TEMP_MOCK_ENTITIES_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_entities'))

  # Helper async methods for removing a map from outputs
  async def evaluate_rules_after_deletion(self):
    removed = await self.remove_file()
    partial_rules_to_create = mock_choose_rules_to_create.get_list_of_rule_maps_to_create()
    return partial_rules_to_create

  async def remove_file(self):
    return os.remove(os.path.join(MOCK_OUTPUTS_DIR, 'idghaam_shafawi.json'))

  # Helper async method for updating an entity definition file
  async def evaluate_rules_after_update(self):
    updated = await self.update_file(os.path.join(TEMP_MOCK_ENTITIES_DIR, 'meem_saakin_rules', 'idhaar_shafawi.py'))
    idhaar_rule_to_create = mock_choose_rules_to_create.get_list_of_rule_maps_to_create()
    return idhaar_rule_to_create

  #Helper async method for updating factory file
  async def evaluate_rules_after_factory_update(self):
    updated = await self.update_file(os.path.join(TEMP_MOCK_ENTITIES_DIR, 'meem_saakin_rules', 'meem_saakin_rule_factory.py'))
    all_rules_to_create = mock_choose_rules_to_create.get_list_of_rule_maps_to_create()
    return all_rules_to_create

  async def update_file(self, file):
    idhaar_rules_def = open(file, 'a')
    idhaar_rules_def.write('\n# I am a randomly added comment')
    idhaar_rules_def.close()


  def test_get_list_of_rule_maps_to_create(self):
    rules_to_create = mock_choose_rules_to_create.get_list_of_rule_maps_to_create()
    self.assertTrue('idghaam_shafawi' in rules_to_create)
    self.assertTrue('idhaar_shafawi' in rules_to_create)
    self.assertTrue('ikhfa_shafawi' in rules_to_create)

  def test_get_rule_map_with_existing_maps_with_no_update(self):
    all_rules_to_create = mock_choose_rules_to_create.get_list_of_rule_maps_to_create()
    mock_create_rule_maps.create_rule_maps(all_rules_to_create)
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
  
  def test_get_all_rule_maps_with_factory_file_update(self):
    all_rules = mock_choose_rules_to_create.get_list_of_rule_maps_to_create()
    mock_create_rule_maps.create_rule_maps(all_rules)
    all_rules_to_create = asyncio.run(self.evaluate_rules_after_factory_update())
    self.assertTrue('idghaam_shafawi' in all_rules_to_create)
    self.assertTrue('ikhfa_shafawi' in all_rules_to_create)
    self.assertTrue('idhaar_shafawi' in all_rules_to_create)