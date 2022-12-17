class PunctuationMarks():
  """Punctuation Marks

  This class calculates how many indices are between a starting index and the target ending index, 
  by calculating an adjustment based on the presence of any punctuation mark or space. 
    * Stop signs have an imperceptible space before them
    * Other punctuation marks on on top or at the bottom of a letter

  Stop signs:
    ۘ - Must stop
    ۚ - Permissible stop (can stop or continue)
    ۖ - Allowed to stop but better to continue
    ۗ - Preferred to stop
    ۜ - The silence symbol, indicates the reader should take a brief pause without breaking its breath
    ۛ ۛ- The linked stops; must stop at one or the other
    ۙ - Forbidden to stop

  Meem of Iqlab:
    ۢ ۭ - Meem of Iqlab, found on top or bottom of noon saakin

  Non_sukoon_vowels:
    َ - fatha
    ِ - kasra
    ُ - dummah
    ً - fatha tanween
    ٍ - kasra tanween
    ٌ - dummah tanween
    ~ - madd
    ٰ - dagger alif
    
  Sukoon:
    ْ- sukoon

  Miscellaneous
      - empty space at end of word
    ا - alif after fatha tanween

  Methods:
    *calculate_adjustment_from_beginning (public) - calculates the adjusted number to add to the starting index to find the ending index for any rule
    *calculate_adjustment_from_end (public) - finds the index of the last letter in the ayah, after counting back from any marks or stop signs
  """

  def __init__(self):
    self.stop_signs = ["ۗ", "ۚ", "ۜ", "ۛ", "ۙ", "ۘ", "ۖ"]
    self.iqlab_meem = ["ۢ", 'ۭ']
    self.madd_vowels = ["ٓ"]
    self.non_sukoon_vowels_no_madd = ["َ", "ِ", "ُ", "ً", "ٍ", "ٌ", "ّ", "ٰ"]
    self.non_sukoon_vowels = self.madd_vowels + self.non_sukoon_vowels_no_madd
    self.sukoon = ["ْ", "۠"]
    self.miscellaneous = [" ", 'ا']

  def calculate_adjustment_from_beginning(self, ayah_text, starting_letter_index):
    """Calculates the adjusted number to add to the starting index to find the ending index for any rule
      - parameters: ayah_text, starting_letter_index
      - retuns: adjustment to add to starting_letter_index as integer
    """
    adjustment = 1
    current_index = starting_letter_index + 1
    all_possible_punctuation = self.stop_signs + \
      self. iqlab_meem + self.non_sukoon_vowels + self.sukoon + self.miscellaneous
    while ayah_text[current_index] in all_possible_punctuation:
      adjustment += 1
      current_index += 1
    return adjustment

  def calculate_adjustment_from_end(self, ayah_text):
    """Finds the index of the last letter in the ayah, after counting back from any marks or stop signs
      - parameters: ayah_text
      - retuns: index of the last letter as an integer
    """
    last_index = len(ayah_text) - 1
    all_possible_punctuation = self.stop_signs + \
      self. iqlab_meem + self.non_sukoon_vowels + self.sukoon + self.miscellaneous
    while ayah_text[last_index] in all_possible_punctuation:
      last_index -= 1
    return last_index
  
  def is_punctuation_mark(self, mark):
    """Determines if a mark is a punctuation mark (meem of iqlaab, vowels including sukoon)
      - parameters: mark
      - retuns: boolean
    """
    all_possible_punctuation = self.iqlab_meem + self.non_sukoon_vowels + self.sukoon
    if mark in all_possible_punctuation:
      return True
    else: 
      return False

