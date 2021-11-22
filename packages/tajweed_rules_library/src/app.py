import sys
from src.controllers.local_file_system_controller import LocalFileSystemController

def run_app(env):
  if env == 'dev':
    print(f'running in {env}')
    return LocalFileSystemController()
  elif env == 'prod':
    print('S3 coming soon')
    return

run_app(sys.argv[2])
