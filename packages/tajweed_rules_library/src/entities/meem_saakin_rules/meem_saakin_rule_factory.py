from src.entities_helpers.stop_signs import StopSigns

class MeemSaakinRuleFactory():
  """Meem Saakin Rule Factory

  Factory for tajweed rules based on the silent letter "م" (meem). Some methods differ slightly
  based on:
    1. wether the meem saakin is bare or carries a  ْ (sukoon) 
    2. the rule, which determines which letter to look for after meem saakin

  **Notes: 
    - The rules are being mapped using Uthmani Quran text
    - Bare meem is found at the end of words and applies to Ikhfa, Idghaam_shafawi
    - Meem with sukoon is found in the middle of words and applies to Idhaar_shafawi

  Constructor:
    *surah_number - the number of the surah (chapter) in which the ayah is found
    *ayah_number - the number of the ayah (verse)
    *ayah_text - the text of the ayah

  Methods:
    *_find_bare_meem_saakin_in_text - in a given ayah text, find all bare meem saakin instances and save the meem's indices to an array
    *_find_meem_saakin_with_sukoon_in_text - in a given ayah text, find all instances of meem saakin with sukoon and save the sukoon indices to an array
    *_get_rule_location_details - get the details of a rule's location in the Quran (surah, ayah, beginning index, ending index)
    *_get_ending_letter_index - based on the index of meem saakin or sukoon, find the index of the relevant letter following meem saakin
    *_is_meem_saakin_at_end_of_a_word - checks whether meem saakin is the last letter in a word
    *_get_correct_method_for_ending_letter - selects which method to run depending on which rule we are looking for
    *_is_ending_letter_an_idghaam_letter - checks if letter following meem saakin is "م" (meem)
    *_is_ending_letter_an_ikhfa_letter - checks if letter following meem saakin is "ب" (baa)
    *_is_ending_letter_an_idhaar_letter - checks if letter following meem saakin is anything but "م" or "ب"

    *get_all_rule_locations (public) - for a given rule found, get the details of all its location and save to an array
  """
  def __init__(self, surah_number, ayah_number, ayah_text):
    self
    self.surah_number = surah_number
    self.ayah_number = ayah_number
    self.ayah_text = ayah_text
    self.stop_signs = StopSigns()

  def get_all_rule_locations(self, meem_type, rule):
    """For a given rule, get the details of all its location and saves to an array
      - parameters: meem_type (bare or with_sukoon); rule (ighaam, ikhfa or idhaar)
			- returns: list of dicts:
      [{
        'surah': surah number, 
        'ayah': ayah number, 
        'start': starting letter index (the meem saakin itself)
        'end': ending letter index + a varying number to also cover that letter's vowel
      }]
    """
    meem_saakin_indices = []
    if meem_type == 'bare':
      meem_saakin_indices = self._find_bare_meem_saakin_in_text()
    elif meem_type == 'with_sukoon':
      meem_saakin_indices = self._find_meem_saakin_with_sukoon_in_text()

    if len(meem_saakin_indices) == 0:
      return []

    all_rule_locations = []

    for index in meem_saakin_indices:
      rule_location = self._get_rule_location_details(index, meem_type, rule)
      if rule_location:
        all_rule_locations.append(rule_location)

    return all_rule_locations

  def _find_bare_meem_saakin_in_text(self):
    """In an ayah, find all bare meem saakin instances and save the meem's indices to an array
    A bare meem saakin is always found at the end of a word. [Ikhfa, Idghaam_shafawi]
    For a given meem:
      *letter_index: the meem
      *letter_index + 1 < len(self.ayah_text) - 1: the vowel on the meem is not the last mark in the ayah;
      in other words, this meem is not the last letter of the ayah
      *letter_index + 1 not in "ًٌٍَُِّْ~ٰ": there is no vowel on the meem
      - retuns: list of indices [3, 5, 8]
    """
    indices_for_meem = [
      letter_index for letter_index, letter in enumerate(self.ayah_text) 
      if letter in ["م"] and letter_index + 1 < len(self.ayah_text) - 1 
      and self.ayah_text[letter_index + 1] not in 'ًٌٍَُِّْ~ٰ'
    ]
    return indices_for_meem

  def _find_meem_saakin_with_sukoon_in_text(self):
    """In an ayah, find all instances of meem saakin with sukoon and save the SUKOON indices to an array
    A noon saakin with sukoon can be in the middle or at the end of a word. [Idhaar]
    For a given meem:
      *letter_index + 1: the vowel on the meem
      *letter_index + 1 < len(self.ayah_text) - 1: the vowel on the meem is not the last mark in the ayah;
      in other words this meem is not the last letter of the ayah
      *letter_index + 1 in "ْ": the meem has a sukoon
      - retuns: list of indices [3, 5, 8]
    """
    indices_for_sukoon_on_meem = [
      letter_index + 1 for letter_index, letter in enumerate(self.ayah_text) 
      if letter in ["م"] and letter_index + 1 < len(self.ayah_text) - 1 
      and self.ayah_text[letter_index + 1] in "ْ"]
    return indices_for_sukoon_on_meem

  def _get_rule_location_details(self, index, meem_type, rule):
    """Get the details of a rule's location in the Quran (surah, ayah, beginning index, ending index)
      - parameters: index of meem or meem's sukoon; meem_type (bare or with_sukoon); rule (idghaam, ikhfa, idhaar)
      - returns: dictionary
      {
        'surah': surah number, 
        'ayah': ayah number, 
        'start': starting letter index (the meem saakin itself)
        'end': ending letter index + a varying number to also cover that letter's vowel
      }
    """
    if meem_type == 'bare':
      starting_letter_index = index # the meem itself
      ending_letter_index = self._get_ending_letter_index(index, 'bare')
    elif meem_type == 'with_sukoon':
      # work backward from the sukoon on the meem
      starting_letter_index = index - 1 
      ending_letter_index = self._get_ending_letter_index(starting_letter_index, 'with_sukoon')
    
    # will match one of the following methods below:
    # _is_ending_letter_an_idghaam_letter, _is_ending_letter_an_ikhfa_letter, _is_ending_letter_an_idhaar_letter
    if self._get_correct_method_for_ending_letter(rule, ending_letter_index):
      return {
        'surah': self.surah_number,
        'ayah': self.ayah_number,
        'start': starting_letter_index,
        'end': ending_letter_index + 2  # Add 2 to encompass the last letter + its vowel
      }

  def _get_ending_letter_index(self, index, meem_type):
    """Returns ending letter index after checking if meem saakin is followed 
      by a stop sign. 
      - parameters: index of meem
      - returns: index as an integer
    """
    if meem_type == 'bare': # bare is always at the end
      adjustment_for_stop = self.stop_signs.find_stop_sign_for_bare_letter()
      if self.ayah_text[index + adjustment_for_stop] in self.stop_signs.list_of_signs:
        # meem + stop sign (2) + space (3) + next letter (4)
        return index + 4
      else:
        # meem + space (1) + next letter (2)
        return index + 2
    elif meem_type == 'with_sukoon': # can be in the middle or end
      adjustment_for_stop = self.stop_signs.find_stop_sign_for_voweled_letter()
      ending = 0
      if self.ayah_text[index + adjustment_for_stop] in self.stop_signs.list_of_signs:
        if self._is_meem_saakin_at_end_of_a_word(index + adjustment_for_stop + 1):
        # meem + sukoon (1) + stop sign (3) + space (4) + next letter (5)
          ending = index + 5
        else:
          # meem + sukoon (1) + stop sign (3) + next letter (5)
          ending = index + 4
      else:
        if self._is_meem_saakin_at_end_of_a_word(index + 2):
          # meem + sukoon (1) + space (2) + next letter (3)
          ending = index + 3
        else:
          # meem + sukoon (1) + next letter (2)
          ending = index + 2
      return ending

  def _is_meem_saakin_at_end_of_a_word(self, ending):
    """Checks if meem saakin is at the end of a word depending on whether it is followed by a space.
    This only applies to meem with sukoon because bare meem sakin is always at the end of a word.
    We start at indices meem + sukoon (1); if the next index is a space, it means meem saakin was at the end of the word.
      - parameters: index of next letter or space
      - retuns: boolean
    """
    if self.ayah_text[ending] == " ":
      return True
    else:
      return False

  def _get_correct_method_for_ending_letter(self, rule, ending_letter_index):
    """Selects the correct ending letter rule to look for. 
      - parameters: rule, ending letter index
      - returns: callback method
    """
    if rule == 'idghaam':
      return self._is_ending_letter_an_idghaam_letter(ending_letter_index)
    elif rule == 'ikhfa':
      return self._is_ending_letter_an_ikhfa_letter(ending_letter_index)
    elif rule == 'idhaar':
      return self._is_ending_letter_an_idhaar_letter(ending_letter_index)

  def _is_ending_letter_an_idghaam_letter(self, ending_letter_index):
    """Checks if ending letter following bare meem is "م". 
    This means we found an instance of Idghaam.
      - parameters: ending letter index
      - returns: boolean
    """
    if self.ayah_text[ending_letter_index] == "م":
      return True
    else:
      return False

  def _is_ending_letter_an_ikhfa_letter(self, ending_letter_index):
    """Checks if ending letter following bare meem is "ب". 
    This means we found an instance of Ikhfa.
      - parameters: ending letter index
      - returns: boolean
    """
    if self.ayah_text[ending_letter_index] == "ب":
      return True
    else:
      return False

  def _is_ending_letter_an_idhaar_letter(self, ending_letter_index):
    """Checks if ending letter following meem with sukoon is anything but "ب" or "م". 
    This means we found an instance of Idhaar.
      - parameters: ending letter index
      - returns: boolean
    """
    if self.ayah_text[ending_letter_index] not in 'مب':
      return True
    else:
      return False