import unittest
from use_cases.rule import Rule

class TestRule(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    surah_number = 23
    ayah_number = 96
    cls.noon_saakin_ayah_text = 'وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ هَمَزَاتِ الشَّيَاطِينِ'
    cls.noon_saakin_rule = Rule(surah_number, ayah_number, cls.noon_saakin_ayah_text)

    surah_number = 23
    ayah_number = 96
    cls.noon_saakin_text_no_space = 'وَقُل رَّبِّ أَعُوذُ بِكَ مِنْهَمَزَاتِ الشَّيَاطِينِ'
    cls.noon_saakin_no_space_rule = Rule(surah_number, ayah_number, cls.noon_saakin_text_no_space)

    surah_number = 23
    ayah_number = 96
    cls.noon_saakin_text_short_ayah = 'وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ'
    cls.noon_saakin_short_ayah_rule = Rule(surah_number, ayah_number, cls.noon_saakin_text_short_ayah)

    surah_number = 112
    ayah_number = 4
    cls.fatha_tanween_ayah_text = 'وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ'
    cls.fatha_tanween_rule = Rule(surah_number, ayah_number, cls.fatha_tanween_ayah_text)
  
    surah_number = 4
    ayah_number = 26
    cls.dummah_tanween_ayah_text = 'وَاللَّـهُ عَلِيمٌ حَكِيمٌ'
    cls.dummah_tanween_rule = Rule(surah_number, ayah_number, cls.dummah_tanween_ayah_text)
  
    surah_number = 113
    ayah_number = 5
    cls.kasra_tanween_ayah_text = 'وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ'
    cls.kasra_tanween_rule = Rule(surah_number, ayah_number, cls.kasra_tanween_ayah_text)
  
  
  def test_find_letter_in_text(cls):
    noon_indices = cls.noon_saakin_rule.find_letter_in_text('ن')
    cls.assertTrue(noon_indices, 1)
    cls.assertEqual(cls.noon_saakin_ayah_text[28], 'ن')
    cls.assertEqual(cls.noon_saakin_ayah_text[29], "ْ")

  def test_fatha_tanween_in_text(cls):
    fatha_tanween_indices = cls.fatha_tanween_rule.find_tanween_in_text('ًٌٍ')
    cls.assertTrue(fatha_tanween_indices, 1)
    cls.assertEqual(cls.fatha_tanween_ayah_text[24], 'ً')
    cls.assertEqual(cls.fatha_tanween_ayah_text[23], 'و')
    cls.assertEqual(cls.fatha_tanween_ayah_text[25], 'ا')

  def test_dummah_tanween_in_text(cls):
    dummah_tanween_indices = cls.dummah_tanween_rule.find_tanween_in_text('ًٌٍ')
    cls.assertTrue(dummah_tanween_indices, 1)
    cls.assertEqual(cls.dummah_tanween_ayah_text[17], 'ٌ')
    cls.assertEqual(cls.dummah_tanween_ayah_text[16], 'م')

  def test_kasra_tanween_in_text(cls):
    kasra_tanween_indices = cls.kasra_tanween_rule.find_tanween_in_text('ًٌٍ')
    cls.assertTrue(kasra_tanween_indices, 1)
    cls.assertEqual(cls.kasra_tanween_ayah_text[18], 'ٍ')
    cls.assertEqual(cls.kasra_tanween_ayah_text[17], 'د')
  
  def test_noon_saakin_followed_by_space(cls):
    noon_indices = cls.noon_saakin_rule.find_letter_in_text('ن')
    space = cls.noon_saakin_rule.is_letter_at_index_followed_by_space(noon_indices[0])
    cls.assertEqual(space, True)

  def test_noon_saakin_not_followed_by_space(cls):
    noon_indices_no_space = cls.noon_saakin_no_space_rule.find_letter_in_text('ن')
    space = cls.noon_saakin_no_space_rule.is_letter_at_index_followed_by_space(noon_indices_no_space[0])
    cls.assertEqual(space, False)

  def test_letter_after_noon_saakin_still_inside_ayah(cls):
    noon_indices = cls.noon_saakin_rule.find_letter_in_text('ن')
    next_letter = cls.noon_saakin_rule.is_letter_after_index_still_inside_ayah(noon_indices[0])
    cls.assertEqual(next_letter, True)

  def test_letter_after_noon_saakin_not_inside_ayah(cls):
    noon_indices_short_ayah = cls.noon_saakin_short_ayah_rule.find_letter_in_text('ن')
    cls.assertEqual(noon_indices_short_ayah[0]+1, len(cls.noon_saakin_text_short_ayah)-1)

  def test_noon_saakin_followed_by_idhaar_letter(cls):
    noon_indices = cls.noon_saakin_rule.find_letter_in_text('ن')
    idhaar = cls.noon_saakin_rule.is_letter_after_noon_idhaar_letter(noon_indices[0]+3)
    cls.assertEqual(idhaar, True)

  def test_noon_saakin_followed_by_idhaar_letter_no_space(cls):
    noon_indices_no_space = cls.noon_saakin_no_space_rule.find_letter_in_text('ن')
    idhaar = cls.noon_saakin_no_space_rule.is_letter_after_noon_idhaar_letter(noon_indices_no_space[0]+2)
    cls.assertEqual(idhaar, True)
    no_idhaar = cls.noon_saakin_no_space_rule.is_letter_after_noon_idhaar_letter(noon_indices_no_space[0]+3)
    cls.assertEqual(no_idhaar, False)
  
  def test_get_rule_location_details_for_letter_base(cls):
    noon_indices = cls.noon_saakin_rule.find_letter_in_text('ن')
    rule_info = cls.noon_saakin_rule.get_rule_location_details_for_letter_base(noon_indices[0])
    cls.assertEquals(rule_info, {"surah": 23, "ayah": 96, "start": 28, "end": 31})