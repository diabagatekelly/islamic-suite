from presenters.file_output import file_output, FileOutput

class OutputFactory():
  def __init__(self, output):
    self
    self.output = output

  def get_output(self):
    if self.output == 'file':
      return file_output
    else:
      return FileOutput
    # elif self.output == 's3'