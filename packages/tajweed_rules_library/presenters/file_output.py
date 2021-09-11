import os, json

class FileOutput():

	def __init__(self, root_dir, relative_dir):
		self
		self.root_dir = root_dir
		self.relative_dir = relative_dir
	
	def create_absolute_output_path(self, rule):
		relative_path = os.path.join(self.relative_dir, f'{rule}.json')
		absolute_path = os.path.join(self.root_dir, relative_path)
		return absolute_path

	def write_to_output_file(self, content, path):
		with open(path, "w") as outfile:
			json.dump(content, outfile)
			outfile.close()

ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
RELATIVE_DIR = 'entities\\output_files'

file_output = FileOutput(ROOT_DIR, RELATIVE_DIR)
