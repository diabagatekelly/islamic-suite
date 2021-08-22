from use_cases.single_rule_files import SingleRuleFiles
from use_cases.idhaar_rules_factory import IdhaarRulesFactory

class IdhaarRuleFiles(SingleRuleFiles):
  def __init__(self, factory):
    self
    self.factory = factory
    self.generate_all_idhaar_files()


  def generate_all_idhaar_files(self):
    self.generate_idhaar_file()
    self.generate_idhaar_shafawi_file()


  def generate_idhaar_file(self):
    return self.factory


  def generate_idhaar_shafawi_file(self):
    return self.factory
    
      

    









    

 
    

        





