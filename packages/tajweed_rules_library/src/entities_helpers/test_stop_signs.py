import unittest
from src.entities_helpers.stop_signs import StopSigns
from src.entities.meem_saakin_rules.meem_saakin_rule_factory import MeemSaakinRuleFactory

# MEEM SAAKIN "MUST STOP ۘ "
# Voweled
must_stop_idhaar_shafawi_end = 'فَتَوَلَّ عَنْهُمْ ۘ يَوْمَ يَدْعُ ٱلدَّاعِ إِلَىٰ شَىْءٍ نُّكُرٍ'

# MEEM SAAKIN "PERMISSIBLE STOP ۚ "
# Bare
permissible_stop_ikhfa_shafawi_end = 'أَمْ يَحْسَبُونَ أَنَّا لَا نَسْمَعُ سِرَّهُمْ وَنَجْوَىٰهُم ۚ بَلَىٰ وَرُسُلُنَا لَدَيْهِمْ يَكْتُبُونَ'
permissible_stop_idghaam_shafawi_end = 'إِنِّى تَوَكَّلْتُ عَلَى ٱللَّهِ رَبِّى وَرَبِّكُم ۚ مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ ۚ إِنَّ رَبِّى عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ'
# Voweled
permissible_stop_idhaar_shafawi_end ='قَدْ فَرَضَ ٱللَّهُ لَكُمْ تَحِلَّةَ أَيْمَٰنِكُمْ ۚ وَٱللَّهُ مَوْلَىٰكُمْ ۖ وَهُوَ ٱلْعَلِيمُ ٱلْحَكِيمُ'

# MEEM SAAKIN "POSSIBLE (PERMISSIBLE) STOP ۖ "
# Bare
possible_stop_ikhfa_shafawi_end = 'يَمُنُّونَ عَلَيْكَ أَنْ أَسْلَمُوا۟ ۖ قُل لَّا تَمُنُّوا۟ عَلَىَّ إِسْلَٰمَكُم ۖ بَلِ ٱللَّهُ يَمُنُّ عَلَيْكُمْ أَنْ هَدَىٰكُمْ لِلْإِيمَٰنِ إِن كُنتُمْ صَٰدِقِينَ'
possible_stop_idghaam_shafawi_end = 'أَمْ حَسِبْتُمْ أَن تَدْخُلُوا۟ ٱلْجَنَّةَ وَلَمَّا يَأْتِكُم مَّثَلُ ٱلَّذِينَ خَلَوْا۟ مِن قَبْلِكُم ۖ مَّسَّتْهُمُ ٱلْبَأْسَآءُ وَٱلضَّرَّآءُ وَزُلْزِلُوا۟ حَتَّىٰ يَقُولَ ٱلرَّسُولُ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ مَتَىٰ نَصْرُ ٱللَّهِ ۗ أَلَآ إِنَّ نَصْرَ ٱللَّهِ قَرِيبٌ'
# Voweled
possible_stop_idhaar_shafawi_end ='قَدْ فَرَضَ ٱللَّهُ لَكُمْ تَحِلَّةَ أَيْمَٰنِكُمْ ۚ وَٱللَّهُ مَوْلَىٰكُمْ ۖ وَهُوَ ٱلْعَلِيمُ ٱلْحَكِيمُ'

# MEEM SAAKIN "PREFERABLE STOP ۗ "
# Bare
preferable_stop_idghaam_shafawi_end = 'وَقَالُوا۟ لَوْ شَآءَ ٱلرَّحْمَٰنُ مَا عَبَدْنَٰهُم ۗ مَّا لَهُم بِذَٰلِكَ مِنْ عِلْمٍ ۖ إِنْ هُمْ إِلَّا يَخْرُصُونَ'
# Voweled
preferable_stop_idhaar_shafawi_end = 'أَلَآ إِنَّهُمْ فِى مِرْيَةٍ مِّن لِّقَآءِ رَبِّهِمْ ۗ أَلَآ إِنَّهُۥ بِكُلِّ شَىْءٍ مُّحِيطٌۢ'

