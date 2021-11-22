def find_all_letter_indices(self, sign, text):
    letter_indices = [letter_index for letter_index, letter in enumerate(text) if letter == sign and letter_index < len(text)-1 and text[letter_index+1] == "ْ"]
    return letter_indices


  def find_all_tanween_indices(self, sign, text):
    tanween_indices = [tanween_index for tanween_index, letter in enumerate(text) if letter in sign and tanween_index < len(text)-1]
    return tanween_indices


  def extract_letter_rule_data(self, rule, indices, text, surah, ayah):
    rule_info = {}

    if len(indices) > 0:
      index = int(indices[0])

      if index + 2 < len(text)-1 and text[index+2] == " ":
        index = index + 3
        rule_info = self.save_index_for_letter_in_target(rule, text, index, 3, surah, ayah)
      elif index +2 < len(text)-1 and text[index+2] != " ":
        index = index + 2
        rule_info = self.save_index_for_letter_in_target(rule, text, index, 2, surah, ayah)

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
      return self.parse_rule_location_details(surah, ayah, base, index + adjustment)


  def save_index_for_letter_in_target(self, rule, text, index, adjustment, surah, ayah):
    if rule == 'idhaar' and text[index] in 'هءأإحعخغ':
      return self.parse_rule_location_details(surah, ayah, index - adjustment, index)
    elif rule != 'idhaar' and text[index] not in 'مب':
      return self.parse_rule_location_details(surah, ayah, index - adjustment, index)