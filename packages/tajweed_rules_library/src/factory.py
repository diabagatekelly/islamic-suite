from src.gateways.file_system import FileSystem
from src.gateways.file_to_map_gateway import FileToMapGateway

class Factory():
  """Factory for selecting:
    *Local file system or online file system gateway (perhaps in the future)
    *File system to JSON map translator gateway
  
  Constructor:
    *env - defaults to local
 
  Returns:
    *FileSystem class
    *FileToMapGateway class

  Functions:
    *get_file_system - returns FileSystem class
    *get_file_to_map_gateway - returns FileToMapGateway class
  """
  def __init__(self, env='local'):
    self
    self.env = env
    
  def get_file_system(self):
    """Returns FileSystem class or online file system."""
    if self.env in ['local', 'prod']:
      return FileSystem()
    elif self.env == 'online':
      return 'online file Urls'
   
  def get_file_to_map_gateway(self):
    """Returns FileToMapGateway class."""
    return FileToMapGateway()

