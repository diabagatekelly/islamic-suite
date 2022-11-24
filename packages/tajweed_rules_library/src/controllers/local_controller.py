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
  """Local (Dev) Controller

    Instantiates CreateRulesMaps class (the package's primary use case)
    in a dev environment, which means all outputed JSON maps are saved to
    the local file system.

    Parameters:
      *env - defaults to local
      *files - defaults to local file directories
      *root: the root directory
      *input_file: the directoy where the Uthmani Quran text file used to create each rule's map is saved
      *entities_dir: the directory where the classes for mapping each tajweed rule are saved
      *outputs_dir: the directory where outputed JSON maps are saved

    Constructor:
      *files parameter
      *Factory: instantiated with the env parameter

    Functions:
      *_get_list_of_rules_to_map (private) - get the list of rules to map
      *create_rule_maps - create JSON maps for the specified rules
  """
  def __init__(self, env='local', files=FILES_SYS):
    self
    self.factory = Factory(env)
    self.files = files

  def create_rule_maps(self):
    """Create JSON maps for specified rules.
      Instantiates CreateRulesMaps with local factory and files.
    """
    rule_creator = CreateRulesMaps(self.factory, files_and_dirs=self.files)
    rules_to_map = self._get_list_of_rules_to_map()
    rule_creator.create_rule_maps(rules_to_map)

  def _get_list_of_rules_to_map(self):
    """Choose the tajweed rules that need to be mapped,
      based on which tajweed rule class has recent changes.
      Instantiates ChooseRuleMapsToCreate with local factory and files.
    """
    rules_to_map = ChooseRuleMapsToCreate(factory=self.factory, files_and_dirs=self.files)
    return rules_to_map.get_list_of_json_maps_to_create()