from src.tajweed_rules_helpers.punctuation_marks import PunctuationMarks


class NoonSaakinRuleFactory():
    """Noon Saakin Rule Factory

    Factory for tajweed rules based on the silent letter "ن" (noon) or tanween ( ً ٍ ٌ). 
      1. noon saakin can carry a  ْ (sukoon) or be bare, and can be in the middle or end of a word
      2. tanween is always at the end of a word

    **Notes: 
      - The rules are being mapped using Uthmani Quran text
      - Both bare and voweled noon can be found in the middle or at the end of words
      - The noon saakin in the words 'صِنْوَانٌ' ,'دُنْيا' and 'قِنْوَانٌ' is an exception whereby it is pronounced
        with Idhaar (clearly) rather than Idghaam (merging) even though it is followed 
        by a Idghaam letter (ي)
      - Idghaam with/without Ghunnah has no instance in the middle
      - Iqlab has no fatha tanween instance

    Constructor:
      *surah_number - the number of the surah (chapter) in which the ayah is found
      *ayah_number - the number of the ayah (verse)
      *ayah_text - the text of the ayah

    Methods:
      *_find_final_index - finds the index of the last letter in an ayah, after excluding any marks that may follow it (vowels, meem of iqlab, stop signs)
      *_find_noon_saakin_in_text - in a given ayah text, find all noon saakin (bare or with sukoon) instances and save the noon's indices to a list
      *_find_tanween_base_in_text - in a given ayah text, find all instances of dummah, kasra and fatha tanween, and save their base letter's indices to a list
      *_get_rule_location_details - get the details of a rule's location in the Quran (surah, ayah, beginning index, ending index)
      *_get_correct_method_for_ending_letter - selects which method to run depending on which rule we are looking for
      *_is_ending_letter_an_idghaam_no_ghunnah_letter - checks if ending letter following noon/tanween is in "ل ر"
      *_is_ending_letter_an_idghaam_ghunnah_letter - checks if ending letter following noon/tanween is in "ي ن م و"
      *_is_ending_letter_an_ikhfa_letter - checks if ending letter following noon/tanween is in "ت ث ج د ذ ز س ش ص ض ط ظ ف ق ك"
      *_is_ending_letter_an_idhaar_letter - checks if ending letter following noon saakin is in "ٱ ع غ ح خ ه ء"
      *_is_ending_letter_an_iqlab_letter - checks if ending letter following noon is "ب"

      *get_all_rule_locations (public) - for a given rule found, get the details of all its location and save to an array
    """

    def __init__(self, surah_number, ayah_number, ayah_text):
        self
        self.surah_number = surah_number
        self.ayah_number = ayah_number
        self.ayah_text = ayah_text
        self.rules = ['idghaam_ghunnah', 'idghaam_no_ghunnah', 'idhaar', 'ikhfa', 'iqlab']
        self.punctuation_marks = PunctuationMarks()

    def get_all_rule_locations(self, rule):
        """For a given rule, get the details of all its location and saves to an array
          - parameters: rule (ighaam_no_ghunnah, idghaam_ghunnah, ikhfa, idhaar or iqlab)
          - returns: list of dicts:
          [{
            'surah': surah number, 
            'ayah': ayah number, 
            'start': starting letter index (the noon saakin itself)
            'end': ending letter index + a varying number to also cover that letter's vowel
          }]
        """
        noon_saakin_indices = []

        noon_saakin_indices = self._find_noon_saakin_in_text()
        noon_saakin_indices = noon_saakin_indices + self._find_tanween_base_in_text()

        if len(noon_saakin_indices) == 0:
            return []

        all_rule_locations = []

        for index in noon_saakin_indices:
            rule_location = self._get_rule_location_details(index, rule)
            if rule_location:
                all_rule_locations.append(rule_location)

        return all_rule_locations

    def _find_final_index(self):
        """Finds the index of the last letter in an ayah, after excluding any marks it may carry
          (vowels, meem of iqlab, stop signs).
          - retuns: index as integer
        """
        return self.punctuation_marks.calculate_adjustment_from_end(self.ayah_text)

    def _find_noon_saakin_in_text(self):
        """In an ayah, find noon saakin instances and save the noon's indices to a list.
        A noon saakin can have a sukoon or be bare.
        For a given noon:
          *letter_index: the noon's index
          *letter_index < self._find_final_index(): the noon is not the last letter in the ayah
          *letter_index + 1 in ["ْ", "ۢ", 'ۭ']: the noon has a sukoon or meem of iqlab
          *self.punctuation_marks.is_punctuation_mark(self.ayah_text[letter_index + 1]): the noon is bare
          - retuns: list of indices [3, 5, 8]
        """
        indices_for_noon = [
            letter_index for letter_index, letter in enumerate(self.ayah_text)
            if letter in ["ن"] and letter_index < self._find_final_index()
            and (self.ayah_text[letter_index + 1] in ["ْ", "ۢ", 'ۭ'] or (not self.punctuation_marks.is_punctuation_mark(self.ayah_text[letter_index + 1])))
        ]
        return indices_for_noon

    def _find_tanween_base_in_text(self):
        """In an ayah, find all kasra, dummah and fatha tanween instances and save the index of the base letter to a list.
        For a given tanween:
          *tanween_index - 1: the letter carrying tanween
          *not (tanween_index + 2 > len(self.ayah_text) - 1): the tanween is not the last mark in the ayah;
          in other words, the letter with tanween is not the last letter of the ayah
          *tanween in "ًٌٍ": dummah, kasra or fatha tanween
          - retuns: list of indices [3, 5, 8]
        """
        indices_for_tanween_base = [
            tanween_index - 1 for tanween_index, tanween in enumerate(self.ayah_text)
            if tanween in "ًٌٍ" and not (tanween_index + 2 > len(self.ayah_text) - 1)
        ]
        return indices_for_tanween_base

    def _get_rule_location_details(self, index, rule):
        """Get the details of a rule's location in the Quran (surah, ayah, beginning index, ending index)
          - parameters: index of noon or tanween base letter; rule (idghaam, ikhfa, idhaar)
          - returns: dictionary
          {
            'surah': surah number, 
            'ayah': ayah number, 
            'start': starting letter index (the noon saakin itself)
            'end': ending letter index + 2 to also cover that letter's vowel
          }
        """
        starting_letter_index = index
        ending_letter_index = starting_letter_index + \
            self.punctuation_marks.calculate_adjustment_from_beginning(
                self.ayah_text, starting_letter_index)

        # will match one of the following methods below:
        # _is_ending_letter_an_idghaam_letter, _is_ending_letter_an_ikhfa_letter, _is_ending_letter_an_idhaar_letter
        if self._get_correct_method_for_ending_letter(rule, index, ending_letter_index):
            return {
                'surah': self.surah_number,
                'ayah': self.ayah_number,
                'start': starting_letter_index,
                'end': ending_letter_index + 2  # Add 2 to encompass the last letter + its vowel
            }

    def _get_correct_method_for_ending_letter(self, rule, index, ending_letter_index):
        """Selects the correct ending letter rule to look for. 
          - parameters: rule, ending letter index
          - returns: callback method
        """
        if rule == 'idghaam_ghunnah':
            return self._is_ending_letter_an_idghaam_ghunnah_letter(ending_letter_index)
        elif rule == 'idghaam_no_ghunnah':
            return self._is_ending_letter_an_idghaam_no_ghunnah_letter(ending_letter_index)
        elif rule == 'ikhfa':
            return self._is_ending_letter_an_ikhfa_letter(ending_letter_index)
        elif rule == 'idhaar':
            return self._is_ending_letter_an_idhaar_letter(ending_letter_index)
        elif rule == 'iqlab':
            return self._is_ending_letter_an_iqlab_letter(index, ending_letter_index)

    def _is_ending_letter_an_idghaam_no_ghunnah_letter(self, ending_letter_index):
        """Checks if ending letter following bare noon or tanween is in "ل ر". 
        This means we found an instance of Idghaam.
          - parameters: ending letter index
          - returns: boolean
        """
        if self.ayah_text[ending_letter_index] in "لر":
            return True
        else:
            return False

    def _is_ending_letter_an_idghaam_ghunnah_letter(self, ending_letter_index):
        """Checks if ending letter following bare noon is in "ي ن م و". 
        This means we found an instance of Idghaam.
          - parameters: ending letter index
          - returns: boolean
        """
        if self.ayah_text[ending_letter_index] in "ينمو":
            return True
        else:
            return False

    def _is_ending_letter_an_ikhfa_letter(self, ending_letter_index):
        """Checks if ending letter following bare noon is in "ت ث ج د ذ ز س ش ص ض ط ظ ف ق ك". 
        Ikhfa letters are all the letters besides the letters of Idhaar,
        the letters of Idghaam, and the letter ب.
        This means we found an instance of Ikhfa.
          - parameters: ending letter index
          - returns: boolean
        """
        if self.ayah_text[ending_letter_index] not in "آٱبلرينموؤئأإعغحخهء":
            return True
        else:
            return False

    def _is_ending_letter_an_idhaar_letter(self, ending_letter_index):
        """Checks if ending letter following noon saakin is in "ٱ ع غ ح خ ه ء". 
        This means we found an instance of Idhaar.
          - parameters: ending letter index
          - returns: boolean
        """
        if self.ayah_text[ending_letter_index] in 'ٱآؤئأإعغحخهء':
            return True
        else:
            return False

    def _is_ending_letter_an_iqlab_letter(self, index, ending_letter_index):
        """Checks if ending letter following noon is "ب". 
        The noon of Iqlab carries a small 'ۢ ' on top or bottom.
        This means we found an instance of Iqlab.
          - parameters: starting letter index, ending letter index
          - returns: boolean
        """
        if self.ayah_text[index + 1] in "ۢ  ۭ" and self.ayah_text[ending_letter_index] in 'ب':
            return True
        else:
            return False
