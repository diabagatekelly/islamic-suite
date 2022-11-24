import unittest
from src.entities.meem_saakin_rules.meem_saakin_rules import MeemSaakinRules

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

class TestMeemSaakinRules(unittest.TestCase):
  def setUp(self):
    self.meem_saakin_rules = MeemSaakinRules()
    
  def tearDown(self):
    del self.meem_saakin_rules
    
  def test_find_meem_saakin_in_text_bare(self):
    self.meem_saakin_rules.surah_number = 106
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= idghaam
    
    indices = self.meem_saakin_rules._find_meem_saakin_in_text()
    self.assertListEqual(indices, [19, 43])
    self.assertEqual(idghaam[19], "م")
    self.assertEqual(idghaam[43], "م")

  def test_find_meem_saakin_in_text_voweled_middle(self):
    self.meem_saakin_rules.surah_number = 111 
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= idhaar_middle
    
    indices = self.meem_saakin_rules._find_meem_saakin_in_text()
    self.assertListEqual(indices, [3])
    self.assertEqual(idhaar_middle[4], "ْ") # indices of sukoons
    self.assertEqual(idhaar_middle[3], "م") # ensure the sukoons are on meem

  def test_find_meem_saakin_in_text_voweled_end(self):
    self.meem_saakin_rules.surah_number = 111 
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= idhaar_end
    
    indices = self.meem_saakin_rules._find_meem_saakin_in_text()
    self.assertListEqual(indices, [4])
    self.assertEqual(idhaar_end[5], "ْ") # indices of sukoons
    self.assertEqual(idhaar_end[4], "م") # ensure the sukoons are on meem

  def test_ignore_bare_meem_when_last_letter(self):
    self.meem_saakin_rules.surah_number = 105 
    self.meem_saakin_rules.ayah_number = 4 
    self.meem_saakin_rules.ayah_text= bare_meem_end
    
    indices = self.meem_saakin_rules._find_meem_saakin_in_text()
    self.assertListEqual(indices, [])

  def test_ignore_voweled_meem_when_last_letter(self):
    self.meem_saakin_rules.surah_number = 112 
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= voweled_meem_end
    
    indices = self.meem_saakin_rules._find_meem_saakin_in_text()
    self.assertListEqual(indices, [])
  
  def test_is_ending_letter_an_idghaam_letter(self):
    self.meem_saakin_rules.surah_number = 106 
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= idghaam
    
    self.assertEqual(idghaam[21], "م")
    self.assertTrue(self.meem_saakin_rules._is_ending_letter_an_idghaam_letter(21))
    self.assertFalse(self.meem_saakin_rules._is_ending_letter_an_ikhfa_letter(21))
    self.assertFalse(self.meem_saakin_rules._is_ending_letter_an_idhaar_letter(21))

  def test_is_ending_letter_an_idhaar_letter(self):
    self.meem_saakin_rules.surah_number = 111
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= idhaar_middle
    
    self.assertNotEqual(idghaam[5], "م")
    self.assertNotEqual(idghaam[5], "ب")
    self.assertTrue(self.meem_saakin_rules._is_ending_letter_an_idhaar_letter(5))
    self.assertFalse(self.meem_saakin_rules._is_ending_letter_an_idghaam_letter(5))
    self.assertFalse(self.meem_saakin_rules._is_ending_letter_an_ikhfa_letter(5))

  def test_is_ending_letter_an_ikhfa_letter(self):
    self.meem_saakin_rules.surah_number = 105 
    self.meem_saakin_rules.ayah_number = 4 
    self.meem_saakin_rules.ayah_text= ikhfa
    
    self.assertEqual(ikhfa[11], "ب")
    self.assertTrue(self.meem_saakin_rules._is_ending_letter_an_ikhfa_letter(11))
    self.assertFalse(self.meem_saakin_rules._is_ending_letter_an_idghaam_letter(11))
    self.assertFalse(self.meem_saakin_rules._is_ending_letter_an_idhaar_letter(11))

  def test_get_all_rule_locations_ikkfa(self):
    self.meem_saakin_rules.surah_number = 105 
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= ikhfa
    
    map = self.meem_saakin_rules.get_all_rule_locations('ikhfa_shafawi')
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
    self.meem_saakin_rules.surah_number = 106
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= idghaam
    
    map = self.meem_saakin_rules.get_all_rule_locations('idghaam_shafawi')
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
    self.meem_saakin_rules.surah_number = 111
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= idhaar_middle
    
    map = self.meem_saakin_rules.get_all_rule_locations('idhaar_shafawi')
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
    self.meem_saakin_rules.surah_number = 112
    self.meem_saakin_rules.ayah_number = 4
    self.meem_saakin_rules.ayah_text= idhaar_end
    
    map = self.meem_saakin_rules.get_all_rule_locations('idhaar_shafawi')
    expectedMaps = [
      {
        'surah': 112,
        'ayah': 4,
        'start': 4,
        'end': 9
      }
    ]
    self.assertListEqual(map, expectedMaps)


  # TEST STOP SIGNS

  # MEEM SAAKIN "MUST STOP ۘ "
  # Voweled
  def test_must_stop_idhaar_shafawi_end(self):
    self.meem_saakin_rules.surah_number = 6
    self.meem_saakin_rules.ayah_number = 54
    self.meem_saakin_rules.ayah_text= must_stop_idhaar_shafawi_end
    
    idhaar_map = self.meem_saakin_rules._get_rule_location_details(16, 'idhaar_shafawi')
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
    self.meem_saakin_rules.surah_number = 80
    self.meem_saakin_rules.ayah_number = 43
    self.meem_saakin_rules.ayah_text= permissible_stop_ikhfa_shafawi_end
    
    ikhfa_map = self.meem_saakin_rules._get_rule_location_details(59, 'ikhfa_shafawi')
    expectedMap = {
      'surah': 80,
      'ayah': 43,
      'start': 59,
      'end': 65
    }
    self.assertDictEqual(ikhfa_map, expectedMap)

  def test_permissible_stop_idghaam_shafawi_end(self):
    self.meem_saakin_rules.surah_number = 11
    self.meem_saakin_rules.ayah_number = 56
    self.meem_saakin_rules.ayah_text= permissible_stop_idghaam_shafawi_end
    idghaam_map = self.meem_saakin_rules._get_rule_location_details(49, 'idghaam_shafawi')
    expectedMap = {
      'surah': 11,
      'ayah': 56,
      'start': 49,
      'end': 55
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # Voweled
  def test_must_stop_idhaar_shafawi_end(self):
    self.meem_saakin_rules.surah_number = 2
    self.meem_saakin_rules.ayah_number = 66
    self.meem_saakin_rules.ayah_text= permissible_stop_idhaar_shafawi_end
    idhaar_map = self.meem_saakin_rules._get_rule_location_details(48, 'idhaar_shafawi')
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
    self.meem_saakin_rules.surah_number = 17
    self.meem_saakin_rules.ayah_number = 49
    self.meem_saakin_rules.ayah_text= possible_stop_ikhfa_shafawi_end
    ikhfa_map = self.meem_saakin_rules._get_rule_location_details(78, 'ikhfa_shafawi')
    expectedMap = {
      'surah': 17,
      'ayah': 49,
      'start': 78,
      'end': 84
    }
    self.assertDictEqual(ikhfa_map, expectedMap)

  def test_possible_stop_idghaam_shafawi_end(self):
    self.meem_saakin_rules.surah_number = 2
    self.meem_saakin_rules.ayah_number = 214
    self.meem_saakin_rules.ayah_text= possible_stop_idghaam_shafawi_end
    idghaam_map = self.meem_saakin_rules._get_rule_location_details(101, 'idghaam_shafawi')
    expectedMap = {
      'surah': 2,
      'ayah': 214,
      'start': 101,
      'end': 107
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # Voweled
  def test_possible_stop_idhaar_shafawi_end(self):
    self.meem_saakin_rules.surah_number = 2
    self.meem_saakin_rules.ayah_number = 66
    self.meem_saakin_rules.ayah_text= possible_stop_idhaar_shafawi_end
    idhaar_map = self.meem_saakin_rules._get_rule_location_details(73, 'idhaar_shafawi')
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
    self.meem_saakin_rules.surah_number = 41
    self.meem_saakin_rules.ayah_number = 54 
    self.meem_saakin_rules.ayah_text= preferable_stop_idghaam_shafawi_end
    idghaam_map = self.meem_saakin_rules._get_rule_location_details(51, 'idghaam_shafawi')
    expectedMap = {
      'surah': 41,
      'ayah': 54,
      'start': 51,
      'end': 57
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # Voweled
  def test_preferable_stop_idhaar_shafawi_end(self):
    self.meem_saakin_rules.surah_number = 41
    self.meem_saakin_rules.ayah_number = 54
    self.meem_saakin_rules.ayah_text= preferable_stop_idhaar_shafawi_end
    idhaar_map = self.meem_saakin_rules._get_rule_location_details(52, 'idhaar_shafawi')
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
    self.meem_saakin_rules.surah_number = 5
    self.meem_saakin_rules.ayah_number = 26
    self.meem_saakin_rules.ayah_text= linked_stops_idhaar_shafawi_end
    idhaar_map = self.meem_saakin_rules._get_rule_location_details(37, 'idhaar_shafawi')
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
    self.meem_saakin_rules.surah_number = 8
    self.meem_saakin_rules.ayah_number = 53
    self.meem_saakin_rules.ayah_text= forbidden_stop_idhaar_shafawi_end
    idhaar_map = self.meem_saakin_rules._get_rule_location_details(117, 'idhaar_shafawi')
    expectedMap = {
      'surah': 8,
      'ayah': 53,
      'start': 117,
      'end': 124
    }
    self.assertDictEqual(idhaar_map, expectedMap)