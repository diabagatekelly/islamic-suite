from use_cases.rule_mapping_helpers import RuleMappingHelpers

class TanweenBasedRule(RuleMappingHelpers):
  def __init__(self, surah_number, ayah_number, ayah_text):
    self
    self.surah_number = surah_number
    self.ayah_number = ayah_number
    self.ayah_text = ayah_text
  
  def get_all_rule_locations(self, tanween_type, target_letter):
    tanween_indices = self.find_in_text(target_letter)

    if len(tanween_indices) == 0:
      return []

    tanween_rules = []

    for index in tanween_indices:
      tanween_idhaar = self.get_rule_location_details(tanween_type, index)
      if tanween_idhaar:
        tanween_rules.append(tanween_idhaar)

    return tanween_rules
  

  def find_in_text(self, target_letter):
    tanween_indices = [tanween_index for tanween_index, letter in enumerate(self.ayah_text) if letter in target_letter and tanween_index < len(self.ayah_text)-1]
    return tanween_indices

  def get_rule_location_details(self, tanween_type, index):
    ayah_idhaar_info = {}

    rule_start_index = index -1       

    if tanween_type != 'fatha':
      rule_end_index = self.get_rule_end_index(index, 2)
      if self.is_tanween_at_index_still_inside_ayah(rule_end_index) and self.is_letter_after_tanween_idhaar_letter(rule_end_index):
        ayah_idhaar_info = self.construct_rule_location_map(self.surah_number, self.ayah_number, rule_start_index, rule_end_index)
    elif tanween_type == 'fatha' and self.ayah_text[rule_start_index] != 'ة':
      rule_end_index = self.get_rule_end_index(index, 3)
      if self.is_tanween_at_index_still_inside_ayah(rule_end_index) and self.is_letter_after_tanween_idhaar_letter(rule_end_index-1):
        ayah_idhaar_info = self.construct_rule_location_map(self.surah_number, self.ayah_number, rule_start_index, rule_end_index)
        
    return ayah_idhaar_info
 
  def is_letter_after_tanween_idhaar_letter(self, rule_end_index):
    if self.ayah_text[rule_end_index] in 'هءأإحعخغ':
      return True
    else:
      return False

  def is_tanween_at_index_still_inside_ayah(self, rule_end_index):
    if rule_end_index < len(self.ayah_text)-1:
      return True
    else:
      return False
