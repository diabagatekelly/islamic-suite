import sys
from src.controllers.local_file_system_controller import LocalFileSystemController

def run_app(env='dev', entity=''):
  if env == 'dev':
    print(f'running in {env}')
    return LocalFileSystemController(env='dev', entity=entity)
  elif env == 'prod':
    print('S3 coming soon')
    return

run_app(env=sys.argv[2], entity=sys.argv[3])

#Before: cd packages/tajweed_rules_library/ && source venv/Scripts/activate
#Build:single:  sh python -m src.app run_app prod ''
#Build:all: sh python -m src.app run_app prod sys.argv[3]
#Test: sh python -m unittest -v
#Coverage: sh coverage run -m unittest && coverage report --omit=*factory.py,*app.py,*test_*.py,src/*__init__.py,src/*/__init__.py
