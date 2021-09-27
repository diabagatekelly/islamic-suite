from presenters.file_output import file_output, FileOutput

# In the future I might save file to a S3
class OutputFactory():
  def __init__(self, output=''):
    self
    self.output = output

  def get_output(self):
    if self.output == 'file':
      return file_output
    else:
      return FileOutput