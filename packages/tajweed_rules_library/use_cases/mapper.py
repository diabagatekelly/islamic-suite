class Mapper():
  def __init__(self, surah_number, ayah_number, ayah_text):
    self
    self.surah_number = surah_number
    self.ayah_number = ayah_number
    self.ayah_text = ayah_text

  def get_all_rule_locations(self, target):
    target_vowel_indices = self.find_in_text(target)

    if len(target_vowel_indices) == 0:
      return []

    all_rule_locations = []

    for vowel_index in target_vowel_indices:
      rule_location = self.get_rule_location_details(vowel_index)
      if rule_location:
        all_rule_locations.append(rule_location)

    return all_rule_locations


  def find_in_text(self, target):
    target_vowel_indices = []
    if target in "من":
      target_vowel_indices = [letter_index+1 for letter_index, letter in enumerate(self.ayah_text) if letter in target and letter_index+1 < len(self.ayah_text)-1 and self.ayah_text[letter_index+1] in "ْۡ"]
    elif target in "ًٌٍ":
      target_vowel_indices = [tanween_index for tanween_index, tanween in enumerate(self.ayah_text) if tanween in target and tanween_index+2 < len(self.ayah_text)-1]
    return target_vowel_indices


  def get_rule_location_details(self, vowel_index):
    starting_letter_index = vowel_index - 1
    ending_letter_index = self.get_ending_letter_index(starting_letter_index)
    
    if self.is_ending_letter_an_idhaar_letter(ending_letter_index):
      return {
        'surah': self.surah_number,
        'ayah': self.ayah_number,
        'start': starting_letter_index,
        'end': ending_letter_index
      }


  def get_ending_letter_index(self, starting_letter_index):
    ending_letter_index = 0

    if self.is_rule_at_end_of_a_word_and_fatha_tanween(starting_letter_index):
      ending_letter_index = starting_letter_index + 4
    elif self.is_non_fatha_tanween_rule_at_end_of_a_word(starting_letter_index):
      ending_letter_index = starting_letter_index + 3
    elif not self.is_non_fatha_tanween_rule_at_end_of_a_word(starting_letter_index):
      ending_letter_index = starting_letter_index + 2

    return ending_letter_index


  def is_non_fatha_tanween_rule_at_end_of_a_word(self, starting_letter_index):
    if self.ayah_text[starting_letter_index + 2] == " ":
      return True
    else:
      return False


  def is_rule_at_end_of_a_word_and_fatha_tanween(self, starting_letter_index):
    if self.ayah_text[starting_letter_index + 2] == "ا" and self.ayah_text[starting_letter_index + 3] == " ":
      return True
    else:
      return False


  def is_ending_letter_an_idhaar_letter(self, ending_letter_index):
    if self.ayah_text[ending_letter_index] in 'هءأإحعخغ':
      return True
    else:
      return False

