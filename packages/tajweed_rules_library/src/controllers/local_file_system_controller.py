from src.factory import Factory
from src.use_cases.create_rules_maps import CreateRulesMaps

class LocalFileSystemController():

  def __init__(self, env='', file_system={}, entity=''):
    self
    self.env = env
    self.file_system = file_system
    self.entity = entity
    self.factory = Factory(env=self.env, file_system=self.file_system, entity=self.entity)
    self.set_up_mapper()

  def set_up_mapper(self):
    mapper = CreateRulesMaps(self.factory)
    mapper.create_rule_maps()