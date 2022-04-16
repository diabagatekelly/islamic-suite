import unittest
from src.entities.meem_saakin_rules.meem_saakin_rule_factory import MeemSaakinRuleFactory

ikhfa = 'تَرْمِيهِم بِحِجَارَةٍ مِّن سِجِّيلٍ'
idghaam = 'ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍ وَءَامَنَهُم مِّنْ خَوْفٍۭ'
idhaar_middle = 'وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ' 
idhaar_end = 'وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ'
bare_meem_end = 'تَرْمِيهِم'
voweled_meem_end = 'وَلَمْ'

# MEEM SAAKIN "MUST STOP ۘ "
#Voweled
must_stop_idhaar_shafawi_end = 'فَتَوَلَّ عَنْهُمْ ۘ يَوْمَ يَدْعُ ٱلدَّاعِ إِلَىٰ شَىْءٍ نُّكُرٍ'

# MEEM SAAKIN "PERMISSIBLE STOP ۚ "
# Bare
permissible_stop_ikhfa_shafawi_end = 'أَمْ يَحْسَبُونَ أَنَّا لَا نَسْمَعُ سِرَّهُمْ وَنَجْوَىٰهُم ۚ بَلَىٰ وَرُسُلُنَا لَدَيْهِمْ يَكْتُبُونَ'
permissible_stop_idghaam_shafawi_end = 'إِنِّى تَوَكَّلْتُ عَلَى ٱللَّهِ رَبِّى وَرَبِّكُم ۚ مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ ۚ إِنَّ رَبِّى عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ'
#Voweled
permissible_stop_idhaar_shafawi_end ='قَدْ فَرَضَ ٱللَّهُ لَكُمْ تَحِلَّةَ أَيْمَٰنِكُمْ ۚ وَٱللَّهُ مَوْلَىٰكُمْ ۖ وَهُوَ ٱلْعَلِيمُ ٱلْحَكِيمُ'

# MEEM SAAKIN "POSSIBLE (PERMISSIBLE) STOP ۖ "
# Bare
possible_stop_ikhfa_shafawi_end = 'يَمُنُّونَ عَلَيْكَ أَنْ أَسْلَمُوا۟ ۖ قُل لَّا تَمُنُّوا۟ عَلَىَّ إِسْلَٰمَكُم ۖ بَلِ ٱللَّهُ يَمُنُّ عَلَيْكُمْ أَنْ هَدَىٰكُمْ لِلْإِيمَٰنِ إِن كُنتُمْ صَٰدِقِينَ'
possible_stop_idghaam_shafawi_end = 'أَمْ حَسِبْتُمْ أَن تَدْخُلُوا۟ ٱلْجَنَّةَ وَلَمَّا يَأْتِكُم مَّثَلُ ٱلَّذِينَ خَلَوْا۟ مِن قَبْلِكُم ۖ مَّسَّتْهُمُ ٱلْبَأْسَآءُ وَٱلضَّرَّآءُ وَزُلْزِلُوا۟ حَتَّىٰ يَقُولَ ٱلرَّسُولُ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ مَتَىٰ نَصْرُ ٱللَّهِ ۗ أَلَآ إِنَّ نَصْرَ ٱللَّهِ قَرِيبٌ'
#Voweled
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

