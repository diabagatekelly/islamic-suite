from src.entities.meem_saakin_rules.meem_saakin_rule_factory import MeemSaakinRuleFactory

class IkhfaShafawi():
  """Ikhfa Shafawi (Meem Saakin Rule)

  If after silent "م" (meem saakin), there appears a "ب", ikhfa will take place. 
  This means the "ب" will be pronounced with a light nasalization. 
  The meem saakin alwasy appears at the end of a word, and in the Uthmani script it is bare.

  Example:
  105:4 تَرْمِيهِم بِحِجَارَةٍ مِّن سِجِّيلٍ

  Constructor:
    *surah_number - the number of the surah (chapter) in which the ayah is found
    *ayah_number - the number of the ayah (verse)
    *ayah_text - the text of the ayah

  Dependencies:
    *MeemSaakinRuleFactory (meem_type=bare, rule=ikhfa)

  Methods:
    *get_all_rule_locations (public) - initializes MeemSaakinRuleFactory and calls get_all_rule_locations
  """
  def __init__(self, surah_number, ayah_number, ayah_text):
    self
    self.surah_number = surah_number
    self.ayah_number = ayah_number
    self.ayah_text = ayah_text

  def get_all_rule_locations(self):
    """Initializes MeemSaakinRuleFactory and calls get_all_rule_locations
      - returns: list of dicts returned from MeemSaakinRuleFactory.get_all_rule_locations('bare', 'ikhfa')
      [{
        'surah': surah number, 
        'ayah': ayah number, 
        'start': starting letter index (the meem saakin itself)
        'end': ending letter index + a varying number to also cover that letter's vowel
      }]
    """
    meem_saakin_factory = MeemSaakinRuleFactory(self.surah_number, self.ayah_number, self.ayah_text)
    return meem_saakin_factory.get_all_rule_locations('bare', 'ikhfa')