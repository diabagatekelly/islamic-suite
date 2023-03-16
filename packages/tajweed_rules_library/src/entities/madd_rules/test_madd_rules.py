import unittest
from src.entities.madd_rules.madd_rules import MaddRules
from src.tajweed_rules_helpers.punctuation_marks import PunctuationMarks

# Madd base letters
madd_alif = "مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ"
madd_dagger_alif = "إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ"
madd_full_yaa = "أَلَمْ يَجِدْكَ يَتِيمًا فَـَٔاوَىٰ"
madd_yaa_no_dots = "فِى عَمَدٍ مُّمَدَّدَةٍۭ"
madd_dagger_yaa = "مَآءً فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًا لَّكُمْ"
madd_wow = "ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ"
madd_dagger_wow = "وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ"
alif_with_sukoon_no_madd = "وَلَآ أَنَا۠ عَابِدٌ مَّا عَبَدتُّمْ"
wow_with_sukoon_no_madd = "فَمَنِ ٱبْتَغَىٰ وَرَآءَ ذَٰلِكَ فَأُو۟لَٰٓئِكَ هُمُ ٱلْعَادُونَ"
yaa_with_sukoon_no_madd = "وَمَا جَعَلْنَا لِبَشَرٍ مِّن قَبْلِكَ ٱلْخُلْدَ ۖ أَفَإِي۟ن مِّتَّ فَهُمُ ٱلْخَٰلِدُونَ"
madd_leen_wow = "مَٰلِكِ يَوْمِ ٱلدِّينِ"
madd_leen_yaa = "فَوَيْلٌ لِّلْمُصَلِّينَ"


#Madd asli
asli_alif = "مَآءً فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًا لَّكُمْ"
asli_yaa = "كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَآ أَسْلَفْتُمْ فِى ٱلْأَيَّامِ ٱلْخَالِيَةِ"
asli_dummah = "قَالُوٓا۟ أَنُؤْمِنُ لَكَ وَٱتَّبَعَكَ ٱلْأَرْذَلُونَ"

# Madd Fari
asli_no_hamzah_before_alif = "أَن رَّءَاهُ ٱسْتَغْنَىٰٓ"
asli_no_hamzah_before_yaa = "قُلْ يَوْمَ ٱلْفَتْحِ لَا يَنفَعُ ٱلَّذِينَ كَفَرُوٓا۟ إِيمَٰنُهُمْ وَلَا هُمْ يُنظَرُونَ"
# asli_no_hamzah_before_wow = "98|4|وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ"

# asli_no_hamzah_after_alif = "111|2|مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ"
# asli_no_hamzah_after_yaa = "77|43|كُلُوا۟ وَٱشْرَبُوا۟ هَنِيٓـًٔۢا بِمَا كُنتُمْ تَعْمَلُونَ"
# asli_no_hamzah_after_wow = "26|111|قَالُوٓا۟ أَنُؤْمِنُ لَكَ وَٱتَّبَعَكَ ٱلْأَرْذَلُونَ"

# asli_no_sukoon_after_alif = "10|91|ءَآلْـَٰٔنَ وَقَدْ عَصَيْتَ قَبْلُ وَكُنتَ مِنَ ٱلْمُفْسِدِينَ"
# asli_no_sukoon_after_yaa = Found none
# asli_no_sukoon_after_woow = "39|64|قُلْ أَفَغَيْرَ ٱللَّهِ تَأْمُرُوٓنِّىٓ أَعْبُدُ أَيُّهَا ٱلْجَٰهِلُونَ"

# TODO: write tests for finding madd fari rule
# TODO: test madd fari rule dictionary




