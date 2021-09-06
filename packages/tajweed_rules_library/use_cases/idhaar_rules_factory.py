from use_cases.single_rule_files import SingleRuleFiles

class IdhaarRulesFactory(SingleRuleFiles):
  def __init__(self, rule, input_file, root_dir, relative_dir):
    self
    self.rule = rule
    self.input_file = input_file
    self.root_dir = root_dir
    self.relative_dir = relative_dir
    self.generate_idhaar_file()


  def generate_idhaar_file(self):
    if self.rule == 'idhaar':
      return self.generate_idhaar_rule_file()
    elif self.rule == 'idhaar_shafawi':
      return self.generate_idhaar_shafawi_rule_file()


  def generate_idhaar_rule_file(self):
    content_for_rule = {}
    idhaar_locations = []

    quran = open(self.input_file, 'r', encoding='utf-8')
    
    for line in quran:
      parsed_line = self.parse_quran_script(line)
      surah = parsed_line['surah']
      ayah = parsed_line['ayah']
      text = parsed_line['text']

      noon_saakin_indices = self.find_all_letter_indices('ن', 'صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ')
      # kasra_dummah_tanween_indices = self.find_all_tanween_indices('ٌٍ' , 'صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ')
      # fatha_tanween_indices = self.find_all_tanween_indices('ً' , 'صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ')

      noon_idhaar = self.extract_letter_rule_data('idhaar', noon_saakin_indices, 'صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ', surah, ayah)
      if noon_idhaar:
        idhaar_locations.append(noon_idhaar)

      # kasra_dummah_tanween_idhaar = self.extract_tanween_idhaar_rule_data('kasra', kasra_dummah_tanween_indices, 'صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ', surah, ayah)
      # if kasra_dummah_tanween_idhaar:
      #   idhaar_locations.append(kasra_dummah_tanween_idhaar)

      # fatha_tanween_idhaar = self.extract_tanween_idhaar_rule_data('fatha', fatha_tanween_indices, 'صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ', surah, ayah)
      # if fatha_tanween_idhaar:
      #   idhaar_locations.append(fatha_tanween_idhaar)
    quran.close()
    
    content_for_rule["idhaar"] = idhaar_locations 
    output_file = self.create_absolute_output_path('idhaar')
    self.write_to_output_file(content_for_rule, output_file)


  # def generate_idhaar_shafawi_rule_file(self):
  #   content_for_rule = {}
  #   idhaar_shafawi_locations = []

  #   quran = open(self.input_file, 'r', encoding='utf-8')
  #   for line in quran:
  #     parsed_line = self.parse_quran_script(line)
  #     surah = parsed_line['surah']
  #     ayah = parsed_line['ayah']
  #     text = parsed_line['text']

  #     meem_saakin_indices = self.find_all_letter_indices('م', text)

  #     idhaar_shafawi = self.extract_letter_rule_data('idhaar_shafawi', meem_saakin_indices, text, surah, ayah)
  #     if idhaar_shafawi:
  #       idhaar_shafawi_locations.append(idhaar_shafawi)

  #   quran.close()

  #   content_for_rule["idhaar_shafawi"] = idhaar_shafawi_locations 
  #   output_file = self.create_absolute_output_path('idhaar_shafawi')
  #   self.write_to_output_file(content_for_rule, output_file)


  def parse_quran_script(self, line):
    segments = line.split('|')
    surah = int(segments[0])
    ayah = int(segments[1])
    text = segments[2].strip()

    parsed_line = {
      'surah': surah,
      'ayah': ayah,
      'text': text
    }

    return  parsed_line

      
  def find_all_letter_indices(self, sign, text):
    print(sign)
    letter_indices = [letter_index for letter_index, letter in enumerate(text) if letter == sign and letter_index < len(text)-1 and text[letter_index+1] == "ْ"]
    print(letter_indices)
    return letter_indices


  # def find_all_tanween_indices(self, sign, text):
  #   tanween_indices = [tanween_index for tanween_index, letter in enumerate(text) if letter in sign and tanween_index < len(text)-1]
  #   return tanween_indices
  

  def extract_letter_rule_data(self, rule, indices, text, surah, ayah):
    rule_info = {}

    if len(indices) == 0:
      return

    for i in indices:
      print(i)

      if i + 2 < len(text)-1 and text[i+2] == " ":
        i = i + 3
        rule_info = self.save_index_for_letter_in_target(rule, text, i, 3, surah, ayah)
      elif i +2 < len(text)-1 and text[i+2] != " ":
        i = i + 2
        rule_info = self.save_index_for_letter_in_target(rule, text, i, 2, surah, ayah)

    return rule_info


  def extract_tanween_idhaar_rule_data(self, tanween_type, tanween_indices, text, surah, ayah):
    ayah_idhaar_info = {}

    if len(tanween_indices) > 0:
      index = int(tanween_indices[0])
      base = index -1       

      if tanween_type != 'fatha':
        ayah_idhaar_info = self.save_index_for_tanween_in_target(index, text, 2, surah, ayah, base)
      elif tanween_type == 'fatha':
        ayah_idhaar_info = self.save_index_for_tanween_in_target(index, text, 3, surah, ayah, base)
        
    return ayah_idhaar_info
  

  def save_index_for_tanween_in_target(self, index, text, adjustment, surah, ayah, base):
    if index + adjustment < len(text)-1 and text[index+2] in 'هءأإحعخغ':
      return self.construct_rule_instance_location_map(surah, ayah, base, index + adjustment)


  def save_index_for_letter_in_target(self, rule, text, index, adjustment, surah, ayah):
    print(text[index-adjustment])
    if rule == 'idhaar' and text[index] in 'هءأإحعخغ':
      return self.construct_rule_instance_location_map(surah, ayah, index - adjustment, index)
    elif rule != 'idhaar' and text[index] not in 'مب':
      return self.construct_rule_instance_location_map(surah, ayah, index - adjustment, index)