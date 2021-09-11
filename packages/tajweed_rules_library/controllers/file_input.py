import json

class FileInput():

	def __init__(self, input_file):
		self
		self.input_file = input_file

	def save_file_content(self):
		all_rules = {}
		all_rules['data'] = []
		with open(self.input_file) as input_file:
			file_content = json.load(input_file)
			all_rules["data"].append(file_content)
			input_file.close()
		return all_rules

	def open_quran_file(self):
		quran = open(self.input_file, 'r', encoding='utf-8')
		return quran
		
	def parse_quran_script(self, line):
		segments = line.split('|')
		surah_number = int(segments[0])
		ayah_number = int(segments[1])
		ayah_text = segments[2].strip()

		parsed_line = {
			'surah_number': surah_number,
			'ayah_number': ayah_number,
			'ayah_text': ayah_text
		}

		return parsed_line

IDHAAR_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\quran-uthmani.txt'
idhaar_file_input = FileInput(IDHAAR_RULES_INPUT_FILE)

OTHER_RULES_INPUT_FILE = 'C:\\Users\\kelly\\Documents\\Development Related\\Portfolio Projects\\islamic ed suite (angular + python + sql)\\tajweed-monorepo\\packages\\tajweed_rules_library\\entities\\input_fixtures\\tajweed_hafs_uthmani_pause_sajdah.json'
others_file_input = FileInput(OTHER_RULES_INPUT_FILE)
