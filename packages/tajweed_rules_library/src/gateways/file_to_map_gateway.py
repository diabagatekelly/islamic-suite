class FileToMapGateway():
  def __init__(self, file_system):
    self
    self.file_system = file_system
  
  def get_rule_names(self):
    rule_names = self.file_system.get_files_in_dir()
    rule_names_no_extension = [name.split('.')[0] for name in rule_names]
    return rule_names_no_extension

  def get_rule_class_from_name(self, rule_name):
    split_name = rule_name.split('_')
    class_name = ''
    for part in split_name:
      capitalized_name = part.capitalize()
      class_name = class_name + capitalized_name
    return class_name


