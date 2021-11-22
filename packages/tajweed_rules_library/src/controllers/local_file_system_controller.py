import os
from src.factory import Factory
from src.use_cases.create_rules_maps import CreateRulesMaps

class LocalFileSystemController():

  def __init__(self):
    self
    self.factory = Factory('dev')
    self.set_up_mapper()

  def set_up_mapper(self):
    mapper = CreateRulesMaps(self.factory)
    mapper.create_rule_maps()
