class FileToMapGateway():
  
  def __init__(self):
    self

  def get_name_from_file(self, file_name):
    return file_name.split('.')[0]
  
  def get_rule_class_from_name(self, rule_name):
    split_name = rule_name.split('_')
    class_name = ''
    for part in split_name:
      capitalized_name = part.capitalize()
      class_name = class_name + capitalized_name
    return class_name


