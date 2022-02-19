class FileToMapGateway():
  """File to JSON Map Gateway
  
  Extacts a rule name and a rule map from a file name.
  Those are then used to create a JSON map for the extacted rule.

  Functions:
    *get_name_from_file - splits file's name.extension to get the name
      - parameters: file name with extension
      - returns: file name as string
    *get_rule_class_from_name - splits file's name and concatenates
      the parts into a Pascal Case class name
			- parameters: rule name
			- returns: ClassName as a string
  """
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


