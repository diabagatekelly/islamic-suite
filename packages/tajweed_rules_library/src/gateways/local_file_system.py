import os, json

ROOT = os.path.abspath(os.path.join(os.getcwd(), 'src'))
INPUT_FILE = os.path.join(ROOT, 'fixtures/input_fixtures/quran-uthmani.txt')
ENTITIES_DIR = os.path.join(ROOT, 'entities')
OUTPUTS_DIR = os.path.join(ROOT, 'outputs')

FILES_SYS = {
	'root': ROOT,
	'input_file': INPUT_FILE,
	'entities_dir': ENTITIES_DIR,
	'outputs_dir': OUTPUTS_DIR
}

#Note: entity should be a file name without extenstion ie. madd_6, qalqalah

class LocalFileSystem():
	def __init__(self, files_sys=FILES_SYS, entity=''):
		self
		self.root = files_sys['root']
		self.input_file = files_sys['input_file']
		self.entities_dir = files_sys['entities_dir']
		self.outputs_dir = files_sys['outputs_dir']
		self.entity = entity
	
	def get_files_in_dir(self):
		filenames = []
		if self.entity != '':
			filenames.append(f'{self.entity}.py')
		else:
			for subdir, dirs, files in os.walk(self.entities_dir):
				print(dirs)
				for filename in files:
					if filename.endswith('py'):
						filenames = filenames + files
		filenames = self._clean_up_list(filenames)
		return filenames

	def _clean_up_list(self, files_list):
		filtered_list = [e for e in files_list if e not in ('__init__.py', 'entities_map.py')]
		final_list = list(set(filtered_list))
		return final_list

	# def read_entire_file_content(self):
	# 	file_content = []
	# 	with open(self.input_file) as input_file:
	# 		entire_file = json.load(input_file)
	# 		file_content.append(entire_file)
	# 		input_file.close()
	# 	return file_content

	def read_file_by_lines(self):
		file_content = []
		file = open(self.input_file, 'r', encoding='utf-8')
		for line in file.readlines():
			file_content.append(line)
		file.close()
		return file_content

	def create_absolute_output_path(self, rule):
		relative_path = os.path.join(self.outputs_dir, f'{rule}.json')
		absolute_path = os.path.join(self.root, relative_path)
		return absolute_path

	def write_to_file(self, content, path):
		with open(path, "w") as outfile:
			json.dump(content, outfile)
			outfile.close()



