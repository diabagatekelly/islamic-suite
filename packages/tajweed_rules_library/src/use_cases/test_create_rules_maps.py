import unittest
import os
import shutil
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.factory import Factory

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/mock_fixtures/partial_quran_input.txt')
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

prod_mock_factory = Factory('prod')
prod_create_rule_maps = CreateRulesMaps(prod_mock_factory, PROD_FILES_SYS)

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

  def get_file_content(self, file):
    file_content = []
    file = open(file, 'r', encoding='utf-8')
    for line in file.readlines():
      file_content.append(line)
    file.close()
    return file_content
  
  def test_create_rule_maps_for_local(self):
    rules_to_create = ['MeemSaakinRules']
    local_create_rule_maps.create_rule_maps(rules_to_create)
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'specs', 'idghaam_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'specs', 'idhaar_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'specs', 'ikhfa_shafawi.json')))

  def test_getting_correct_map_content_meem_saakin_rules(self):
    local_rules_to_create = ['MeemSaakinRules']
    local_create_rule_maps.create_rule_maps(local_rules_to_create)
    
    idghaam_shafawi_content = self.get_file_content(os.path.join(OUTPUTS_DIR, 'specs', 'idghaam_shafawi.json'))
    idghaam_shafawi_expected_content = '{"idghaam_shafawi": [{"surah": 106, "ayah": 4, "start": 19, "end": 23}, {"surah": 106, "ayah": 4, "start": 43, "end": 47}]}'
    self.assertEqual(idghaam_shafawi_content[0], idghaam_shafawi_expected_content)

    ikhfa_shafawi_content = self.get_file_content(os.path.join(OUTPUTS_DIR, 'specs', 'ikhfa_shafawi.json'))
    expected_ikhfa_shafawi_content = '{"ikhfa_shafawi": [{"surah": 105, "ayah": 4, "start": 9, "end": 13}]}'
    self.assertEqual(ikhfa_shafawi_content[0], expected_ikhfa_shafawi_content)
    
    idhaar_shafawi_content = self.get_file_content(os.path.join(OUTPUTS_DIR, 'specs', 'idhaar_shafawi.json'))
    expected_idhaar_shafawi_content = '{"idhaar_shafawi": [{"surah": 111, "ayah": 4, "start": 3, "end": 7}]}'
    self.assertEqual(idhaar_shafawi_content[0], expected_idhaar_shafawi_content)
    
  def test_getting_correct_map_content_noon_saakin_rules(self):
    local_rules_to_create = ['NoonSaakinRules']
    local_create_rule_maps.create_rule_maps(local_rules_to_create)
    # ['iqlab']
    
    idghaam_ghunnah_content = self.get_file_content(os.path.join(OUTPUTS_DIR, 'specs', 'idghaam_ghunnah.json'))
    idghaam_ghunnah_expected_content = '{"idghaam_ghunnah": [{"surah": 105, "ayah": 4, "start": 20, "end": 25}, {"surah": 106, "ayah": 4, "start": 29, "end": 34}]}'
    self.assertEqual(idghaam_ghunnah_content[0], idghaam_ghunnah_expected_content)

    ikhfa_content = self.get_file_content(os.path.join(OUTPUTS_DIR, 'specs', 'ikhfa.json'))
    expected_ikhfa_content = '{"ikhfa": [{"surah": 105, "ayah": 4, "start": 26, "end": 30}, {"surah": 106, "ayah": 4, "start": 24, "end": 28}]}'
    self.assertEqual(ikhfa_content[0], expected_ikhfa_content)
    
    idhaar_content = self.get_file_content(os.path.join(OUTPUTS_DIR, 'specs', 'idhaar.json'))
    expected_idhaar_content = '{"idhaar": [{"surah": 106, "ayah": 4, "start": 48, "end": 53}]}'
    self.assertEqual(idhaar_content[0], expected_idhaar_content)
    
    idghaam_no_ghunnah_content = self.get_file_content(os.path.join(OUTPUTS_DIR, 'specs', 'idghaam_no_ghunnah.json'))
    expected_idghaam_no_ghunnah_content = '{"idghaam_no_ghunnah": [{"surah": 56, "ayah": 3, "start": 7, "end": 12}]}'
    self.assertEqual(idghaam_no_ghunnah_content[0], expected_idghaam_no_ghunnah_content)
    
    iqlab_content = self.get_file_content(os.path.join(OUTPUTS_DIR, 'specs', 'iqlab.json'))
    expected_iqlab_content = '{"iqlab": [{"surah": 104, "ayah": 4, "start": 13, "end": 17}]}'
    self.assertEqual(iqlab_content[0], expected_iqlab_content)
    
    
  def test_create_rule_maps_for_prod(self):
    local_rules_to_create = ['MeemSaakinRules']
    local_create_rule_maps.create_rule_maps(local_rules_to_create)
    
    rules_to_create = [
      {'name': 'idghaam_shafawi', 'absolute_path': os.path.join(OUTPUTS_DIR, 'specs', 'idghaam_shafawi.json')},
      {'name': 'idhaar_shafawi', 'absolute_path': os.path.join(OUTPUTS_DIR, 'specs', 'idhaar_shafawi.json')},
      {'name': 'ikhfa_shafawi', 'absolute_path': os.path.join(OUTPUTS_DIR, 'specs', 'ikhfa_shafawi.json')}
    ]
    prod_create_rule_maps.create_rule_maps(rules_to_create)
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'dist', 'idghaam_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'dist', 'idhaar_shafawi.json')))
    self.assertTrue(os.path.exists(os.path.join(OUTPUTS_DIR, 'dist', 'ikhfa_shafawi.json')))