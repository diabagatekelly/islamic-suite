from use_cases.rule_mapping_helpers import RuleMappingHelpers

class LetterBasedRule(RuleMappingHelpers):
  def __init__(self, surah_number, ayah_number, ayah_text):
    self
    self.surah_number = surah_number
    self.ayah_number = ayah_number
    self.ayah_text = ayah_text

  def get_all_rule_locations(self, target_letter):
    letter_indices = self.find_in_text(target_letter)

    if len(letter_indices) == 0:
      return []

    noon_rules = []

    for index in letter_indices:
      noon_idhaar = self.get_rule_location_details(index)
      if noon_idhaar:
        noon_rules.append(noon_idhaar)

    return noon_rules

  def find_in_text(self, target_letter):
    letter_indices = [letter_index for letter_index, letter in enumerate(self.ayah_text) if letter == target_letter and letter_index < len(self.ayah_text)-1 and self.ayah_text[letter_index+1] in "ْۡ"]
    return letter_indices


  def get_rule_location_details(self, index):
    rule_info = {}

    rule_start_index = index

    if not self.is_letter_after_index_still_inside_ayah(rule_start_index):
      return
    
    if self.is_letter_at_index_followed_by_space(rule_start_index):
      rule_end_index = self.get_rule_end_index(rule_start_index, 3)
      if self.is_letter_after_noon_idhaar_letter(rule_end_index):
        rule_info = self.construct_rule_location_map(self.surah_number, self.ayah_number, index, rule_end_index)
    elif not self.is_letter_at_index_followed_by_space(rule_start_index):
      rule_end_index = self.get_rule_end_index(rule_start_index, 2)
      if self.is_letter_after_noon_idhaar_letter(rule_end_index):
        rule_info = self.construct_rule_location_map(self.surah_number, self.ayah_number, index, rule_end_index)

    return rule_info

 
  def is_letter_at_index_followed_by_space(self, index):
    if self.ayah_text[index+2] == " ":
      return True
    else:
      return False

  def is_letter_after_index_still_inside_ayah(self, index):
    if index + 2 < len(self.ayah_text)-1:
      return True
    else:
      return False

  def is_letter_after_noon_idhaar_letter(self, end_index):
    if self.ayah_text[end_index] in 'هءأإحعخغ':
      return True
    else:
      return False

