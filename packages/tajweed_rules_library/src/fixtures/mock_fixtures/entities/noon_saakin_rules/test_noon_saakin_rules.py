import unittest
from src.entities.noon_saakin_rules.noon_saakin_rules import NoonSaakinRules

# NOON SAAKIN
idghaam_ghunnah_middle = "NO INSTANCE FOUND, IDHAAM GHUNNAH ALWAYS AT THE END"
idghaam_ghunnah_end = "وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ شَرًّا يَرَهُۥ"
idghaam_no_ghunnah_middle = "NO INSTANCE FOUND, IDHAAM NO GHUNNAH ALWAYS AT THE END"
idghaam_no_ghunnah_end = "وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ"
idhaar_middle = "مَّتَٰعًا لَّكُمْ وَلِأَنْعَٰمِكُمْ"
idhaar_end =  "خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ"
ikhfa_middle = "وَلَآ أَنتُمْ عَٰبِدُونَ مَآ أَعْبُدُ"
ikhfa_end = "ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ"
iqlab_middle = "كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ"
iqlab_end = "وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ"
bare_noon_end = "ٱلَّذِينَ هُمْ عَن"
voweled_noon_end = "خَلَقَ مِنْ"

# FATHA TANWEEN
ft_idghaam_ghunnah_end = "رَسُولٌ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًا مُّطَهَّرَةً"
ft_idghaam_ghunnah_ta_marboutah = "ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةً مَّرْضِيَّةً"
#---
ft_idghaam_no_ghunnah_end = "وَلَئِنْ أَرْسَلْنَا رِيحًا فَرَأَوْهُ مُصْفَرًّا لَّظَلُّوا۟ مِنۢ بَعْدِهِۦ يَكْفُرُونَ"
ft_idhaar_end = "يَٰوَيْلَتَىٰ لَيْتَنِى لَمْ أَتَّخِذْ فُلَانًا خَلِيلًا"
ft_ikhfa_end = "76|27|إِنَّ هَٰٓؤُلَآءِ يُحِبُّونَ ٱلْعَاجِلَةَ وَيَذَرُونَ وَرَآءَهُمْ يَوْمًا ثَقِيلًا"
ft_iqlab_end = "NO INSTANCE FOUND"
ft_fatha_tanween_end = "يَٰوَيْلَتَىٰ لَيْتَنِى لَمْ أَتَّخِذْ فُلَانًا خَلِيلًا"
ft_fatha_tanween_stop_end = "إِنَّ ٱلَّذِينَ ءَامَنُوا۟ ثُمَّ كَفَرُوا۟ ثُمَّ ءَامَنُوا۟ ثُمَّ كَفَرُوا۟ ثُمَّ ٱزْدَادُوا۟ كُفْرًا لَّمْ يَكُنِ ٱللَّهُ لِيَغْفِرَ لَهُمْ وَلَا لِيَهْدِيَهُمْ سَبِيلًۢا"

# DUMMAH & KASRA TANWEEN
dkt_idghaam_ghunnah_end = "وُجُوهٌ يَوْمَئِذٍ خَٰشِعَةٌ"
dkt_idghaam_no_ghunnah_end = "56|3|خَافِضَةٌ رَّافِعَةٌ"
dkt_idhaar_end = "74|9|فَذَٰلِكَ يَوْمَئِذٍ يَوْمٌ عَسِيرٌ"
dkt_ikhfa_end = "ٱلَّذِينَ هُمْ فِى غَمْرَةٍ سَاهُونَ"
dkt_iqlab_end_top = "مَّا خَلْقُكُمْ وَلَا بَعْثُكُمْ إِلَّا كَنَفْسٍ وَٰحِدَةٍ ۗ إِنَّ ٱللَّهَ سَمِيعٌۢ بَصِيرٌ"
dkt_iqlab_end_bottom = "كِرَامٍۭ بَرَرَةٍ"
dkt_kasra_dummah_tanween_end = "كِرَامٍۭ بَرَرَةٍ"


