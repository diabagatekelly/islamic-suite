from use_cases.rule import LetterBasedRule
from use_cases.rule import TanweenBasedRule

class Rule():
  def __init__(self, surah_number, ayah_number, ayah_text):
    self
    self.surah_number = surah_number
    self.ayah_number = ayah_number
    self.ayah_text = ayah_text

  def get_letter_based_locations(self, target_letter):
    letter = LetterBasedRule(self.surah_number, self.ayah_number, self.ayah_text)
    locations = letter.get_all_rule_locations(target_letter)
    
  
  def get_tanween_based_locations(self, tanween_type, target_letter):
    tanween = TanweenBasedRule(self.surah_number, self.ayah_number, self.ayah_text)
    locations = tanween.get_all_rule_locations(tanween_type, target_letter)