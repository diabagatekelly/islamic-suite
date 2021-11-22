import os

from src.gateways.local_file_system import LocalFileSystem
from src.gateways.file_to_map_gateway import FileToMapGateway

# In the future I might add a S3 file handler
class Factory():
  def __init__(self, env=''):
    self
    self.env = env

  def get_input_system(self):
    if self.env == 'dev':
      return LocalFileSystem
    elif self.env == 'S3':
      return 'S3'

  def get_input_to_map_gateway(self):
    if self.env == 'dev':
      return FileToMapGateway
    elif self.env == 'S3':
      return 'S3'