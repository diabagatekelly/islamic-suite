import os
import json
import shutil

class FileSystem():
  """File System Gateway

  Gateway to the local file system which allows getting files from
  lists of directories, getting files in nested directories, getting
  the last update of, reading from, and writing to files, create file
  paths, and copying files to other directories.

  Functions:
    *_get_nested_directories (private) - get the directories nested within a given directory
    
    *get_files_in_directory - get the files in a given directory
    *read_file_by_lines - read file line by by line
    *create_absolute_path - concatenates the root path, a directory path, and a rule name to create
    an absolute path for a new file json file 
    *write_json_to_file - save json content to a file
    *copy_file_from_original_to_target_dir - copy file to a new directory
    *empty_directory - delete all the content inside a directory
    *delete_directory - delete a directory and its content
  """

  def __init__(self):
    self

  def get_files_in_directory(self, directory):
    """Get the files in a given directory
      - parameters: directory absolute path
      - returns: array of file objects
      [{
        'name': filename.py,
        'absolute_path': 'C://path/to/file.py'
      }]
    """
    filenames = []
    subdir_paths = self._get_nested_directories(directory)

    if len(subdir_paths) != 0:
      # This block iterates over nested directories insise the entities directory.
      # These define how to create the maps for each tajweed rule (each entity).
      for path in subdir_paths:
        for subdir, dirs, files in os.walk(path):
          for filename in files:
            # Do not return info for __init__.py, tests, or factory files
            if filename.endswith('py') and not any(map(filename.__contains__, ['test', '__init__'])):
              file_stats = {
                'name': filename,
                'absolute_path': os.path.join(path, filename)
              }
              filenames.append(file_stats)
    else:
      # This block iterates over the flat output directories ('outputs' in local env or 'dist' in prod env).
      # These are our exisiting output JSON files.
      for subdir, dirs, files in os.walk(directory):
        for filename in files:
          file_stats = {
            'name': filename,
            'absolute_path': os.path.join(directory, filename)
          }
          filenames.append(file_stats)
    return filenames

  def _get_nested_directories(self, directory):
    """Get the directories nested within a given directory
      - parameters: directory absolute path
      - returns: array of file objects
      [{
        'name': filename.py,
        'absolute_path': 'C://path/to/file.py'
      }]
    """
    subdirectories_paths = []
    with os.scandir(directory) as subdirectory:
      for entry in subdirectory:
        if not entry.is_file() and entry.name != '__pycache__':
          subdirectories_paths.append(entry.path)
    return subdirectories_paths

  def read_file_by_lines(self, file):
    """Read file line by by line
      - parameters: file path
      - returns: array of strings, where each string is a file line
    """
    file_content = []
    file = open(file, 'r', encoding='utf-8')
    for line in file.readlines():
      file_content.append(line)
    file.close()
    return file_content

  def create_absolute_path(self, path, rule):
    """Concatenates the root path, a directory path, and a rule name
      to create an absolute path for a new JSON file
      - parameters: directory path, rule name
      - returns: JSON file absolute path as string
    """
    relative_path = os.path.join(path["outputs_dir"], f'{rule}.json')
    absolute_path = os.path.join(path["root"], relative_path)
    return absolute_path

  def write_json_to_file(self, content, path):
    """Write JSON to a file
      - parameters : JSON content, file path
    """
    with open(path, "w") as outfile:
      json.dump(content, outfile)
      outfile.close()
          
  def copy_file_from_original_to_target_dir(self, original, target):
    """Copy file to a new directory
      - parameters: original file path, destination file path
    """
    shutil.copyfile(original, target)

  def empty_directory(self, directory):
    """Delete all the files in a given directory
      - parameters: directory
    """
    for file in os.listdir(directory):
      os.remove(os.path.join(directory, file))

  def delete_directory(self, directory):
    """Delete a directory and its content
      - parameters: directory
    """
    shutil.rmtree(directory)