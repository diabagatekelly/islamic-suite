class MeemSaakinRuleFactory():
  """Meem Saakin Rule Factory

  Factory for tajweed rules based on the silent letter "م" (meem). Some methods differ slightly
  based on:
    1. wether the meem saakin is bare or carries a  ْ (sukoon) 
    2. the rule, which determines which letter to look for after meem saakin

  **Note: The rules are being mapped using Uthmani Quran text

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
    *_get_correct_ending_letter_check - selects which method to run depending on which rule we are looking for
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

  def get_all_rule_locations(self, meem_type, rule):
    """For a given rule, get the details of all its location and saves to an array
      - parameters: meem_type (bare or with_sukoon); rule (ighaam, ikhfa or idhaar)
			- returns: list of dicts:
      {
        'surah': surah number, 
        'ayah': ayah number, 
        'start': starting letter index (the meem saakin itself)
        'end': ending letter index + a varying number to also cover that letter's vowel
      }
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
    For a given meem:
      *letter_index: the meem
      *letter_index + 1 < len(self.ayah_text) - 1: the vowel on the meem is not the last mark in the ayah;
      in other words, this meem is not the last letter of the ayah
      *letter_index + 1 not in "ًٌٍَُِّْ~": there is no vowel on the meem
      - retuns: list of indices [3, 5, 8]
    """
    indices_for_meem = [
      letter_index for letter_index, letter in enumerate(self.ayah_text) 
      if letter in ["م"] and letter_index + 1 < len(self.ayah_text) - 1 
      and self.ayah_text[letter_index + 1] not in "ًٌٍَُِّْ~"
    ]
    return indices_for_meem

  def _find_meem_saakin_with_sukoon_in_text(self):
    """In an ayah, find all instances of meem saakin with sukoon and save the sukoon indices to an array
    For a given meem:
      *letter_index + 1: the vowel on the meem
      *letter_index + 1 < len(self.ayah_text) - 1: the vowel on the meem is not the last mark in the ayah;
      in other words this meem is not the last letter of the ayah
      *letter_index + 1 in "ْ": the meem has a sukoon
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
      ending_letter_index = starting_letter_index + 2 # add 2 (space + ending_letter)
    elif meem_type == 'with_sukoon':
      starting_letter_index = index - 1 # work backward from the sukoon on the meem
      # will vary depending on if meem is in the middle of a word or at the end
      ending_letter_index = self._get_ending_letter_index(starting_letter_index)
    
    # will match one of the following methods below:
    # _is_ending_letter_an_idghaam_letter, _is_ending_letter_an_ikhfa_letter, _is_ending_letter_an_idhaar_letter
    if self._get_correct_ending_letter_check(rule, ending_letter_index):
      return {
        'surah': self.surah_number,
        'ayah': self.ayah_number,
        'start': starting_letter_index,
        'end': ending_letter_index + 2  # this will encompass the last letter + its vowel
      }

  def _get_ending_letter_index(self, starting_letter_index):
    """Add 2 or 3 to the starting meem saaking to get to the last letter of the rule
     - parameters: meem saaking index
     - returns: ending letter index (int)
    """
    ending_letter_index = 0

    if self._is_meem_saakin_at_end_of_a_word(starting_letter_index):
      # meem + sukoon (1) + space (2) + ending_letter (3) = 3
      ending_letter_index = starting_letter_index + 3
    elif not self._is_meem_saakin_at_end_of_a_word(starting_letter_index):
      # meem + sukoon (1) + ending_letter (2) = 2
      ending_letter_index = starting_letter_index + 2

    return ending_letter_index

  def _is_meem_saakin_at_end_of_a_word(self, starting_letter_index):
    """Checks if meem saakin is at the end of a word depending on whether it is followed by a space;
    This only applies to meem with sukoon because bare meem sakin is always at the end of a word.
    meem + sukoon (1); if the next index is a space, it means meem saakin was at the end of the word
      - parameters: meem saakin index
      - retuns: boolean
    """
    if self.ayah_text[starting_letter_index + 2] == " ":
      return True
    else:
      return False

  def _get_correct_ending_letter_check(self, rule, ending_letter_index):
    """Selects the correct ending letter rule to look for. 
      - parameters: rule, ending letter index
      - returns: method
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