# NOON SAAKIN "MUST STOP ۘ "
# Tanween
must_stop_idghaam_tanween = 'إِنَّ ٱللَّهَ لَا يَسْتَحْىِۦٓ أَن يَضْرِبَ مَثَلًا مَّا بَعُوضَةً فَمَا فَوْقَهَا ۚ فَأَمَّا ٱلَّذِينَ ءَامَنُوا۟ فَيَعْلَمُونَ أَنَّهُ ٱلْحَقُّ مِن رَّبِّهِمْ ۖ وَأَمَّا ٱلَّذِينَ كَفَرُوا۟ فَيَقُولُونَ مَاذَآ أَرَادَ ٱللَّهُ بِهَٰذَا مَثَلًا ۘ يُضِلُّ بِهِۦ كَثِيرًا وَيَهْدِى بِهِۦ كَثِيرًا ۚ وَمَا يُضِلُّ بِهِۦٓ إِلَّا ٱلْفَٰسِقِينَ'

# NOON SAAKIN "PERMISSIBLE STOP ۚ "
# Tanween
permissible_stop_idghaam_tanween = 'خِتَٰمُهُۥ مِسْكٌ ۚ وَفِى ذَٰلِكَ فَلْيَتَنَافَسِ ٱلْمُتَنَٰفِسُونَ'
permissible_stop_idghaam_fatha_tanween = 'إِنَّ رَبَّكَ يَعْلَمُ أَنَّكَ تَقُومُ أَدْنَىٰ مِن ثُلُثَىِ ٱلَّيْلِ وَنِصْفَهُۥ وَثُلُثَهُۥ وَطَآئِفَةٌ مِّنَ ٱلَّذِينَ مَعَكَ ۚ وَٱللَّهُ يُقَدِّرُ ٱلَّيْلَ وَٱلنَّهَارَ ۚ عَلِمَ أَن لَّن تُحْصُوهُ فَتَابَ عَلَيْكُمْ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ ۚ عَلِمَ أَن سَيَكُونُ مِنكُم مَّرْضَىٰ ۙ وَءَاخَرُونَ يَضْرِبُونَ فِى ٱلْأَرْضِ يَبْتَغُونَ مِن فَضْلِ ٱللَّهِ ۙ وَءَاخَرُونَ يُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ ۖ فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنْهُ ۚ وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَأَقْرِضُوا۟ ٱللَّهَ قَرْضًا حَسَنًا ۚ وَمَا تُقَدِّمُوا۟ لِأَنفُسِكُم مِّنْ خَيْرٍ تَجِدُوهُ عِندَ ٱللَّهِ هُوَ خَيْرًا وَأَعْظَمَ أَجْرًا ۚ وَٱسْتَغْفِرُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ غَفُورٌ رَّحِيمٌۢ'

# NOON SAAKIN "POSSIBLE (PERMISSIBLE) STOP ۖ "
# Tanween
possible_stop_idghaam_ghunnah = 'يَوْمَ لَا تَمْلِكُ نَفْسٌ لِّنَفْسٍ شَيْـًٔا ۖ وَٱلْأَمْرُ يَوْمَئِذٍ لِّلَّهِ'

# NOON SAAKIN "PREFERABLE STOP ۗ "
# Tanween
preferable_stop_idghaam_ghunnah = 'وَأُخْرَىٰ تُحِبُّونَهَا ۖ نَصْرٌ مِّنَ ٱللَّهِ وَفَتْحٌ قَرِيبٌ ۗ وَبَشِّرِ ٱلْمُؤْمِنِينَ'

# MEEM SAAKIN "LINKED STOPS ۛ  ۛ"
# Tanween
linked_stops_idghaam_tanween = 'قَالَ فَإِنَّهَا مُحَرَّمَةٌ عَلَيْهِمْ ۛ أَرْبَعِينَ سَنَةً ۛ يَتِيهُونَ فِى ٱلْأَرْضِ ۚ فَلَا تَأْسَ عَلَى ٱلْقَوْمِ ٱلْفَٰسِقِينَ'

