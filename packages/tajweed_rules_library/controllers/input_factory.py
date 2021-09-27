from controllers.file_input import idhaar_file_input, others_file_input, FileInput

# In the future I might add a S3 file handler
class InputFactory():
  def __init__(self, input_type=''):
    self
    self.input = input_type

  def get_input(self):
    if self.input == 'idhaar_file':
      return idhaar_file_input
    elif self.input == 'others_file':
      return others_file_input
    else:
      return FileInput