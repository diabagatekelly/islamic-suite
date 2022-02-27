from src.entities.meem_saakin_rules.meem_saakin_rule_factory import MeemSaakinRuleFactory

class IdhaarShafawi():
  def __init__(self, surah_number, ayah_number, ayah_text):
    self
    self.surah_number = surah_number
    self.ayah_number = ayah_number
    self.ayah_text = ayah_text

  def get_all_rule_locations(self):
    meem_saakin_factory = MeemSaakinRuleFactory(
        self.surah_number, self.ayah_number, self.ayah_text)
    return meem_saakin_factory.get_all_rule_locations('with_sukoon', 'idhaar')