# MEEM SAAKIN "FORBIDDEN STOP ۙ "
# Tanween
forbidden_stop_idghaam_tanween = 'مَا جَعَلَ ٱللَّهُ مِنۢ بَحِيرَةٍ وَلَا سَآئِبَةٍ وَلَا وَصِيلَةٍ وَلَا حَامٍ ۙ وَلَٰكِنَّ ٱلَّذِينَ كَفَرُوا۟ يَفْتَرُونَ عَلَى ٱللَّهِ ٱلْكَذِبَ ۖ وَأَكْثَرُهُمْ لَا يَعْقِلُونَ'

# MEEM SAAKIN "MEEM OF IQLAB ۢ "
# Tanween
meem_iqlab_noon = 'كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ'
meem_iqlab_tanween_top = 'أَءِذَا مِتْنَا وَكُنَّا تُرَابًا ۖ ذَٰلِكَ رَجْعٌۢ بَعِيدٌ'
meem_iqlab_tanween_bottom = 'كِرَامٍۭ بَرَرَةٍ'

class TestNoonSaakinRules(unittest.TestCase):
  def setUp(self):
    self.noon_saakin_rules = NoonSaakinRules()
    
  def tearDown(self):
    del self.noon_saakin_rules
    
  def test_find_bare_noon_saakin_in_text_end(self):
    self.noon_saakin_rules.surah_number = 112
    self.noon_saakin_rules.ayah_number = 4
    self.noon_saakin_rules.ayah_text = idghaam_no_ghunnah_end
    
    indices = self.noon_saakin_rules._find_noon_saakin_in_text()
    self.assertListEqual(indices, [11])
    self.assertEqual(idghaam_no_ghunnah_end[11], "ن")

  def test_find_bare_noon_saakin_in_middle_text(self):
    self.noon_saakin_rules.surah_number = 109
    self.noon_saakin_rules.ayah_number = 5
    self.noon_saakin_rules.ayah_text = ikhfa_middle
    
    indices = self.noon_saakin_rules._find_noon_saakin_in_text()
    self.assertListEqual(indices, [9])
    self.assertEqual(ikhfa_middle[9], "ن")

  def test_find_noon_saakin_with_sukoon_in_text_end(self):
    self.noon_saakin_rules.surah_number = 96
    self.noon_saakin_rules.ayah_number = 2
    self.noon_saakin_rules.ayah_text = idhaar_end
    
    self.assertEqual(idhaar_end[22], "ْ")
    self.assertEqual(idhaar_end[21], "ن")

  def test_find_noon_saakin_with_sukoon_in_text_middle(self):
    self.noon_saakin_rules.surah_number = 80
    self.noon_saakin_rules.ayah_number = 32
    self.noon_saakin_rules.ayah_text =  idhaar_middle
    
    indices = self.noon_saakin_rules._find_noon_saakin_in_text()
    self.assertEqual(idhaar_middle[25], "ْ")
    self.assertEqual(idhaar_middle[24], "ن")

  def test_ignore_bare_noon_saakin_at_end(self):
    self.noon_saakin_rules.surah_number = 107
    self.noon_saakin_rules.ayah_number =  5
    self.noon_saakin_rules.ayah_text =  bare_noon_end
    
    indices = self.noon_saakin_rules._find_noon_saakin_in_text()
    self.assertEqual(len(indices), 0)

  def test_ignore_voweled_noon_saakin_at_end(self):
    self.noon_saakin_rules.surah_number = 96
    self.noon_saakin_rules.ayah_number = 2
    self.noon_saakin_rules.ayah_text = voweled_noon_end
    
    indices = self.noon_saakin_rules._find_noon_saakin_in_text()
    self.assertEqual(len(indices), 0)

  def test_find_dummah_kasra_tanween_in_text(self):
    self.noon_saakin_rules.surah_number = 88
    self.noon_saakin_rules.ayah_number = 2
    self.noon_saakin_rules.ayah_text = dkt_idghaam_ghunnah_end
    
    indices = self.noon_saakin_rules._find_tanween_base_in_text()
    self.assertListEqual(indices, [5, 16])
    self.assertEqual(dkt_idghaam_ghunnah_end[6], "ٌ")
    self.assertEqual(dkt_idghaam_ghunnah_end[5], "ه")
    self.assertEqual(dkt_idghaam_ghunnah_end[17], "ٍ")
    self.assertEqual(dkt_idghaam_ghunnah_end[16], "ذ")

  def test_ignore_dummah_kasra_tanween_at_end(self):
    self.noon_saakin_rules.surah_number = 80
    self.noon_saakin_rules.ayah_number = 6
    self.noon_saakin_rules.ayah_text = dkt_kasra_dummah_tanween_end
    
    indices = self.noon_saakin_rules._find_tanween_base_in_text()
    self.assertEqual(len(indices), 1)

  def test_find_fatha_tanween_in_text(self):
    self.noon_saakin_rules.surah_number = 25
    self.noon_saakin_rules.ayah_number = 28
    self.noon_saakin_rules.ayah_text =  ft_idhaar_end
    indices = self.noon_saakin_rules._find_tanween_base_in_text()
    
    self.assertListEqual(indices, [44])
    self.assertEqual(ft_idhaar_end[46], "ا")
    self.assertEqual(ft_idhaar_end[45], "ً")

  def test_ignore_alif_fatha_tanween_at_end(self):
    self.noon_saakin_rules.surah_number = 25
    self.noon_saakin_rules.ayah_number = 28
    self.noon_saakin_rules.ayah_text =  ft_fatha_tanween_end
    
    indices = self.noon_saakin_rules._find_tanween_base_in_text()
    self.assertEqual(len(indices), 1)
    
  def test_ignore_fatha_tanween_and_stop_at_end(self):
    self.noon_saakin_rules.surah_number = 4
    self.noon_saakin_rules.ayah_number = 137
    self.noon_saakin_rules.ayah_text = ft_fatha_tanween_stop_end
    
    indices = self.noon_saakin_rules._find_tanween_base_in_text()
    print(indices, '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    self.assertEqual(len(indices), 1)

  def test_ignore_fatha_tanween_on_ta_marbouta_at_end(self):
    self.noon_saakin_rules.surah_number = 98
    self.noon_saakin_rules.ayah_number = 2
    self.noon_saakin_rules.ayah_text = dkt_idghaam_ghunnah_end    
    
    indices = self.noon_saakin_rules._find_tanween_base_in_text()
    self.assertTrue(len(indices), 2)

  def test_is_ending_letter_an_idhaar_letter(self):
    self.noon_saakin_rules.surah_number = 96 
    self.noon_saakin_rules.ayah_number = 2
    self.noon_saakin_rules.ayah_text = idhaar_end
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_idhaar_letter(24))
    
    self.noon_saakin_rules.surah_number = 25
    self.noon_saakin_rules.ayah_number = 28
    self.noon_saakin_rules.ayah_text =  ft_idhaar_end
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_idhaar_letter(48))

  def test_is_ending_letter_an_idghaam_ghunnah_letter(self):
    self.noon_saakin_rules.surah_number = 99
    self.noon_saakin_rules.ayah_number = 8
    self.noon_saakin_rules.ayah_text = idghaam_ghunnah_end
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_idghaam_ghunnah_letter(6))
    
    self.noon_saakin_rules.surah_number = 88 
    self.noon_saakin_rules.ayah_number = 2
    self.noon_saakin_rules.ayah_text = dkt_idghaam_ghunnah_end
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_idghaam_ghunnah_letter(8))

  def test_is_ending_letter_an_idghaam_no_ghunnah_letter(self):
    self.noon_saakin_rules.surah_number = 112
    self.noon_saakin_rules.ayah_number = 4
    self.noon_saakin_rules.ayah_text = idghaam_no_ghunnah_end
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_idghaam_no_ghunnah_letter(13))
    
    self.noon_saakin_rules.surah_number = 30
    self.noon_saakin_rules.ayah_number = 51
    self.noon_saakin_rules.ayah_text = ft_idghaam_no_ghunnah_end
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_idghaam_no_ghunnah_letter(50))

  def test_is_ending_letter_an_ikhfa_letter(self):
    self.noon_saakin_rules.surah_number = 109
    self.noon_saakin_rules.ayah_number = 5
    self.noon_saakin_rules.ayah_text = ikhfa_middle
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_ikhfa_letter(10))
    
    self.noon_saakin_rules.surah_number = 51
    self.noon_saakin_rules.ayah_number = 11
    self.noon_saakin_rules.ayah_text = dkt_ikhfa_end
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_ikhfa_letter(28))
  
  def test_is_ending_letter_an_iqlab_letter(self):
    self.noon_saakin_rules.surah_number = 92
    self.noon_saakin_rules.ayah_number = 8
    self.noon_saakin_rules.ayah_text =iqlab_end
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_iqlab_letter(11, 14))
    
    self.noon_saakin_rules.surah_number = 31
    self.noon_saakin_rules.ayah_number = 28
    self.noon_saakin_rules.ayah_text = dkt_iqlab_end_top
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_iqlab_letter(81, 84))
    
    self.noon_saakin_rules.surah_number = 80
    self.noon_saakin_rules.ayah_number = 16 
    self.noon_saakin_rules.ayah_text = dkt_iqlab_end_bottom
    self.assertTrue(self.noon_saakin_rules._is_ending_letter_an_iqlab_letter(6, 9))


  def test_idghaam_ghunnah_end(self):
    self.noon_saakin_rules.surah_number = 99 
    self.noon_saakin_rules.ayah_number = 8
    self.noon_saakin_rules.ayah_text = idghaam_ghunnah_end
    
    map = self.noon_saakin_rules.get_all_rule_locations('idghaam_ghunnah')
    expectedRule = {
      'surah': 99,
      'ayah': 8,
      'start': 4,
      'end': 8
    }
  
    self.assertTrue(expectedRule in map)

  def test_idghaam_no_ghunnah_end(self):
    self.noon_saakin_rules.surah_number = 112
    self.noon_saakin_rules.ayah_number = 4
    self.noon_saakin_rules.ayah_text = idghaam_no_ghunnah_end
    
    map = self.noon_saakin_rules.get_all_rule_locations('idghaam_no_ghunnah')
    expectedMaps = [
      {
        'surah': 112,
        'ayah': 4,
        'start': 11,
        'end': 15
      }
    ]
    self.assertListEqual(map, expectedMaps)

  def test_idhaar_middle(self):
    self.noon_saakin_rules.surah_number = 80
    self.noon_saakin_rules.ayah_number = 32
    self.noon_saakin_rules.ayah_text =  idhaar_middle
    
    idhaar_map = self.noon_saakin_rules.get_all_rule_locations('idhaar')
    expectedMap = [
      {
      'surah': 80,
      'ayah': 32,
      'start': 24,
      'end': 28
      }
    ]
    self.assertListEqual(idhaar_map, expectedMap)

  def test_idhaar_end(self):
    self.noon_saakin_rules.surah_number = 96
    self.noon_saakin_rules.ayah_number = 2
    self.noon_saakin_rules.ayah_text = idhaar_end
    
    idhaar_map = self.noon_saakin_rules.get_all_rule_locations('idhaar')
    expectedMap = [
      {
      'surah': 96,
      'ayah': 2,
      'start': 21,
      'end': 26
      }
    ]
    self.assertListEqual(idhaar_map, expectedMap)

  def test_ikhfa_middle(self):
    self.noon_saakin_rules.surah_number = 109 
    self.noon_saakin_rules.ayah_number = 5
    self.noon_saakin_rules.ayah_text = ikhfa_middle
    
    ikhfa_map = self.noon_saakin_rules.get_all_rule_locations('ikhfa')
    expectedMap = [
      {
      'surah': 109,
      'ayah': 5,
      'start': 9,
      'end': 12
      }
    ]
    self.assertListEqual(ikhfa_map, expectedMap)

  def test_ikhfa_end(self):
    self.noon_saakin_rules.surah_number = 107
    self.noon_saakin_rules.ayah_number = 5
    self.noon_saakin_rules.ayah_text = ikhfa_end
    
    ikhfa_map = self.noon_saakin_rules.get_all_rule_locations('ikhfa')
    expectedMap = [
      {
      'surah': 107,
      'ayah': 5,
      'start': 17,
      'end': 21
      }
    ]
    self.assertListEqual(ikhfa_map, expectedMap)

  def test_iqlab_middle(self):
    self.noon_saakin_rules.surah_number = 104
    self.noon_saakin_rules.ayah_number = 4
    self.noon_saakin_rules.ayah_text = iqlab_middle
    
    iqlab_map = self.noon_saakin_rules.get_all_rule_locations('iqlab')
    expectedMaps = [
      {
        'surah': 104,
        'ayah': 4,
        'start': 13,
        'end': 17
      }
    ]
    self.assertListEqual(iqlab_map, expectedMaps)

  def test_iqlab_end(self):
    self.noon_saakin_rules.surah_number = 92
    self.noon_saakin_rules.ayah_number = 8
    self.noon_saakin_rules.ayah_text =iqlab_end
    
    iqlab_map = self.noon_saakin_rules.get_all_rule_locations('iqlab')
    expectedMaps = [
      {
        'surah': 92,
        'ayah': 8,
        'start': 11,
        'end': 16
      }
    ]
    self.assertListEqual(iqlab_map, expectedMaps)

  def test_ft_idghaam_ghunnah_end(self):
    self.noon_saakin_rules.surah_number = 98
    self.noon_saakin_rules.ayah_number = 2
    self.noon_saakin_rules.ayah_text = ft_idghaam_ghunnah_end 
    
    idghaam_map = self.noon_saakin_rules.get_all_rule_locations('idghaam_ghunnah')
    expectedRule = {
      'surah': 98,
      'ayah': 2,
      'start': 36,
      'end': 42
    }
    self.assertTrue(expectedRule in idghaam_map)

  def test_ft_idghaam_ghunnah_ta_marboutah(self):
    self.noon_saakin_rules.surah_number = 89
    self.noon_saakin_rules.ayah_number = 28
    self.noon_saakin_rules.ayah_text = ft_idghaam_ghunnah_ta_marboutah
    
    idghaam_map = self.noon_saakin_rules.get_all_rule_locations('idghaam_ghunnah')
    expectedMaps = [
      {
        'surah': 89,
        'ayah': 28,
        'start': 32,
        'end': 37
      }
    ]
    self.assertListEqual(idghaam_map, expectedMaps)

  def test_ft_idghaam_no_ghunnah_end(self):
    self.noon_saakin_rules.surah_number = 30
    self.noon_saakin_rules.ayah_number = 51
    self.noon_saakin_rules.ayah_text = ft_idghaam_no_ghunnah_end
    
    idghaam_map = self.noon_saakin_rules.get_all_rule_locations('idghaam_no_ghunnah')
    expectedMaps = [
      {
        'surah': 30,
        'ayah': 51,
        'start': 46,
        'end': 52
      }
    ]
    self.assertListEqual(idghaam_map, expectedMaps)

  # ------------------------------------------------------------------------------------------
  # NOON SAAKIN "MUST STOP ۘ "
  # Tanween
  def test_must_stop_idghaam_tanween(self):
    self.noon_saakin_rules.surah_number = 2
    self.noon_saakin_rules.ayah_number = 26
    self.noon_saakin_rules.ayah_text = must_stop_idghaam_tanween
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(244, 'idghaam_ghunnah')
    expectedMap = {
      'surah': 2,
      'ayah': 26,
      'start': 244,
      'end': 250
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # NOON SAAKIN "PERMISSIBLE STOP ۚ "
  # Tanween
  def test_permissible_stop_idghaam_tanween(self):
    self.noon_saakin_rules.surah_number = 83
    self.noon_saakin_rules.ayah_number = 26
    self.noon_saakin_rules.ayah_text = permissible_stop_idghaam_tanween
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(16, 'idghaam_ghunnah')
    expectedMap = {
      'surah': 83,
      'ayah': 26,
      'start': 16,
      'end': 22
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  def test_permissible_stop_idghaam_fatha_tanween(self):
    self.noon_saakin_rules.surah_number = 73
    self.noon_saakin_rules.ayah_number = 20
    self.noon_saakin_rules.ayah_text = permissible_stop_idghaam_fatha_tanween
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(550, 'idghaam_ghunnah')
    expectedMap = {
      'surah': 73,
      'ayah': 20,
      'start': 550,
      'end': 556
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # NOON SAAKIN "POSSIBLE (PERMISSIBLE) STOP ۖ "
  # Tanween
  def test_possible_stop_idghaam_ghunnah(self):
    self.noon_saakin_rules.surah_number = 82
    self.noon_saakin_rules.ayah_number = 19
    self.noon_saakin_rules.ayah_text = possible_stop_idghaam_ghunnah
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(44, 'idghaam_ghunnah')
    expectedMap = {
      'surah': 82,
      'ayah': 19,
      'start': 44,
      'end': 50
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # NOON SAAKIN "PREFERABLE STOP ۗ "
  # Tanween
  def test_preferable_stop_idghaam_ghunnah(self):
    self.noon_saakin_rules.surah_number = 61
    self.noon_saakin_rules.ayah_number = 13
    self.noon_saakin_rules.ayah_text = preferable_stop_idghaam_ghunnah
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(63, 'idghaam_ghunnah')
    expectedMap = {
      'surah': 61,
      'ayah': 13,
      'start': 63,
      'end': 69
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # NOON SAAKIN "LINKED STOPS ۛ  ۛ"
  # Tanween
  def test_linked_stops_idghaam_tanween(self):
    self.noon_saakin_rules.surah_number = 5
    self.noon_saakin_rules.ayah_number = 26
    self.noon_saakin_rules.ayah_text = linked_stops_idghaam_tanween
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(59, 'idghaam_ghunnah')
    expectedMap = {
      'surah': 5,
      'ayah': 26,
      'start': 59,
      'end': 65
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # NOON SAAKIN "FORBIDDEN STOP ۙ "
  # Tanween
  def test_forbidden_stop_idghaam_tanween(self):
    self.noon_saakin_rules.surah_number = 5
    self.noon_saakin_rules.ayah_number = 103
    self.noon_saakin_rules.ayah_text = forbidden_stop_idghaam_tanween
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(77, 'idghaam_ghunnah')
    expectedMap = {
      'surah': 5,
      'ayah': 103,
      'start': 77,
      'end': 83
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  # NOON SAAKIN "MEEM OF IQLAB ۢ "
  # Tanween
  def test_meem_iqlab_noon(self):
    self.noon_saakin_rules.surah_number = 104
    self.noon_saakin_rules.ayah_number = 4
    self.noon_saakin_rules.ayah_text = meem_iqlab_noon
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(13, 'iqlab')
    expectedMap = {
      'surah': 104,
      'ayah': 4,
      'start': 13,
      'end': 17
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  def test_meem_iqlab_tanween_top(self):
    self.noon_saakin_rules.surah_number = 50
    self.noon_saakin_rules.ayah_number = 3
    self.noon_saakin_rules.ayah_text =meem_iqlab_tanween_top
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(49, 'iqlab')
    expectedMap = {
      'surah': 50,
      'ayah': 3,
      'start': 49,
      'end': 54
    }
    self.assertDictEqual(idghaam_map, expectedMap)

  def test_meem_iqlab_tanween_bottom(self):
    self.noon_saakin_rules.surah_number = 80
    self.noon_saakin_rules.ayah_number = 16
    self.noon_saakin_rules.ayah_text = meem_iqlab_tanween_bottom
    
    idghaam_map = self.noon_saakin_rules._get_rule_location_details(6, 'iqlab')
    expectedMap = {
      'surah': 80,
      'ayah': 16,
      'start': 6,
      'end': 11
    }
    self.assertDictEqual(idghaam_map, expectedMap)