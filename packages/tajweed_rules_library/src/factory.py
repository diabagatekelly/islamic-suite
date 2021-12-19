from src.gateways.file_system import FileSystem
from src.gateways.file_to_map_gateway import FileToMapGateway

# In the future I might add a S3 file handler
class Factory():
  def __init__(self, env='local'):
    self
    self.env = env
    
  def get_file_system(self):
    if self.env in ['local', 'prod']:
      return FileSystem()
    elif self.env == 'online':
      return 'online file Urls'
   
  def get_file_to_map_gateway(self):
      return FileToMapGateway()

