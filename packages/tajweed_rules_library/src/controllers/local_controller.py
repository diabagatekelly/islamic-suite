import os

from src.factory import Factory
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.use_cases.choose_rule_maps_to_create import ChooseRuleMapsToCreate

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/input_fixtures/quran-uthmani.txt')
ENTITIES_DIR = os.path.join(ROOT, 'entities')
OUTPUTS_DIR = os.path.join(ROOT, 'outputs')

FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': ENTITIES_DIR,
	'outputs_dir': OUTPUTS_DIR
}
    
class LocalController():
  def __init__(self, env='local', files=FILES_SYS):
    self
    self.factory = Factory(env)
    self.files = files

  def create_rule_maps(self):
    rule_creator = CreateRulesMaps(self.factory, files_and_dirs=self.files)
    rule_selector = self._choose_rules_to_map()
    rule_creator.create_rule_maps(rule_selector)

  def _choose_rules_to_map(self):
    rule_selector = ChooseRuleMapsToCreate(factory=self.factory, files_and_dirs=self.files)
    return rule_selector.get_list_of_rule_maps_to_create()
