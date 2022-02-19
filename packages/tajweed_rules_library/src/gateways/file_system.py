import os, json, shutil

class FileSystem():
	"""File System Gateway
  
  Gateway to the local file system which allows getting files from
	lists of directories, getting files in nested directories, getting
	the last update of, reading from, and writing to files, create file
	paths, and copying files to other directories. 

  Functions:
    *get_files_in_directory - get the files in a given directory
				- parameters: directory
				- returns: array of file names
    *_get_nested_directories (private) - get the directories nested within a given directory
				- parameters: directory
				- returns: array of objects with a file's name and absolute path
		*get_file_last_update_date - get last update date for a file
				- parameters: file path
				- returns: float
		*read_file_by_lines - read file line by by line
				- parameters: file path
				- returns: array of strings, where each string is a file line
		*create_absolute_path - concatenates the root path, a directory path, and a rule name to create 
			an absolute path for a new file json file
				- parameters: directory path, rule
				- returns: JSON file absolute path as string
		*write_to_file - save content to a file
				- parameters : file path, content
		*copy_file_from_original_to_target_dir - copy file to a new directory
				- parameters: original file path, destination file path
  """
	def __init__(self):
		self

	def get_files_in_directory(self, directory):
		"""Get the files in a given directory
			- parameters: directory path
			- returns: array of file names
    """
		filenames = []
		subdir_paths = self._get_nested_directories(directory)

		if len(subdir_paths) != 0:
			for path in subdir_paths:
				for subdir, dirs, files in os.walk(path):
					for filename in files:
						if filename.endswith('py'):
							file_stats = {
								'name': filename,
								'absolute_path': os.path.join(path, filename)
							}
							filenames.append(file_stats)
		else:
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
			- parameters: directory path
			- returns: array of objects with a file's name and absolute path
		"""
		subdirectories_paths = []
		with os.scandir(directory) as subdirectory:
			for entry in subdirectory:
				if not entry.is_file() and entry.name != '__pycache__':
					subdirectories_paths.append(entry.path)
		return subdirectories_paths

	def get_file_last_update_date(self, file_path):
		"""Get last update date for a file
			- parameters: file path
			- returns: date as float
		"""
		return os.stat(file_path).st_mtime

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

	def write_to_file(self, content, path):
		"""Write to a file
			- parameters : file path, content
		"""
		with open(path, "w") as outfile:
			json.dump(content, outfile)
			outfile.close()

	def copy_file_from_original_to_target_dir(self, original, target):
		"""Copy file to a new directory
			- parameters: original file path, destination file path
		"""
		shutil.copyfile(original, target)
