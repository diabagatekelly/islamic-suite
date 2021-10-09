import unittest
from use_cases.mapper import Mapper

class TestMapper(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    surah_number = 2
    ayah_number = 7
    cls.multiple_idhaar_rules_in_text = '‏خَتَمَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ وَعَلَىٰ سَمْعِهِمْ ۖ وَعَلَىٰٓ أَبْصَرِهِمْ غِشَوَةٌۭ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌۭ'
    cls.multiple_idhaar_rules = Mapper(surah_number, ayah_number, cls.multiple_idhaar_rules_in_text)

    surah_number = 23
    ayah_number = 96
    cls.noon_saakin_ayah_text = 'وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ هَمَزَاتِ الشَّيَاطِينِ'
    cls.noon_saakin_rule = Mapper(surah_number, ayah_number, cls.noon_saakin_ayah_text)

    surah_number = 108
    ayah_number = 2
    cls.noon_saakin_text_no_space = 'فَصَلِّ لِرَبِّكَ وَانۡحَرۡ'
    cls.noon_saakin_no_space_rule = Mapper(surah_number, ayah_number, cls.noon_saakin_text_no_space)

    surah_number = 23
    ayah_number = 96
    cls.noon_saakin_text_short_ayah = 'وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ'
    cls.noon_saakin_short_ayah_rule = Mapper(surah_number, ayah_number, cls.noon_saakin_text_short_ayah)

    surah_number = 112
    ayah_number = 4
    cls.fatha_tanween_ayah_text = 'وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ'
    cls.fatha_tanween_rule = Mapper(surah_number, ayah_number, cls.fatha_tanween_ayah_text)
  
    surah_number = 4
    ayah_number = 26
    cls.dummah_tanween_ayah_text = 'وَاللَّـهُ عَلِيمٌ حَكِيمٌ'
    cls.dummah_tanween_rule = Mapper(surah_number, ayah_number, cls.dummah_tanween_ayah_text)
  
    surah_number = 113
    ayah_number = 5
    cls.kasra_tanween_ayah_text = 'وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ'
    cls.kasra_tanween_rule = Mapper(surah_number, ayah_number, cls.kasra_tanween_ayah_text)

  def test_get_all_rule_locations(cls):
    all_rule_locations = cls.multiple_idhaar_rules.get_all_rule_locations('م')
    cls.assertEqual(all_rule_locations, [
      {'surah': 2, 'ayah': 7, 'start': 46,'end': 48},
      {'surah': 2, 'ayah': 7, 'start': 77,'end': 80},
      {'surah': 2, 'ayah': 7, 'start': 98,'end': 101}
    ])

  def test_get_rule_location_details(cls):
    noon_indices = cls.noon_saakin_rule.get_rule_location_details(29)
    cls.assertEqual(noon_indices, {'surah': 23, 'ayah': 96, 'start': 28,'end': 31})

  def test_find_letter_in_text(cls):
    noon_indices = cls.noon_saakin_rule.find_in_text('ن')
    cls.assertTrue(noon_indices, 1)
    cls.assertEqual(cls.noon_saakin_ayah_text[28], 'ن')
    cls.assertEqual(cls.noon_saakin_ayah_text[29], "ْ")

  def test_fatha_tanween_in_text(cls):
    fatha_tanween_indices = cls.fatha_tanween_rule.find_in_text('ًٌٍ')
    cls.assertTrue(fatha_tanween_indices, 1)
    cls.assertEqual(cls.fatha_tanween_ayah_text[24], 'ً')
    cls.assertEqual(cls.fatha_tanween_ayah_text[23], 'و')
    cls.assertEqual(cls.fatha_tanween_ayah_text[25], 'ا')

  def test_dummah_tanween_in_text(cls):
    dummah_tanween_indices = cls.dummah_tanween_rule.find_in_text('ًٌٍ')
    cls.assertTrue(dummah_tanween_indices, 1)
    cls.assertEqual(cls.dummah_tanween_ayah_text[17], 'ٌ')
    cls.assertEqual(cls.dummah_tanween_ayah_text[16], 'م')

  def test_kasra_tanween_in_text(cls):
    kasra_tanween_indices = cls.kasra_tanween_rule.find_in_text('ًٌٍ')
    cls.assertTrue(kasra_tanween_indices, 1)
    cls.assertEqual(cls.kasra_tanween_ayah_text[18], 'ٍ')
    cls.assertEqual(cls.kasra_tanween_ayah_text[17], 'د')
  
  def test_skipping_noon_saakin_at_end_of_ayah(cls):
    noon_indices_short_ayah = cls.noon_saakin_short_ayah_rule.find_in_text('ن')
    cls.assertEqual(len(noon_indices_short_ayah), 0)

  def test_is_ending_letter_an_idhaar_letter(cls):
    non_idhaar_letter = cls.noon_saakin_rule.is_ending_letter_an_idhaar_letter(28)
    cls.assertEqual(non_idhaar_letter, False)
    
    idhaar_letter = cls.noon_saakin_rule.is_ending_letter_an_idhaar_letter(31)
    cls.assertEqual(idhaar_letter, True)

  def test_is_rule_at_end_of_a_word_and_fatha_tanween(cls):
    fatha_tanween = cls.fatha_tanween_rule.is_rule_at_end_of_a_word_and_fatha_tanween(23)
    cls.assertEqual(fatha_tanween, True)

    fatha_tanween = cls.dummah_tanween_rule.is_rule_at_end_of_a_word_and_fatha_tanween(16)
    cls.assertEqual(fatha_tanween, False)
  
  def test_is_non_fatha_tanween_rule_at_end_of_a_word(cls):
    non_fatha_tanween = cls.dummah_tanween_rule.is_non_fatha_tanween_rule_at_end_of_a_word(16)
    cls.assertEqual(non_fatha_tanween, True)

    non_fatha_tanween = cls.fatha_tanween_rule.is_non_fatha_tanween_rule_at_end_of_a_word(23)
    cls.assertEqual(non_fatha_tanween, False)

  def test_get_ending_letter_index(cls):
    fatha_tanween_at_end = cls.fatha_tanween_rule.get_ending_letter_index(23)
    cls.assertEqual(fatha_tanween_at_end, 27)
    noon_at_end = cls.noon_saakin_rule.get_ending_letter_index(28)
    cls.assertEqual(noon_at_end, 31)
    noon_in_middle = cls.noon_saakin_no_space_rule.get_ending_letter_index(21)
    cls.assertEqual(noon_in_middle, 23)