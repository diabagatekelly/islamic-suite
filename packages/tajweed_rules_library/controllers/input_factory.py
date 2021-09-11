from controllers.file_input import idhaar_file_input, others_file_input, FileInput

class InputFactory():
  def __init__(self, input):
    self
    self.input = input

  def get_input(self):
    if self.input == 'idhaar_file':
      return idhaar_file_input
    elif self.input == 'others_file':
      return others_file_input
    else:
      return FileInput
    # elif self.input == 'idhaar_s3':