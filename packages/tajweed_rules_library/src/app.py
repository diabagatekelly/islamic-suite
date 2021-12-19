import sys
from src.controllers.local_file_system_controller import LocalFileSystemController

def build_dev():
  print(f'running in local')
  local_controller = LocalFileSystemController(env='local')
  local_controller.create_rule_maps()

build_dev()

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