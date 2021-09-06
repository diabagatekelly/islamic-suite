from use_cases.single_rule_files import SingleRuleFiles

class Idhaar(SingleRuleFiles):
  def __init__(self, input_file, relative_dir):
    self
    self.input_file = input_file
    self.relative_dir = relative_dir

  def generate_idhaar_rule_file(self):
    content_for_rule = {}
    idhaar_locations = []

    quran = open(self.input_file, 'r', encoding='utf-8')
    
    for line in quran:
      parsed_line = self.parse_quran_script(line)
      surah_number = parsed_line['surah_number']
      ayah_number = parsed_line['ayah_number']
      ayah_text = parsed_line['ayah_text']

      noon_saakin_indices = self.find_letter_in_text('ن', ayah_text)
      noon_idhaar_locations = self.get_all_rule_locations_for_letter_base(noon_saakin_indices, ayah_text, surah_number, ayah_number)
      idhaar_locations + noon_idhaar_locations

      kasra_dummah_tanween_indices = self.find_tanween_in_text('ٌٍ' , ayah_text)
      kasra_dummah_tanween_idhaar_locations = self.get_all_rule_locations_for_tanween_base('kasra', kasra_dummah_tanween_indices, ayah_text, surah_number, ayah_number)
      idhaar_locations + kasra_dummah_tanween_idhaar_locations

      fatha_tanween_indices = self.find_tanween_in_text('ً' , ayah_text)
      fatha_tanween_idhaar_locations = self.get_all_rule_locations_for_tanween_base('fatha', fatha_tanween_indices, ayah_text, surah_number, ayah_number)
      idhaar_locations + fatha_tanween_idhaar_locations

    quran.close()
    
    content_for_rule["idhaar"] = idhaar_locations 
    output_file = self.create_absolute_output_path('idhaar')
    self.write_to_output_file(content_for_rule, output_file)

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

    return  parsed_line

  def find_letter_in_text(self, target_letter, ayah_text):
    letter_indices = [letter_index for letter_index, letter in enumerate(ayah_text) if letter == target_letter and letter_index < len(ayah_text)-1 and ayah_text[letter_index+1] == "ْ"]
    return letter_indices
  
  def find_tanween_in_text(self, target_letter, ayah_text):
    tanween_indices = [tanween_index for tanween_index, letter in enumerate(ayah_text) if letter in target_letter and tanween_index < len(ayah_text)-1]
    return tanween_indices

  def get_all_rule_locations_for_letter_base(self, base, ayah_text, surah_number, ayah_number):
    if len(type) == 0:
      return

    noon_rules = []

    for index in base:
      noon_idhaar = self.get_rule_location_details(index, ayah_text, surah_number, ayah_number)
      if noon_idhaar:
        noon_rules.append(noon_idhaar)

    return noon_rules


  def get_all_rule_locations_for_tanween_base(self, tanween_type, base, ayah_text, surah_number, ayah_number):
    if len(type) == 0:
      return

    tanween_rules = []

    for index in base:
      tanween_idhaar = self.get_rule_location_details_for_tanween_base(tanween_type, index, ayah_text, surah_number, ayah_number)
      if tanween_idhaar:
        tanween_rules.append(tanween_idhaar)

    return tanween_rules


  def get_rule_location_details_for_letter_base(self, index, ayah_text, surah_number, ayah_number):
    rule_info = {}

    rule_start_index = index

    if not self.is_letter_at_index_still_inside_ayah(rule_start_index, ayah_text):
      return

    
    if self.is_letter_at_index_followed_by_space(rule_start_index, ayah_text):
      rule_end_index = self.get_rule_end_index(rule_start_index, 3)
      if self.is_letter_after_noon_idhaar_letter(rule_end_index, ayah_text):
        rule_info = self.construct_rule_location_map(surah_number, ayah_number, index, rule_end_index)
    elif not self.is_letter_at_index_followed_by_space(index, ayah_text):
      rule_end_index = self.get_rule_end_index(rule_start_index, 2)
      if self.is_letter_after_noon_idhaar_letter(rule_end_index, ayah_text):
        rule_info = self.construct_rule_location_map(surah_number, ayah_number, index, rule_end_index)

    return rule_info


  def get_rule_location_details_for_tanween_base(self, tanween_type, index, ayah_text, surah_number, ayah_number):
    ayah_idhaar_info = {}

    rule_start_index = index -1       

    if tanween_type != 'fatha':
      rule_end_index = self.get_rule_end_index(rule_start_index, 2)
      if self.is_tanween_at_index_still_inside_ayah(rule_end_index, ayah_text) and self.is_letter_after_tanween_idhaar_letter(rule_end_index, ayah_text):
        ayah_idhaar_info = self.construct_rule_instance_location_map(surah_number, ayah_number, rule_start_index, rule_end_index)
    elif tanween_type == 'fatha':
      rule_end_index = self.get_rule_end_index(rule_start_index, 3)
      ayah_idhaar_info = self.construct_rule_instance_location_map(surah_number, ayah_number, rule_start_index, rule_end_index)
        
    return ayah_idhaar_info
 

  def is_letter_at_index_followed_by_space(self, index, ayah_text):
    if ayah_text[index+2] == " ":
      return True

  def is_letter_at_index_still_inside_ayah(self, index, ayah_text):
    if index + 2 < len(ayah_text)-1:
      return True

  def is_letter_after_noon_idhaar_letter(self, index, ayah_text):
    if ayah_text[index] in 'هءأإحعخغ':
      return True

  def is_letter_after_tanween_idhaar_letter(self, rule_end_index, ayah_text):
    if  ayah_text[rule_end_index] in 'هءأإحعخغ':
      return True

  def is_tanween_at_index_still_inside_ayah(self, rule_end_index, ayah_text):
    if rule_end_index < len(ayah_text)-1:
      return True

  def get_rule_end_index(self, start_index, move_by_spaces):
    return start_index + move_by_spaces
