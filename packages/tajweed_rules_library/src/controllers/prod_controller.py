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
    *_get_local_maps_to_copy (private) - get the details of the local JSON maps that need to be copied
    *create_rule_maps - create JSON maps or chosen rules
  """
  def __init__(self, env='prod', files=FILES_SYS):
    self
    self.factory = Factory(env)
    self.files = files

  def create_rule_maps(self):
    """Create JSON maps for chosen rules.
      Instantiates CreateRulesMaps with prod factory and files.
    """
    rule_creator = CreateRulesMaps(self.factory, files_and_dirs=self.files)
    rules_to_copy = self._get_local_maps_to_copy()
    rule_creator.create_rule_maps(rules_to_copy)

  def _get_local_maps_to_copy(self):
    """Get the details of the local JSON maps that need to be copied 
      to the dist folder.
      Instantiates ChooseRuleMapsToCreate with prod factory and files.
    """
    rules_to_copy = ChooseRuleMapsToCreate(factory=self.factory, files_and_dirs=self.files)
    return rules_to_copy.get_list_of_json_maps_to_create()