# MEEM SAAKIN "LINKED STOPS ۛ  ۛ"
# Voweled
linked_stops_idhaar_shafawi_end = 'قَالَ فَإِنَّهَا مُحَرَّمَةٌ عَلَيْهِمْ ۛ أَرْبَعِينَ سَنَةً ۛ يَتِيهُونَ فِى ٱلْأَرْضِ ۚ فَلَا تَأْسَ عَلَى ٱلْقَوْمِ ٱلْفَٰسِقِينَ'

#MEEM SAAKIN "FORBIDDEN STOP ۙ "
# Voweled
forbidden_stop_idhaar_shafawi_end = 'ذَٰلِكَ بِأَنَّ ٱللَّهَ لَمْ يَكُ مُغَيِّرًا نِّعْمَةً أَنْعَمَهَا عَلَىٰ قَوْمٍ حَتَّىٰ يُغَيِّرُوا۟ مَا بِأَنفُسِهِمْ ۙ وَأَنَّ ٱللَّهَ سَمِيعٌ عَلِيمٌ'

class TestStopSigns(unittest.TestCase):
  # MEEM SAAKIN "MUST STOP ۘ "
  # Voweled
  def test_must_stop_idhaar_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_voweled_letter()
    self.assertEqual(must_stop_idhaar_shafawi_end[16 + stop_sign_adjustment], "ۘ")
    
  # MEEM SAAKIN "PERMISSIBLE STOP ۚ "
  # Bare
  def test_permissible_stop_ikhfa_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_bare_letter()
    self.assertEqual(permissible_stop_ikhfa_shafawi_end[59 + stop_sign_adjustment], "ۚ")

  def test_permissible_stop_idghaam_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_bare_letter()
    self.assertEqual(permissible_stop_idghaam_shafawi_end[49 + stop_sign_adjustment], "ۚ")
  
  # Voweled
  def test_permissible_stop_idhaar_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_voweled_letter()
    self.assertEqual(permissible_stop_idhaar_shafawi_end[48 + stop_sign_adjustment], "ۚ")

  # MEEM SAAKIN "POSSIBLE (PERMISSIBLE) STOP ۖ "
  # Bare
  def test_possible_stop_ikhfa_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_bare_letter()
    self.assertEqual(possible_stop_ikhfa_shafawi_end[78 + stop_sign_adjustment], "ۖ")

  def test_possible_stop_idghaam_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_bare_letter()
    self.assertEqual(possible_stop_idghaam_shafawi_end[101 + stop_sign_adjustment], "ۖ")
  
  # Voweled
  def test_possible_stop_idhaar_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_voweled_letter()
    self.assertEqual(possible_stop_idhaar_shafawi_end[73 + stop_sign_adjustment], "ۖ")


  # MEEM SAAKIN "PREFERABLE STOP ۗ "
  # Bare
  def test_preferable_stop_idghaam_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_bare_letter()
    self.assertEqual(preferable_stop_idghaam_shafawi_end[51 + stop_sign_adjustment], "ۗ")
  
  # Voweled
  def test_preferable_stop_idhaar_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_voweled_letter()
    self.assertEqual(preferable_stop_idhaar_shafawi_end[52 + stop_sign_adjustment], "ۗ")

  # MEEM SAAKIN "LINKED STOPS ۛ  ۛ"
  # Voweled
  def test_linked_stops_idhaar_shafawi_end_stop(self):
    stop_sign_adjustment = StopSigns().find_stop_sign_for_voweled_letter()
    self.assertEqual(linked_stops_idhaar_shafawi_end[37 + stop_sign_adjustment], "ۛ")

  #MEEM SAAKIN "FORBIDDEN STOP ۙ "
  # Voweled
  def test_forbidden_stop_idhaar_shafawi_end_stop(self):
    # idhaar_factory = MeemSaakinRuleFactory(8, 53, forbidden_stop_idhaar_shafawi_end)
    # voweled_meem_saakins = idhaar_factory._find_meem_saakin_with_sukoon_in_text()
    # print('*****************************************', voweled_meem_saakins)
    stop_sign_adjustment = StopSigns().find_stop_sign_for_voweled_letter()
    self.assertEqual(forbidden_stop_idhaar_shafawi_end[117 + stop_sign_adjustment], "ۙ")