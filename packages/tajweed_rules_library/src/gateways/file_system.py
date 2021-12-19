import os, json, shutil

class FileSystem():
	def __init__(self):
		self

	def get_files_in_directory(self, directory):
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
		subdirectories_paths = []
		with os.scandir(directory) as subdirectory:
			for entry in subdirectory:
				if not entry.is_file() and entry.name != '__pycache__':
					subdirectories_paths.append(entry.path)
		return subdirectories_paths

	def get_file_last_update_date(self, file_path):
		return os.stat(file_path).st_mtime

	def read_file_by_lines(self, file):
		file_content = []
		file = open(file, 'r', encoding='utf-8')
		for line in file.readlines():
			file_content.append(line)
		file.close()
		return file_content

	def create_absolute_path(self, path, rule):
		relative_path = os.path.join(path["outputs_dir"], f'{rule}.json')
		absolute_path = os.path.join(path["root"], relative_path)
		return absolute_path

	def write_to_file(self, content, path):
		with open(path, "w") as outfile:
			json.dump(content, outfile)
			outfile.close()

	def copy_file_from_original_to_target_dir(self, original, target):
		shutil.copyfile(original, target)
