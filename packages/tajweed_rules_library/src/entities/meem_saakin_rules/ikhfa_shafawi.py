class IkhfaShafawi():
  def __init__(self, surah_number, ayah_number, ayah_text):
    self
    self.surah_number = surah_number
    self.ayah_number = ayah_number
    self.ayah_text = ayah_text

  def get_all_rule_locations(self):
    meem_saakin_indices = self.find_meem_saakin_in_text()

    if len(meem_saakin_indices) == 0:
      return []

    all_rule_locations = []

    for sukoon_index in meem_saakin_indices:
      rule_location = self.get_rule_location_details(sukoon_index)
      if rule_location:
        all_rule_locations.append(rule_location)

    return all_rule_locations

  def find_meem_saakin_in_text(self):
    indices_for_sukoon_on_meem = [letter_index + 1 for letter_index, letter in enumerate(self.ayah_text) if letter in ["م"] and letter_index + 1 < len(self.ayah_text)-1 and self.ayah_text[letter_index + 1] not in "ًٌٍَُِّْ~"]
    return indices_for_sukoon_on_meem

  def get_rule_location_details(self, vowel_index):
    starting_letter_index = vowel_index -1
    ending_letter_index = self.get_ending_letter_index(starting_letter_index)
    
    if self.is_ending_letter_an_idghaam_letter(ending_letter_index):
      return {
        'surah': self.surah_number,
        'ayah': self.ayah_number,
        'start': starting_letter_index,
        'end': ending_letter_index + 2
      }

  def get_ending_letter_index(self, starting_letter_index):
    ending_letter_index = 0

    if self.ayah_text[starting_letter_index + 1] == "ْ":
      ending_letter_index = self.is_meem_saakin_with_sukoon(starting_letter_index)
    else:
      ending_letter_index = self.is_meem_saakin_without_sukoon(starting_letter_index)

    return ending_letter_index

  def is_meem_saakin_with_sukoon(self, starting_letter_index):
    return starting_letter_index + 3
  
  def is_meem_saakin_without_sukoon(self, starting_letter_index):
    return starting_letter_index + 2

  def is_ending_letter_an_idghaam_letter(self, ending_letter_index):
    if self.ayah_text[ending_letter_index] == "ب":
      return True
    else:
      return False
#test ikhfa