class TestMeemSaakinRuleFactory(unittest.TestCase):
  def test_find_bare_meem_saakin_in_text(self):
    idghaam_factory = MeemSaakinRuleFactory(106, 4, idghaam)
    indices = idghaam_factory._find_bare_meem_saakin_in_text()
    self.assertListEqual(indices, [19, 43])
    self.assertEqual(idghaam[19], "م")
    self.assertEqual(idghaam[43], "م")

  def test_find_meem_saakin_with_sukoon_in_text(self):
    idhaar_factory = MeemSaakinRuleFactory(111, 4, idhaar_middle)
    indices = idhaar_factory._find_meem_saakin_with_sukoon_in_text()
    self.assertListEqual(indices, [4])
    self.assertEqual(idhaar_middle[4], "ْ") # indices of sukoons
    self.assertEqual(idhaar_middle[3], "م") # ensure the sukoons are on meem
  
  def test_is_ending_letter_an_idghaam_letter(self):
    idghaam_factory = MeemSaakinRuleFactory(106, 4, idghaam)
    self.assertEqual(idghaam[21], "م")
    self.assertTrue(idghaam_factory._is_ending_letter_an_idghaam_letter(21))
    self.assertFalse(idghaam_factory._is_ending_letter_an_ikhfa_letter(21))
    self.assertFalse(idghaam_factory._is_ending_letter_an_idhaar_letter(21))

  def test_is_ending_letter_an_idhaar_letter(self):
    idhaar_factory = MeemSaakinRuleFactory(111, 4, idhaar_middle)
    self.assertNotEqual(idghaam[5], "م")
    self.assertNotEqual(idghaam[5], "ب")
    self.assertTrue(idhaar_factory._is_ending_letter_an_idhaar_letter(5))
    self.assertFalse(idhaar_factory._is_ending_letter_an_idghaam_letter(5))
    self.assertFalse(idhaar_factory._is_ending_letter_an_ikhfa_letter(5))

  def test_is_meem_saakin_at_end_of_a_word(self):
    idhaar_factory = MeemSaakinRuleFactory(111, 4, idhaar_middle)
    self.assertFalse(idhaar_factory._is_meem_saakin_at_end_of_a_word(3))

  def test_is_ending_letter_an_ikhfa_letter(self):
    ikhfa_factory = MeemSaakinRuleFactory(105, 4, ikhfa)
    self.assertEqual(ikhfa[11], "ب")
    self.assertTrue(ikhfa_factory._is_ending_letter_an_ikhfa_letter(11))
    self.assertFalse(ikhfa_factory._is_ending_letter_an_idghaam_letter(11))
    self.assertFalse(ikhfa_factory._is_ending_letter_an_idhaar_letter(11))

  def test_get_all_rule_locations_ikkfa(self):
    ikhfa_factory = MeemSaakinRuleFactory(105, 4, ikhfa)
    map = ikhfa_factory.get_all_rule_locations('bare', 'ikhfa')
    expectedMaps = [
      {
        'surah': 105,
        'ayah': 4,
        'start': 9,
        'end': 13
      }
    ]
    self.assertListEqual(map, expectedMaps)

  def test_get_all_rule_locations_idghaam(self):
    idghaam_factory = MeemSaakinRuleFactory(106, 4, idghaam)
    map = idghaam_factory.get_all_rule_locations('bare', 'idghaam')
    expectedMaps = [
      {
        'surah': 106,
        'ayah': 4,
        'start': 19,
        'end': 23
      },
      {
        'surah': 106,
        'ayah': 4,
        'start': 43,
        'end': 47
      }
    ]
    self.assertListEqual(map, expectedMaps)

  def test_get_all_rule_locations_idhaar_middle(self):
    idhaar_factory = MeemSaakinRuleFactory(111, 4, idhaar_middle)
    map = idhaar_factory.get_all_rule_locations('with_sukoon', 'idhaar')
    expectedMaps = [
      {
        'surah': 111,
        'ayah': 4,
        'start': 3,
        'end': 7
      }
    ]
    self.assertListEqual(map, expectedMaps)

  def test_get_all_rule_locations_idhaar_end(self):
    idhaar_factory = MeemSaakinRuleFactory(112, 4, idhaar_end)
    map = idhaar_factory.get_all_rule_locations('with_sukoon', 'idhaar')
    expectedMaps = [
      {
        'surah': 112,
        'ayah': 4,
        'start': 4,
        'end': 9
      }
    ]
    self.assertListEqual(map, expectedMaps)

  def test_ignore_bare_meem_when_last_letter(self):
    bare_factory = MeemSaakinRuleFactory(105, 4, bare_meem_end)
    indices = bare_factory._find_bare_meem_saakin_in_text()
    self.assertListEqual(indices, [])

  def test_ignore_voweled_meem_when_last_letter(self):
    voweled_factory = MeemSaakinRuleFactory(112, 4, voweled_meem_end)
    indices = voweled_factory._find_meem_saakin_with_sukoon_in_text()
    self.assertListEqual(indices, [])


  # TEST STOP SIGNS

  # MEEM SAAKIN "MUST STOP ۘ "
  # Voweled
  def test_must_stop_idhaar_shafawi_end(self):
    idhaar_factory = MeemSaakinRuleFactory(6, 54, must_stop_idhaar_shafawi_end)
    idhaar_map = idhaar_factory._get_rule_location_details(17, 'with_sukoon', 'idhaar')
    expectedMap = {
      'surah': 6,
      'ayah': 54,
      'start': 16,
      'end': 23
    }
    self.assertDictEqual(idhaar_map, expectedMap)

  # MEEM SAAKIN "PERMISSIBLE STOP ۚ "
  # Bare
  def test_permissible_stop_ikhfa_shafawi_end(self):
    ikhfa_factory = MeemSaakinRuleFactory(80, 43, permissible_stop_ikhfa_shafawi_end)
    ikhfa_map = ikhfa_factory._get_rule_location_details(59, 'bare', 'ikhfa')
    expectedMap = {
      'surah': 80,
      'ayah': 43,
      'start': 59,
      'end': 65
    }
    self.assertDictEqual(ikhfa_map, expectedMap)

  def test_permissible_stop_idghaam_shafawi_end(self):
    idghaam_factory = MeemSaakinRuleFactory(11, 56, permissible_stop_idghaam_shafawi_end)
    idghaam_map = idghaam_factory._get_rule_location_details(49, 'bare', 'idghaam')
    expectedMap = {
      'surah': 11,
      'ayah': 56,
      'start': 49,
      'end': 55
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # Voweled
  def test_must_stop_idhaar_shafawi_end(self):
    idhaar_factory = MeemSaakinRuleFactory(2, 66, permissible_stop_idhaar_shafawi_end)
    idhaar_map = idhaar_factory._get_rule_location_details(49, 'with_sukoon', 'idhaar')
    expectedMap = {
      'surah': 2,
      'ayah': 66,
      'start': 48,
      'end': 55
    }
    self.assertDictEqual(idhaar_map, expectedMap)

  # MEEM SAAKIN "POSSIBLE (PERMISSIBLE) STOP ۖ "
  # Bare
  def test_possible_stop_ikhfa_shafawi_end(self):
    ikhfa_factory = MeemSaakinRuleFactory(17, 49, possible_stop_ikhfa_shafawi_end)
    ikhfa_map = ikhfa_factory._get_rule_location_details(78, 'bare', 'ikhfa')
    expectedMap = {
      'surah': 17,
      'ayah': 49,
      'start': 78,
      'end': 84
    }
    self.assertDictEqual(ikhfa_map, expectedMap)

  def test_possible_stop_idghaam_shafawi_end(self):
    idghaam_factory = MeemSaakinRuleFactory(2, 214, possible_stop_idghaam_shafawi_end)
    idghaam_map = idghaam_factory._get_rule_location_details(101, 'bare', 'idghaam')
    expectedMap = {
      'surah': 2,
      'ayah': 214,
      'start': 101,
      'end': 107
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # Voweled
  def test_possible_stop_idhaar_shafawi_end(self):
    idhaar_factory = MeemSaakinRuleFactory(2, 66, possible_stop_idhaar_shafawi_end)
    idhaar_map = idhaar_factory._get_rule_location_details(74, 'with_sukoon', 'idhaar')
    expectedMap = {
      'surah': 2,
      'ayah': 66,
      'start': 73,
      'end': 80
    }
    self.assertDictEqual(idhaar_map, expectedMap)
  

  # MEEM SAAKIN "PREFERABLE STOP ۗ "
  # Bare
  def test_preferable_stop_idghaam_shafawi_end(self):
    idghaam_factory = MeemSaakinRuleFactory(41, 54, preferable_stop_idghaam_shafawi_end)
    idghaam_map = idghaam_factory._get_rule_location_details(51, 'bare', 'idghaam')
    expectedMap = {
      'surah': 41,
      'ayah': 54,
      'start': 51,
      'end': 57
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # Voweled
  def test_preferable_stop_idhaar_shafawi_end(self):
    idhaar_factory = MeemSaakinRuleFactory(41, 54, preferable_stop_idhaar_shafawi_end)
    idhaar_map = idhaar_factory._get_rule_location_details(53, 'with_sukoon', 'idhaar')
    expectedMap = {
      'surah': 41,
      'ayah': 54,
      'start': 52,
      'end': 59
    }
    self.assertDictEqual(idhaar_map, expectedMap)

  # MEEM SAAKIN "LINKED STOPS ۛ  ۛ"
  # Voweled
  def test_linked_stops_idhaar_shafawi_end(self):
    idhaar_factory = MeemSaakinRuleFactory(5, 26, linked_stops_idhaar_shafawi_end)
    idhaar_map = idhaar_factory._get_rule_location_details(38, 'with_sukoon', 'idhaar')
    expectedMap = {
      'surah': 5,
      'ayah': 26,
      'start': 37,
      'end': 44
    }
    self.assertDictEqual(idhaar_map, expectedMap)

  #MEEM SAAKIN "FORBIDDEN STOP ۙ "
  # Voweled
  def test_forbidden_stop_idhaar_shafawi_end(self):
    idhaar_factory = MeemSaakinRuleFactory(8, 53, forbidden_stop_idhaar_shafawi_end)
    idhaar_map = idhaar_factory._get_rule_location_details(118, 'with_sukoon', 'idhaar')
    expectedMap = {
      'surah': 8,
      'ayah': 53,
      'start': 117,
      'end': 124
    }
    self.assertDictEqual(idhaar_map, expectedMap)