class TestMaddRules(unittest.TestCase):
  def setUp(self):
    self.madd_rules = MaddRules()
    
  def tearDown(self):
    del self.madd_rules
    
  def test_find_madd_alif(self):
    self.madd_rules.surah_number = 114
    self.madd_rules.ayah_number = 6
    self.madd_rules.ayah_text = madd_alif
    
    indices = self.madd_rules._find_madd_letters_in_text()
    self.assertListEqual(indices, [23])
    self.assertEqual(madd_alif[23], "ا")
    
  def test_find_madd_dagger_alif(self):
    self.madd_rules.surah_number = 103
    self.madd_rules.ayah_number = 2
    self.madd_rules.ayah_text = madd_dagger_alif
    
    indices = self.madd_rules._find_madd_letters_in_text()
    self.assertListEqual(indices, [14, 22])
    self.assertEqual(madd_dagger_alif[14], "ٰ")

    
  def test_madd_full_yaa(self):
    self.madd_rules.surah_number = 93
    self.madd_rules.ayah_number = 6
    self.madd_rules.ayah_text = madd_full_yaa
    
    indices = self.madd_rules._find_madd_letters_in_text()
    self.assertListEqual(indices, [20, 30, 34])
    self.assertEqual(madd_full_yaa[20], "ي")
    
  def test_madd_yaa_no_dots(self):
    self.madd_rules.surah_number = 104
    self.madd_rules.ayah_number = 9
    self.madd_rules.ayah_text = madd_yaa_no_dots
    
    indices = self.madd_rules._find_madd_letters_in_text()
    self.assertListEqual(indices, [2])
    self.assertEqual(madd_yaa_no_dots[2], "ى")
    
  def test_madd_dagger_yaa(self):
    self.madd_rules.surah_number = 2
    self.madd_rules.ayah_number = 22
    self.madd_rules.ayah_text = madd_dagger_yaa

    indices = self.madd_rules._find_madd_letters_in_text()
    self.assertListEqual(indices, [2, 22, 38])
    self.assertEqual(madd_dagger_yaa[22], "ۦ")
    
  def test_madd_wow(self):
    self.madd_rules.surah_number = 114
    self.madd_rules.ayah_number = 5
    self.madd_rules.ayah_text = madd_wow
    
    indices = self.madd_rules._find_madd_letters_in_text()
    self.assertListEqual(indices, [6, 21, 27, 36])
    self.assertEqual(madd_wow[27], "و")
    
  def test_madd_dagger_wow(self):
    self.madd_rules.surah_number = 111
    self.madd_rules.ayah_number = 4
    self.madd_rules.ayah_text = madd_dagger_wow
    
    indices = self.madd_rules._find_madd_letters_in_text()
    self.assertListEqual(indices, [13, 20])
    self.assertEqual(madd_dagger_wow[13], "ۥ")
    
  def test_alif_with_sukoon_no_madd(self):
    self.madd_rules.surah_number = 109
    self.madd_rules.ayah_number = 4
    self.madd_rules.ayah_text = alif_with_sukoon_no_madd

    indices = self.madd_rules._find_madd_letters_in_text()
    self.assertListEqual(indices, [4, 16, 25])
    self.assertEqual(alif_with_sukoon_no_madd[11], "ا")
    self.assertTrue(alif_with_sukoon_no_madd[12] in PunctuationMarks().sukoon)
    
  def test_wow_with_sukoon_no_madd(self):
    self.madd_rules.surah_number = 70
    self.madd_rules.ayah_number = 31
    self.madd_rules.ayah_text = wow_with_sukoon_no_madd
    indices = self.madd_rules._find_madd_letters_in_text()
    
    self.assertListEqual(indices, [15, 21, 28, 42, 59, 62])
    self.assertEqual(wow_with_sukoon_no_madd[38], "و")
    self.assertTrue(wow_with_sukoon_no_madd[39] in PunctuationMarks().sukoon)
  
  def test_yaa_with_sukoon_no_madd(self):
    self.madd_rules.surah_number = 21
    self.madd_rules.ayah_number = 34
    self.madd_rules.ayah_text = yaa_with_sukoon_no_madd
    indices = self.madd_rules._find_madd_letters_in_text()
    
    self.assertListEqual(indices, [4, 14, 80, 85])
    self.assertEqual(yaa_with_sukoon_no_madd[57], "ي")
    self.assertTrue(yaa_with_sukoon_no_madd[58] in PunctuationMarks().sukoon)
    
  def test_madd_leen_wow(self):
    self.madd_rules.surah_number = 1
    self.madd_rules.ayah_number = 4
    self.madd_rules.ayah_text = madd_leen_wow
    indices = self.madd_rules._find_madd_letters_in_text()
    
    self.assertListEqual(indices, [2, 10, 20])
    self.assertEqual(madd_leen_wow[10], "و")
    self.assertTrue(madd_leen_wow[11] in PunctuationMarks().sukoon)
    
  def test_madd_leen_yaa(self):
    self.madd_rules.surah_number = 107
    self.madd_rules.ayah_number = 4
    self.madd_rules.ayah_text = madd_leen_yaa
    indices = self.madd_rules._find_madd_letters_in_text()
    
    self.assertListEqual(indices, [4, 21])
    self.assertEqual(madd_leen_yaa[4], "ي")
    self.assertTrue(madd_leen_yaa[5] in PunctuationMarks().sukoon)
    
    
  # Madd Asli
  def test_asli_alif(self):
    self.madd_rules.surah_number = 2
    self.madd_rules.ayah_number = 22
    self.madd_rules.ayah_text = asli_alif
    

    madd_asli_alif_map = self.madd_rules.get_all_rule_locations('madd_asli')
    expectedMap = [
      {
      'surah': 2,
      'ayah': 22,
      'start': 20,
      'end': 24
      },
      {
      'surah': 2,
      'ayah': 22,
      'start': 36,
      'end': 39
      }]
    
    self.assertListEqual(madd_asli_alif_map, expectedMap)
    
  def test_asli_yaa(self):
    self.madd_rules.surah_number = 69
    self.madd_rules.ayah_number = 24
    self.madd_rules.ayah_text = asli_yaa
    
    print(asli_yaa[28], asli_yaa[27])
    

    madd_asli_yaa_map = self.madd_rules.get_all_rule_locations('madd_asli')
    expectedMap = [
      {
      'surah': 69,
      'ayah': 24,
      'start': 2,
      'end': 8
      },
      {
      'surah': 69,
      'ayah': 24,
      'start': 15,
      'end': 21
      },
      {
      'surah': 69,
      'ayah': 24,
      'start': 53,
      'end': 57
      },
      {
      'surah': 69,
      'ayah': 24,
      'start': 62,
      'end': 66
      },
      {
      'surah': 69,
      'ayah': 24,
      'start': 72,
      'end': 75
      }]
    
    self.assertListEqual(madd_asli_yaa_map, expectedMap)
    
    
  def test_asli_dummah(self):
    self.madd_rules.surah_number = 26
    self.madd_rules.ayah_number = 111
    self.madd_rules.ayah_text = asli_dummah

    madd_asli_dummah_map = self.madd_rules.get_all_rule_locations('madd_asli')
    expectedMap = [
      {
      'surah': 26,
      'ayah': 111,
      'start': 0,
      'end': 3
      },
      {
      'surah': 26,
      'ayah': 111,
      'start': 48,
      'end': 51
      }]
    
    self.assertListEqual(madd_asli_dummah_map, expectedMap)
    
# Madd Fari

  def test_asli_no_hamzah_before_alif(self):
    self.madd_rules.surah_number = 96
    self.madd_rules.ayah_number = 7
    self.madd_rules.ayah_text = asli_no_hamzah_before_alif

    asli_no_hamzah_before_alif_map = self.madd_rules.get_all_rule_locations('madd_fari')
    expectedMap = [
      {
      'surah': 96,
      'ayah': 7,
      'start': 7,
      'end': 10
      }]
    
    self.assertListEqual(asli_no_hamzah_before_alif_map, expectedMap)
    
  def test_asli_no_hamzah_before_yaa(self):
    self.madd_rules.surah_number = 32
    self.madd_rules.ayah_number = 29
    self.madd_rules.ayah_text = asli_no_hamzah_before_yaa
    
    asli_no_hamzah_before_yaa_map = self.madd_rules.get_all_rule_locations('madd_fari')
    expectedMap = [
      {
        'surah': 32,
        'ayah': 29,
        'start': 48,
        'end': 55
      },
      {
        'surah': 32,
        'ayah': 29,
        'start': 55,
        'end': 58
      }]
    
    self.assertListEqual(asli_no_hamzah_before_yaa_map, expectedMap)
 
  