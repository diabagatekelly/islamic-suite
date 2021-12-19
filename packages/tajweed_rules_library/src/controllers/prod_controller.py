import os

from src.factory import Factory
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.use_cases.choose_rule_maps_to_create import ChooseRuleMapsToCreate

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = ''
LOCAL_OUTPUTS = os.path.join(ROOT, 'outputs')
PROD_OUTPUTS = os.path.join(ROOT, 'dist')

FILES_SYS = {
	'root': ROOT,
	'local_outputs': LOCAL_OUTPUTS,
	'outputs_dir': PROD_OUTPUTS
}
    
class ProdController():
  def __init__(self, env='prod', files=FILES_SYS):
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