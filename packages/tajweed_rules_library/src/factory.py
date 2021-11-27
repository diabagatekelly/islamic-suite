from src.gateways.local_file_system import LocalFileSystem
from src.gateways.file_to_map_gateway import FileToMapGateway

# In the future I might add a S3 file handler
class Factory():
  def __init__(self, env='', file_system={}, entity=''):
    self
    self.env = env
    self.file_system = file_system
    self.entity = entity

  def get_input_system(self):
    if self.env == 'dev':
      return LocalFileSystem(entity=self.entity)
    elif self.env == 'prod':
      return 'prod'
    else:
      return LocalFileSystem(files_sys=self.file_system, entity=self.entity)

  def get_input_to_map_gateway(self):
    if self.env == 'dev':
      return FileToMapGateway(LocalFileSystem(entity=self.entity))
    elif self.env == 'prod':
      return 'prod'
    else:
      return FileToMapGateway(LocalFileSystem(files_sys=self.file_system, entity=self.entity))
