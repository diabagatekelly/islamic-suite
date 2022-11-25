import unittest
import os
import shutil
import asyncio
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.use_cases.choose_rule_maps_to_create import ChooseRuleMapsToCreate
from src.factory import Factory

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/idhaar_mock_input.txt')
MOCK_ENTITIES_DIR = os.path.join(ROOT, 'fixtures/mock_fixtures/entities')
MOCK_OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_outputs', 'specs')
PROD_MOCK_OUTPUTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_dist', 'specs')

MOCK_FILES_SYS = {
  'root': ROOT,
  'input_file': INPUT_FILE,
  'entities_dir': MOCK_ENTITIES_DIR,
  'outputs_dir': MOCK_OUTPUTS_DIR
}

PROD_MOCK_FILES_SYS = {
  'root': ROOT,
  'local_outputs': MOCK_OUTPUTS_DIR,
  'outputs_dir': PROD_MOCK_OUTPUTS_DIR
}

mock_factory = Factory()
mock_choose_rules_to_create = ChooseRuleMapsToCreate(mock_factory, MOCK_FILES_SYS)

mock_prod_factory = Factory(env='prod')
prod_mock_choose_rules_to_create = ChooseRuleMapsToCreate(mock_prod_factory, PROD_MOCK_FILES_SYS)

class TestChooseRuleMapsToCreate(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    if not os.path.exists(MOCK_OUTPUTS_DIR):
      os.makedirs(MOCK_OUTPUTS_DIR)
      file1 = open(os.path.join(MOCK_OUTPUTS_DIR, 'temp_output.json'), 'w')
      file1.writelines('{"idghaam_shafawi": [{"surah": 2, "ayah": 10, "start": 13, "end": 17}]')
      file1.close()
    if not os.path.exists(PROD_MOCK_OUTPUTS_DIR):
      os.makedirs(PROD_MOCK_OUTPUTS_DIR)

  @classmethod
  def tearDownClass(cls):
    if MOCK_OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_outputs'))
    if PROD_MOCK_OUTPUTS_DIR:
      shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'choose_dist'))


  # Helper async method for updating factory file
  async def delete_entities_file(self, file):
    return os.remove(os.path.join(MOCK_ENTITIES_DIR, 'meem_saakin_rules', file))

  async def write_to_entities_file(self, file, content=""):
    file_content = [f'class TestFile{content}:\n', '  def __init__(self):\n', '    pass']
    file1 = open(os.path.join(MOCK_ENTITIES_DIR, 'meem_saakin_rules', file), 'w')
    file1.writelines(file_content)
    file1.close()

  async def update_file(self, file):
    test_file = open(os.path.join(MOCK_ENTITIES_DIR, 'meem_saakin_rules', file), 'a')
    test_file.write('\n# I am a randomly added comment')
    test_file.close()

  def test_unmodified_file_not_mapped(self): 
    local_list = mock_choose_rules_to_create.get_list_of_json_maps_to_create()
    self.assertEqual(len(local_list), 0)
    
  def test_deleted_file_not_mapped(self):
    asyncio.run(self.delete_entities_file('temp_file_meem_to_delete.py'))
    local_list = mock_choose_rules_to_create.get_list_of_json_maps_to_create()
    self.assertEqual(len(local_list), 0)
    asyncio.run(self.write_to_entities_file('temp_file_meem_to_delete.py'))
    
  def test_new_file_is_mapped(self):
    asyncio.run(self.write_to_entities_file('temp_file_meem2_to_delete.py', '2'))
    local_list = mock_choose_rules_to_create.get_list_of_json_maps_to_create()
    self.assertEqual(len(local_list), 1)
    asyncio.run(self.delete_entities_file('temp_file_meem2_to_delete.py'))
    
  def test_modified_file_is_mapped(self):
    asyncio.run(self.update_file('temp_file_meem_to_delete.py'))
    local_list = mock_choose_rules_to_create.get_list_of_json_maps_to_create()
    self.assertEqual(len(local_list), 1)
    asyncio.run(self.delete_entities_file('temp_file_meem_to_delete.py'))
    asyncio.run(self.write_to_entities_file('temp_file_meem_to_delete.py'))
    
  def test_get_outputs_list_in_prod(self):
    prod_list = prod_mock_choose_rules_to_create.get_list_of_json_maps_to_create()
    expected_list_path = os.path.join(MOCK_OUTPUTS_DIR, 'temp_output.json')
    self.assertEqual(len(prod_list), 1)
    self.assertListEqual(prod_list, [{'name': 'temp_output', 'absolute_path': f'{expected_list_path}' }])