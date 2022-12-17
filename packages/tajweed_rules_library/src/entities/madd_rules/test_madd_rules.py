import unittest
from src.entities.madd_rules.madd_rules import MaddRules

madd_alif = "مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ"
madd_dagger_alif = "إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ"
madd_full_yaa = "أَلَمْ يَجِدْكَ يَتِيمًا فَـَٔاوَىٰ"
madd_yaa_no_dots = "فِى عَمَدٍ مُّمَدَّدَةٍۭ"
madd_dagger_yaa = "مَآءً فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًا لَّكُمْ"
madd_wow = "ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ"
madd_dagger_wow = "وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ"
# hamza_before_no_madd = "أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ"
# hamza_after_no_madd = "111|2|مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ"
sukoon_after_no_madd = "وَلَآ أَنَا۠ عَابِدٌ مَّا عَبَدتُّمْ"


class TestMaddRules(unittest.TestCase):
  def setUp(self):
    self.madd_rules = MaddRules()
    
  def tearDown(self):
    del self.madd_rules
    
  def test_find_madd_alif(self):
    self.madd_rules.surah_number = 114
    self.madd_rules.ayah_number = 6
    self.madd_rules.ayah_text = madd_alif
    
    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [23])
    self.assertEqual(madd_alif[23], "ا")
    
  def test_find_madd_dagger_alif(self):
    self.madd_rules.surah_number = 103
    self.madd_rules.ayah_number = 2
    self.madd_rules.ayah_text = madd_dagger_alif
    
    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [14, 22])
    self.assertEqual(madd_dagger_alif[14], "ٰ")

    
  def test_madd_full_yaa(self):
    self.madd_rules.surah_number = 93
    self.madd_rules.ayah_number = 6
    self.madd_rules.ayah_text = madd_full_yaa
    
    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [20, 23, 30, 34])
    self.assertEqual(madd_full_yaa[20], "ي")
    
  def test_madd_yaa_no_dots(self):
    self.madd_rules.surah_number = 104
    self.madd_rules.ayah_number = 9
    self.madd_rules.ayah_text = madd_yaa_no_dots
    
    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [2])
    self.assertEqual(madd_yaa_no_dots[2], "ى")
    
  def test_madd_dagger_yaa(self):
    self.madd_rules.surah_number = 2
    self.madd_rules.ayah_number = 22
    self.madd_rules.ayah_text = madd_dagger_yaa

    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [2, 22, 38, 48])
    self.assertEqual(madd_dagger_yaa[22], "ۦ")
    
  def test_madd_wow(self):
    self.madd_rules.surah_number = 114
    self.madd_rules.ayah_number = 5
    self.madd_rules.ayah_text = madd_wow
    
    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [6, 21, 27, 36])
    self.assertEqual(madd_wow[27], "و")
    
  def test_madd_dagger_wow(self):
    self.madd_rules.surah_number = 111
    self.madd_rules.ayah_number = 4
    self.madd_rules.ayah_text = madd_dagger_wow
    
    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [13, 20])
    self.assertEqual(madd_dagger_wow[13], "ۥ")
    
  def test_sukoon_after_no_madd(self):
    self.madd_rules.surah_number = 109
    self.madd_rules.ayah_number = 4
    self.madd_rules.ayah_text = sukoon_after_no_madd

    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [4, 16, 25])
    self.assertEqual(sukoon_after_no_madd[11], "ا")
    
  