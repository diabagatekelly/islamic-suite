from src.tajweed_rules_helpers.punctuation_marks import PunctuationMarks

class MeemSaakinRules():
  """Meem Saakin Rules

  Find tajweed rules based on the silent letter "م" (meem).
  Some methods differ slightly based on the rule, which determines
  which letter to look for after meem saakin.

  **Notes:
    - The rules are being mapped using Uthmani Quran text
    - Bare meem is found at the end of words and applies to Ikhfa, Idghaam_shafawi
    - Meem saakin with sukoon is found in the middle or end of words and applies to Idhaar_shafawi
  
  Rules:
    
    Idghaam Shafawi
    If after silent "م" (meem saakin), there appears a "م", idghaam with ghunnah (nasalization)
    will take place. This means the second meem will become incorporated into the first and will 
    be read with nasalization. 
    The meem saakin always appears at the end of a word, and in the Uthmani script it is bare.
    Example:  106:4 ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍ وَءَامَنَهُم مِّنْ خَوْفٍۭ
    
    Idhaar Shafawi
    If after silent "م" (meem saakin), there appears any letter other than "م" or "ب", 
    idhaar will take place. This means the second letter will NOT become incorporated into the meem,
    but will rather be pronounced clearly.
    The meem saakin can appear in the middle or at the end of a word, and in the Uthmani script it carries a sukoon.
    Examples: 
    (middle) 111:4 وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ
    (end) 112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ
    
    Ikhfa Shafawi
    If after silent "م" (meem saakin), there appears a "ب", ikhfa will take place. 
    This means the "ب" will be pronounced with a light nasalization. 
    The meem saakin alwasy appears at the end of a word, and in the Uthmani script it is bare.
    Example:
    105:4 تَرْمِيهِم بِحِجَارَةٍ مِّن سِجِّيلٍ

  Properties:
    *_surah_number: number of the surah (Quran chapter) where the verse being mapped is found
    *_ayah_number: number of the ayah (verse) being mapped
    *_ayah_text: text of the ayah (verse) being mapped

  Methods:
    *_find_final_index - finds the index of the last letter in an ayah, after excluding any marks that might follow it (vowels, meem of iqlab, stop signs)
    *_find_meem_saakin_in_text - in a given ayah text, find all meem saakin (bare or with sukoon) instances and save the meem's indices to a list
    *_get_rule_location_details - get the details of a rule's location in the Quran (surah, ayah, beginning index, ending index)
    *_factory_for_finding_ending_letter_type - selects which method to run depending on which rule we are looking for
    *_is_ending_letter_an_idghaam_letter - checks if letter following meem saakin is "م" (meem)
    *_is_ending_letter_an_ikhfa_letter - checks if letter following meem saakin is "ب" (baa)
    *_is_ending_letter_an_idhaar_letter - checks if letter following meem saakin is anything but "م" or "ب"

    *get_all_rule_locations (public) - for a given rule, get the details of all its locations and save to a list
  """

  def __init__(self):
    self
    self._surah_number = None
    self._ayah_number = None
    self._ayah_text = None
    self.rules = ['idghaam_shafawi', 'idhaar_shafawi', 'ikhfa_shafawi']
    self.punctuation_marks = PunctuationMarks()
    
  @property
  def surah_number(self):
    return self._surah_number
  @surah_number.setter
  def surah_number(self, value):
    self._surah_number = value
    
  @property
  def ayah_number(self):
    return self._ayah_number
  @ayah_number.setter
  def ayah_number(self, value):
    self._ayah_number = value
    
  @property
  def ayah_text(self):
    return self._ayah_text
  @ayah_text.setter
  def ayah_text(self, value):
    self._ayah_text = value

  def get_all_rule_locations(self, rule):
    """For a given rule, get the details of all its location and save to a list
      - parameters: rule (ighaam_shafawi, ikhfa_shafawi or idhaar_shafawi)
      - returns: list of dicts:
      [{
        'surah': surah number,
        'ayah': ayah number,
        'start': starting letter index (the meem saakin itself)
        'end': ending letter index + 2 (the 2 is to also cover that letter's vowel)
      }]
    """
    if len(self._find_meem_saakin_in_text()) == 0:
      return []

    all_rule_locations = []

    for index in self._find_meem_saakin_in_text():
      rule_location = self._get_rule_location_details(index, rule)
      if rule_location:
        all_rule_locations.append(rule_location)

    return all_rule_locations

  def _find_meem_saakin_in_text(self):
    """In an ayah (verse), find meem saakin instances and save the meem's indices to a list.
    A meem saakin can have a sukoon or be bare.
    For a given meem:
      *letter_index: the meem's index
      *letter_index < self._find_final_index(): insures the meem is not the last letter in the ayah
      *letter_index + 1 in [" ", "ْ"]: the meem has a sukoon or is bare
      - retuns: list of indices [3, 5, 8]
    """
    indices_for_meem = [
      letter_index for letter_index, letter in enumerate(self.ayah_text)
      if letter in ["م"] and letter_index < self._find_final_index()
      and self.ayah_text[letter_index + 1] in [" ", "ْ"]
    ]
    return indices_for_meem
  
  def _find_final_index(self):
    """Finds the index of the last letter in an ayah (verse), after excluding any diacritical marks that might follow it
      (vowels, meem of iqlab, stop signs).
      - retuns: index as integer
    """
    return self.punctuation_marks.calculate_adjustment_from_end(self.ayah_text)

  def _get_rule_location_details(self, index, rule):
    """Get the details of a rule's location in the Quran (surah, ayah, beginning index, ending index)
      - parameters: index of meem; rule (idghaam_shafawi, ikhfa_shafawi, idhaar_shafawi)
      - returns: dictionary
      {
        'surah': surah number,
        'ayah': ayah number,
        'start': starting letter index (the meem saakin itself)
        'end': ending letter index + 2 to also cover that letter's vowel
      }
    """
    starting_letter_index = index
    ending_letter_index = starting_letter_index + \
      self.punctuation_marks.calculate_adjustment_from_beginning(self.ayah_text, starting_letter_index)

    # will match one of the following methods below:
    # _is_ending_letter_an_idghaam_letter, _is_ending_letter_an_ikhfa_letter, _is_ending_letter_an_idhaar_letter
    if self._factory_for_finding_ending_letter_type(rule, ending_letter_index):
      return {
        'surah': self.surah_number,
        'ayah': self.ayah_number,
        'start': starting_letter_index,
        'end': ending_letter_index + 2  # Add 2 to encompass the last letter + its vowel
      }

  def _factory_for_finding_ending_letter_type(self, rule, ending_letter_index):
    """Selects the correct ending letter rule to look for.
      - parameters: rule, ending letter index
      - returns: method
    """
    if rule == 'idghaam_shafawi':
      return self._is_ending_letter_an_idghaam_letter(ending_letter_index)
    elif rule == 'ikhfa_shafawi':
      return self._is_ending_letter_an_ikhfa_letter(ending_letter_index)
    elif rule == 'idhaar_shafawi':
      return self._is_ending_letter_an_idhaar_letter(ending_letter_index)

  def _is_ending_letter_an_idghaam_letter(self, ending_letter_index):
    """Checks if ending letter following meem is "م".
    This means we found an instance of Idghaam.
      - parameters: ending letter index
      - returns: boolean
    """
    if self.ayah_text[ending_letter_index] == "م":
      return True
    else:
      return False

  def _is_ending_letter_an_ikhfa_letter(self, ending_letter_index):
    """Checks if ending letter following meem is "ب".
    This means we found an instance of Ikhfa.
      - parameters: ending letter index
      - returns: boolean
    """
    if self.ayah_text[ending_letter_index] == "ب":
      return True
    else:
      return False

  def _is_ending_letter_an_idhaar_letter(self, ending_letter_index):
    """Checks if ending letter following meem is anything but "ب" or "م".
    This means we found an instance of Idhaar.
      - parameters: ending letter index
      - returns: boolean
    """
    if self.ayah_text[ending_letter_index] not in 'مب':
      return True
    else:
      return False