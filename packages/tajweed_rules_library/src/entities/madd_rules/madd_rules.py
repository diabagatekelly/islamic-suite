from src.tajweed_rules_helpers.punctuation_marks import PunctuationMarks

class MaddRules():
  """Madd Rules
  
  Madd means to lenghten the letters of madd or leen. 
  The letters of madd are "ا و ى" carrying a sukoon.
  Alif saakin must be preceded by a letter carrying fatha: عَا
  Yaa saakin must be preceded by a letter carrying kasra: عِي
  Wow saakin must be preceded by a letter carrying dummah: عُو
  A letter carrying fatha followed by wow or yaa saakin is called 
  a 'Leen' letter: عَي, عَو
  
  **Notes:
    - The rules are being mapped using Uthmani Quran text
    - The letters of madd are bare
    - The letters of leen carry the round sukoon
    
  Rules:
  
  There are 2 broad types of madd:
  A. Madd Asli: length -> 2 vowels
    - "ا و ى" not preceded by hamza
    - "ا و ى" not followed by hamza or sukoon
    
  B. Madd Far'i
  

  Properties:
    *_surah_number: number of the surah (Quran chapter) where the verse being mapped is found
    *_ayah_number: number of the ayah (verse) being mapped
    *_ayah_text: text of the ayah (verse) being mapped

  Methods:
    *_find_madd_letters_in_text - gathers and sorts all indices for full madd, dagger madd and madd leen instances in a given ayah
    *_find_full_madd_letter_in_text - finds all full madd letter instances in an ayah
    *_find_dagger_letter_in_text - finds all dagger letter instances in an ayah
    *_find_leen_madd_letter_in_text - finds all instances of madd leen in an ayah
    *_get_rule_location_details - get the details of a rule's location in the Quran (surah, ayah, beginning index, ending index)
    
    *get_all_rule_locations (public) - for a given rule, get the details of all its locations and save to a list
  
  
  
  *_find_final_index - finds the index of the last letter in an ayah, after excluding any marks that might follow it (vowels, meem of iqlab, stop signs)
    
    
    *_factory_for_finding_ending_letter_type - selects which method to run depending on which rule we are looking for
    *_is_ending_letter_an_idghaam_letter - checks if letter following meem saakin is "م" (meem)
    *_is_ending_letter_an_ikhfa_letter - checks if letter following meem saakin is "ب" (baa)
    *_is_ending_letter_an_idhaar_letter - checks if letter following meem saakin is anything but "م" or "ب"

  """

  def __init__(self):
    self
    self._surah_number = None
    self._ayah_number = None
    self._ayah_text = None
    self.rules = ['madd_asli', "madd_fari"]
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
      - parameters: rule (madd_asli, madd_fari)
      - returns: list of dicts:
      [{
        'surah': surah number,
        'ayah': ayah number,
        'start': starting letter index (the meem saakin itself)
        'end': ending letter index + 2 (the 2 is to also cover that letter's vowel)
      }]
    """
    if len(self._find_madd_letters_in_text()) == 0:
      return []

    all_rule_locations = []

    for index in self._find_madd_letters_in_text():
      rule_location = self._get_rule_location_details(index, rule)
      if rule_location:
        all_rule_locations.append(rule_location)
    return all_rule_locations
  

  def _find_madd_letters_in_text(self):
    all_madd_letters = []
    all_madd_letters = all_madd_letters + self._find_full_madd_letter_in_text() + self._find_dagger_letter_in_text() + self._find_leen_madd_letter_in_text()
    all_madd_letters.sort()
    return all_madd_letters

  def _find_full_madd_letter_in_text(self):
    """In an ayah (verse), find all full madd letters (ا و ى) instances and save the madd letter's indices to a list.
    A madd letter is bare.
    For a given madd letter:
      *letter_index: the madd letter's index
      *self.ayah_text[letter_index + 1] not in 
      (self.punctuation_marks.non_sukoon_vowels + self.punctuation_marks.sukoon)): the madd letter is bare
      *letter in "ٰۦۥ": accounts for dagger and small variations of the madd letters
      - retuns: list of indices [3, 5, 8]
    """
    all_vowels_except_madd = self.punctuation_marks.sukoon + self.punctuation_marks.non_sukoon_vowels_no_madd
    indices_for_full_madd = [
      letter_index for letter_index, letter in enumerate(self.ayah_text) 
      if letter in ["ا", "و", "ي", "ى"] 
      and self.ayah_text[letter_index + 1] not in all_vowels_except_madd
      and self.ayah_text[letter_index - 1] not in self.punctuation_marks.tanweens
      and self.ayah_text[letter_index - 1] not in self.punctuation_marks.iqlab_meem
    ]
    return indices_for_full_madd
  
  def _find_dagger_letter_in_text(self):
    """In an ayah (verse), find all dagger madd letters ("ٰۦۥ") instances and save the dagger letter's indices to a list.
    For a given dagger madd letter:
      *letter_index: the dagger letter's index
      *letter in "ٰۦۥ": make sure it is a dagger letter
      - retuns: list of indices [3, 5, 8]
    """
    indices_for_dagger_madd = [
      letter_index for letter_index, letter in enumerate(self.ayah_text) if letter in "ٰۦۥ"
    ]
    return indices_for_dagger_madd
  
  def _find_leen_madd_letter_in_text(self):
    """In an ayah (verse), find all leen madd letters (و ى) instances and save the leen letter's indices to a list.
    A leen letter has the round sukoon on it.
    For a given madd letter:
      *letter_index: the madd letter's index
      *self.ayah_text[letter_index + 1] in (self.punctuation_marks.sukoon)): the leen letter has sukoon
      *self.ayah_text[letter_index - 1] === 'َ'): the vowel before the leen letter is fatha
      *letter in ['و', 'ي']: the leen letter in wow or yaa 
     
      - retuns: list of indices [3, 5, 8]
    """
    indices_for_leen_madd = [
      letter_index for letter_index, letter in enumerate(self.ayah_text)
      if (letter in ["و", "ي"] 
      and (self.ayah_text[letter_index + 1] in (self.punctuation_marks.sukoon)) 
      and (self.ayah_text[letter_index - 1] in "َ"))
    ]
    return indices_for_leen_madd
  
  
  def _get_rule_location_details(self, index, rule):
    """Get the details of a rule's location in the Quran (surah, ayah, beginning index, ending index)
      - parameters: index of madd letter; rule (madd_asli, madd_fari)
      - returns: dictionary
      {
        'surah': surah number,
        'ayah': ayah number,
        'start': starting letter index (the madd letter itself)
        'end': ending letter index + 2 to also cover that letter's vowel
      }
    """
    first_preceding_letter = index - self.punctuation_marks.find_closest_preceding_letter(self.ayah_text, index)
    ending_letter_index = index + \
      self.punctuation_marks.calculate_adjustment_from_beginning(self.ayah_text, index)
      
      
    if rule == 'madd_asli' and self._is_letter_at_index_madd_asli(first_preceding_letter, ending_letter_index):
      return {
        'surah': self.surah_number,
        'ayah': self.ayah_number,
        'start': first_preceding_letter,
        'end': ending_letter_index
      }
    elif rule == 'madd_fari' and not self._is_letter_at_index_madd_asli(first_preceding_letter, ending_letter_index):
      print(index, 'index*****************')
      print(self.ayah_text[first_preceding_letter], 'start', first_preceding_letter)
      print(self.ayah_text[ending_letter_index], 'end', ending_letter_index)
      return {
        'surah': self.surah_number,
        'ayah': self.ayah_number,
        'start': first_preceding_letter,
        'end': ending_letter_index
      }

      
  def _is_letter_at_index_madd_asli(self, starting_index, ending_index):
    return not (self._is_preceded_by_hamza(starting_index) 
    or self._is_followed_by_hamza(ending_index) or self._is_followed_by_sukoon(ending_index))
      
  def _is_preceded_by_hamza(self, starting_index):
    return self.ayah_text[starting_index] in ['ء', 'ؤ', "ئ", "أ", "إ", "ٔ"]
  
  def _is_followed_by_hamza(self, ending_index):
    return self.ayah_text[ending_index] in ['ء', 'ؤ', "ئ", "أ", "إ", "ٔ"]
  
  def _is_followed_by_sukoon(self, ending_index):
    sukoon_and_shaddah = self.punctuation_marks.sukoon + ["ّ"]
    if ending_index == len(self.ayah_text) - 1:
      return False
    
    return self.ayah_text[ending_index + 1] in sukoon_and_shaddah
    
      

      
      
      
      
      
      
      
        # def _find_final_index(self):
  #   """Finds the index of the last letter in an ayah (verse), after excluding any diacritical marks that might follow it
  #     (vowels, meem of iqlab, stop signs).
  #     - retuns: index as integer
  #   """
  #   return self.punctuation_marks.calculate_adjustment_from_end(self.ayah_text)