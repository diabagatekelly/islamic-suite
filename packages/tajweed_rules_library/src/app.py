import sys
from src.controllers.prod_controller import ProdController
from src.controllers.local_controller import LocalController

def run_app(env):
  if env == 'local':
    build_dev()
  elif env == 'prod':
    build_prod()

def build_dev():
  print(f'build local')
  local_controller = LocalController(env='local')
  local_controller.create_rule_maps()

def build_prod():
  print(f'build prod')
  build_dev()
  prod_controller = ProdController(env='prod')
  prod_controller.create_rule_maps()

run_app(sys.argv[2])

#pseudo build_prod()
#  s3 FILESYSTEM which will run logic to see which files to create 
#Before: cd packages/tajweed_rules_library/ && source venv/Scripts/activate
#Build:single:  sh python -m src.app run_app prod ''
#Build:all: sh python -m src.app run_app prod sys.argv[3]
#Test: sh python -m unittest -v
#Coverage: sh coverage run -m unittest && coverage report --omit=*factory.py,*app.py,*test_*.py,src/*__init__.py,src/*/__init__.py


# Local file system provides functions to write, read, create paths for a local system of file; if my filea were URLS, I might create a online file system to deal with file from links, etc...
# File to map gateway parses file name (string) into a relevant rule and class; it doesn't care where that string came from, or what its content is? Maybe it shouldn't be responsible for choosing what rule map need to be created
# Use cases are now 2 - determine which rule maps need to be created/// create said rule maps
# My local file controller would take all the files needed (input entities and output dirs) and the factory which has all the other things i need