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

class LocalFileSystem():
	def __init__(self, files_sys=FILES_SYS):
		self
		self.root = files_sys['root']
		self.input_file = files_sys['input_file']
		self.entities_dir = files_sys['entities_dir']
		self.outputs_dir = files_sys['outputs_dir']
	
	def get_files_in_dir(self):
		filenames = []
		for subdir, dirs, files in os.walk(self.entities_dir):
			for filename in files:
				if filename.endswith('py'):
					filenames = filenames + files
		filenames.remove('__init__.py')
		print(filenames)
		return filenames


	def read_entire_file_content(self):
		file_content = []
		with open(self.input_file) as input_file:
			entire_file = json.load(input_file)
			file_content.append(entire_file)
			input_file.close()
		return file_content

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



	# def save_file_content(self):
	# 	all_rules = {}
	# 	all_rules['data'] = []
	# 	with open(self.input_file) as input_file:
	# 		file_content = json.load(input_file)
	# 		all_rules["data"].append(file_content)
	# 		input_file.close()
	# 	return all_rules

	# def read_quran_file(self):
	# 	quran = []
	# 	quran_file = open(self.input_file, 'r', encoding='utf-8')
	# 	for line in quran_file.readlines():
	# 		quran.append(line)
	# 	quran_file.close()
	# 	return quran

# IDHAAR_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\quran-uthmani.txt'
# idhaar_file_input = FileInput(IDHAAR_RULES_INPUT_FILE)

# OTHER_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\tajweed_hafs_uthmani_pause_sajdah.json'
# others_file_input = FileInput(OTHER_RULES_INPUT_FILE)

# class FileOutput():

	# def __init__(self, root_dir, relative_dir):
	# 	self
	# 	self.root_dir = root_dir
	# 	self.relative_dir = relative_dir
	
	# def create_absolute_output_path(self, rule):
	# 	relative_path = os.path.join(self.relative_dir, f'{rule}.json')
	# 	absolute_path = os.path.join(self.root_dir, relative_path)
	# 	return absolute_path

	# def write_to_output_file(self, content, path):
	# 	with open(path, "w") as outfile:
	# 		json.dump(content, outfile)
	# 		outfile.close()

# ROOT_DIR = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library'
# RELATIVE_DIR = 'entities\\output_files'

# file_output = FileOutput(ROOT_DIR, RELATIVE_DIR)




