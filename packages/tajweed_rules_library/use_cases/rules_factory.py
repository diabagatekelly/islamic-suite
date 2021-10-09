from use_cases.other_rules import other_rules
from use_cases.idhaar_rule import idhaar
from use_cases.idhaar_shafawi_rule import idhaar_shafawi

class RulesFactory():
  def __init__(self, rule=''):
    self
    self.rule = rule

  def get_tajweed_rule(self):
    if self.rule == 'others':
      return other_rules
    elif self.rule == 'idhaar':
      return idhaar
    elif self.rule == 'idhaar_shafawi':
      return idhaar_shafawi
