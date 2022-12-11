import unittest
from src.entities.madd_rules.madd_rules import MaddRules

madd_asli_alif = "مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ"
madd_asli_dagger_alif = "إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ"
madd_asli_full_yaa = "93|6|أَلَمْ يَجِدْكَ يَتِيمًا فَـَٔاوَىٰ"
madd_asli_yaa_no_dots = "104|9|فِى عَمَدٍ مُّمَدَّدَةٍۭ"
madd_asli_dagger_yaa = "2|22|ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًا وَٱلسَّمَآءَ بِنَآءً وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءً فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًا لَّكُمْ ۖ فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًا وَأَنتُمْ تَعْلَمُونَ"
madd_asli_dummah = "114|5|ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ"
madd_asli_dagger_wow = "111|4|وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ"
hamza_before_no_madd = "98|7|إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ"
hamza_after_no_madd = "111|2|مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ"
sukoon_after_no_madd = "109|4|وَلَآ أَنَا۠ عَابِدٌ مَّا عَبَدتُّمْ"


class TestMaddRules(unittest.TestCase):
  def setUp(self):
    self.madd_rules = MaddRules()
    
  def tearDown(self):
    del self.madd_rules
    
  def test_find_madd_asli_alif(self):
    self.madd_rules.surah_number = 114
    self.madd_rules.ayah_number = 6
    self.madd_rules.ayah_text = madd_asli_alif
    
    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [23])
    self.assertEqual(madd_asli_alif[23], "ا")
    
  def test_find_madd_asli_dagger_alif(self):
    self.madd_rules.surah_number = 103
    self.madd_rules.ayah_number = 2
    self.madd_rules.ayah_text = madd_asli_dagger_alif
    
    indices = self.madd_rules._find_madd_letter_in_text()
    self.assertListEqual(indices, [14, 22])
    self.assertEqual(madd_asli_dagger_alif[14], "ٰ")

    
  # def test_madd_asli_full_yaa(self):
  #   self.madd_rules.surah_number = 93
  #   self.madd_rules.ayah_number = 6
  #   self.madd_rules.ayah_text = madd_asli_full_yaa
    
  # def test_madd_asli_yaa_no_dots(self):
  #   self.madd_rules.surah_number = 104
  #   self.madd_rules.ayah_number = 9
  #   self.madd_rules.ayah_text = madd_asli_yaa_no_dots
    
  # def test_madd_asli_dagger_yaa(self):
  #   self.madd_rules.surah_number = 2
  #   self.madd_rules.ayah_number = 22
  #   self.madd_rules.ayah_text = madd_asli_dagger_yaa
    
  # def test_madd_asli_dummah(self):
  #   self.madd_rules.surah_number = 114
  #   self.madd_rules.ayah_number = 5
  #   self.madd_rules.ayah_text = madd_asli_dummah
    
  # def test_madd_asli_dagger_wow(self):
  #   self.madd_rules.surah_number = 111
  #   self.madd_rules.ayah_number = 4
  #   self.madd_rules.ayah_text = madd_asli_dagger_wow
    
  # def test_hamza_before_no_madd(self):
  #   self.madd_rules.surah_number = 98
  #   self.madd_rules.ayah_number = 7
  #   self.madd_rules.ayah_text = hamza_before_no_madd
    
  # def test_hamza_after_no_madd(self):
  #   self.madd_rules.surah_number = 111
  #   self.madd_rules.ayah_number = 2
  #   self.madd_rules.ayah_text = hamza_after_no_madd
    
  # def test_sukoon_after_no_madd(self):
  #   self.madd_rules.surah_number = 109
  #   self.madd_rules.ayah_number = 4
  #   self.madd_rules.ayah_text = sukoon_after_no_madd
    
  