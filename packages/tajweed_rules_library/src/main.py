import sys
import os
from src.controllers.prod_controller import ProdController
from src.controllers.local_controller import LocalController

class Main():
  """Tajweed Rules Library

  The Tajweed Rules Library takes a text file of Uthmani Quran
  and creates JSON maps of each rules's location in the Quran.

  The rules currently supported are:
    *Madd Rules
      *Madd al-Aarid/al-Leen: 2, 4, 6 harakat
      *Madd al-Muttasil: 4, 5 harakat
      *Madd al-Munfasil: 4, 5 harakat
      *Madd Laazim: 6 harakat
    *Meem Saakin Rules
      *Idghaam Shafawi (Meem Saakin)
      *Ikhfa Shafawi (Meem Saakin)
      *Idhaar Shafawi (Meem Saakin)
    *Noon Saakin Rules
      *Idghaam w/ Ghunnah (Noon Saakin)
      *Idghaam w/ No Ghunnah (Noon Saakin)
      *Ikhfa (Noon Saakin)
      *Idhaar (Noon Saakin)
      *Iqlab
    *Miscellaneous
      *Ghunnah
      *Qalqalah
      *Idghaam Mutajaanisayn
      *Idghaam Mutaqaaribayn

  Each rule's location information contains:
    *The surah
    *The ayah
    *The rule's beginning and ending index

  This is the entry point to build each tajweed rule's JSON map.
  The script to run the app from the tajweed_library_rules module is:
    DEV - python -m src.main run_app local
    PROD - python -m src.main run_app prod

  Running the app in the dev environment saves all JSON maps to the local
  file directory. Running the app in the prod environment saves all JSON maps
  to a S3 bucket.

  Functions:
    *run_app - accepts the environment (dev or prod) as a parameter and runs the app
    *build_dev - initializes Local Controller
    *build_prod - initializes Prod Controller
    *clean_up_pycache - removes pycache from project
  """

  def run_app(self, env):
    """Use in python script to build Tajweed rules's JSON maps.

    Parameters:
    env (str): 'local' or 'prod'
    """
    if env == 'local':
      self.build_dev()
    elif env == 'prod':
      self.build_prod()
    else:
      print('Oops! Something went wrong. Make sure to pass "local" or "prod" as an argument.')

    self.clean_up_pycache()
    print('All done! Check src.outputs or src.dist to see your new maps.')

  def build_dev(self):
    """Runs app locally, saves maps to local file system."""
    print('Building maps locally. This might take a few minutes...')
    local_controller = LocalController(env='local')
    local_controller.create_rule_maps()

  def build_prod(self):
    """Runs app for production, saves maps to S3 bucket."""
    print('running prod')
    self.build_dev()
    prod_controller = ProdController(env='prod')
    prod_controller.create_rule_maps()

  def clean_up_pycache(self):
    """Removes pycache directories."""
    os.popen('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')

if __name__ == "__main__":
  main = Main()
  main.run_app(sys.argv[2])