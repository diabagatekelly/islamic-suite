class Rule():
  def __init__(self, surah_number, ayah_number, ayah_text):
    self
    self.surah_number = surah_number
    self.ayah_number = ayah_number
    self.ayah_text = ayah_text

  def find_letter_in_text(self, target_letter):
    letter_indices = [letter_index for letter_index, letter in enumerate(self.ayah_text) if letter == target_letter and letter_index < len(self.ayah_text)-1 and self.ayah_text[letter_index+1] == "ْ"]
    return letter_indices
  
  def find_tanween_in_text(self, target_letter):
    tanween_indices = [tanween_index for tanween_index, letter in enumerate(self.ayah_text) if letter in target_letter and tanween_index < len(self.ayah_text)-1]
    return tanween_indices

  def get_all_rule_locations_for_letter_base(self, base):
    if len(base) == 0:
      return []

    noon_rules = []

    for index in base:
      noon_idhaar = self.get_rule_location_details_for_letter_base(index)
      if noon_idhaar:
        noon_rules.append(noon_idhaar)

    return noon_rules


  def get_all_rule_locations_for_tanween_base(self, tanween_type, base):
    if len(base) == 0:
      return []

    tanween_rules = []

    for index in base:
      tanween_idhaar = self.get_rule_location_details_for_tanween_base(tanween_type, index)
      if tanween_idhaar:
        tanween_rules.append(tanween_idhaar)

    return tanween_rules


  def get_rule_location_details_for_letter_base(self, index):
    rule_info = {}

    rule_start_index = index

    if not self.is_letter_at_index_still_inside_ayah(rule_start_index):
      return

    
    if self.is_letter_at_index_followed_by_space(rule_start_index):
      rule_end_index = self.get_rule_end_index(rule_start_index, 3)
      if self.is_letter_after_noon_idhaar_letter(rule_end_index):
        rule_info = self.construct_rule_location_map(self.surah_number, self.ayah_number, index, rule_end_index)
    elif not self.is_letter_at_index_followed_by_space(index):
      rule_end_index = self.get_rule_end_index(rule_start_index, 2)
      if self.is_letter_after_noon_idhaar_letter(rule_end_index):
        rule_info = self.construct_rule_location_map(self.surah_number, self.ayah_number, index, rule_end_index)

    return rule_info


  def get_rule_location_details_for_tanween_base(self, tanween_type, index):
    ayah_idhaar_info = {}

    rule_start_index = index -1       

    if tanween_type != 'fatha':
      rule_end_index = self.get_rule_end_index(rule_start_index, 2)
      if self.is_tanween_at_index_still_inside_ayah(rule_end_index) and self.is_letter_after_tanween_idhaar_letter(rule_end_index):
        ayah_idhaar_info = self.construct_rule_location_map(self.surah_number, self.ayah_number, rule_start_index, rule_end_index)
    elif tanween_type == 'fatha':
      rule_end_index = self.get_rule_end_index(rule_start_index, 3)
      ayah_idhaar_info = self.construct_rule_location_map(self.surah_number, self.ayah_number, rule_start_index, rule_end_index)
        
    return ayah_idhaar_info

  def construct_rule_location_map(self, surah, ayah, start_index, end_index):
    ayah_rule_info = {}
    ayah_rule_info["surah"] = surah
    ayah_rule_info["ayah"] = ayah
    ayah_rule_info["start"] = start_index
    ayah_rule_info["end"] = end_index
    return ayah_rule_info
 
  def is_letter_at_index_followed_by_space(self, index):
    if self.ayah_text[index+2] == " ":
      return True

  def is_letter_at_index_still_inside_ayah(self, index):
    if index + 2 < len(self.ayah_text)-1:
      return True

  def is_letter_after_noon_idhaar_letter(self, index):
    if self.ayah_text[index] in 'هءأإحعخغ':
      return True

  def is_letter_after_tanween_idhaar_letter(self, rule_end_index):
    if  self.ayah_text[rule_end_index] in 'هءأإحعخغ':
      return True

  def is_tanween_at_index_still_inside_ayah(self, rule_end_index):
    if rule_end_index < len(self.ayah_text)-1:
      return True

  def get_rule_end_index(self, start_index, move_by_spaces):
    return start_index + move_by_spaces
