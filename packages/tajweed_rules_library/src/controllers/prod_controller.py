import os
from src.factory import Factory
from src.use_cases.create_rules_maps import CreateRulesMaps
from src.use_cases.choose_rule_maps_to_create import ChooseRuleMapsToCreate

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
LOCAL_OUTPUTS = os.path.join(ROOT, 'outputs')
PROD_OUTPUTS = os.path.join(ROOT, 'dist')

FILES_SYS = {
	'root': ROOT,
	'local_outputs': LOCAL_OUTPUTS,
	'outputs_dir': PROD_OUTPUTS
}
    
class ProdController():
  """Prod (Production) Controller
  
  Instantiates CreateRulesMaps class (the package's primary use case)
  in a prod environment, which means all outputed JSON maps are saved to
  a S3 bucket by CI/CD pipeline.

  Parameters:
    *env - defaults to prod
    *files - builds a dist output directory from a local outputs directory
      *root: the root directory 
      *local_outputs: the local outputs directory
      *outputs_dir: the dist outpus directory
  
  Constructor:
    *files parameter
    *Factory: instantiated with the prod parameter 

  Functions:
    *choose_rules_to_map (private) - choose rules to map
    *create_rule_maps - create JSON maps or chosen rules
  """
  def __init__(self, env='prod', files=FILES_SYS):
    self
    self.factory = Factory(env)
    self.files = files

  def create_rule_maps(self):
    """Create JSON maps for chosen rules.
    Instantiates CreateRulesMaps with local factory and files.
    """
    rule_creator = CreateRulesMaps(self.factory, files_and_dirs=self.files)
    rule_selector = self._choose_rules_to_map()
    rule_creator.create_rule_maps(rule_selector)

  def _choose_rules_to_map(self):
    """Choose the JSON maps that need to be copied to the dist folder,
    based on whether they don't already exist, or if there have been
    recent changes to the local outputes JSON maps.
    Instantiates ChooseRuleMapsToCreate with prod factory and files.
    """
    rule_selector = ChooseRuleMapsToCreate(
      factory=self.factory, files_and_dirs=self.files
    )
    return rule_selector.get_list_of_rule_maps_to_create()