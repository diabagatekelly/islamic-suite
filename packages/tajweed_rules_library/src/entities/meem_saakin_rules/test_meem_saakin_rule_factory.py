import unittest
from src.entities.meem_saakin_rules.meem_saakin_rule_factory import MeemSaakinRuleFactory

ikhfa = 'تَرْمِيهِم بِحِجَارَةٍ مِّن سِجِّيلٍ'
idghaam = 'ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍ وَءَامَنَهُم مِّنْ خَوْفٍۭ'
idhaar_middle = 'وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ' 
idhaar_end = 'وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ'

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