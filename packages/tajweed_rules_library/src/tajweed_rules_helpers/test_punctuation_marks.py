import unittest
from src.tajweed_rules_helpers.punctuation_marks import PunctuationMarks

# Adjustment Reducer Examples
# MEEM - starting_index - adjustment - final letter
adj_meem_saakin_middle = 'ٱمْرَأَتُهُ'  # 2, 2, ra
adj_meem_saakin_end = 'لَمْ يَ'  # 2, 3, ya
adj_meem_saakin_end_stop = 'هِمْ ۚ إِنَّ'  # 2, 5, kasra/alif; stop signs add 2

adj_bare_meem_end = 'م مِّن'  # 0, 2, meem
adj_bare_meem_end_stop = 'م ۚ بَ'  # 0, 4, ba

# NOON
adj_noon_bare_middle = 'ٱلْإِنسَٰنَ'  # bare noon in middle; 5 1 seen
adj_noon_bare_end = 'مَن يَ'  # 2 2 ya

adj_noon_voweled_middle = 'لَيُنۢبَذَنَّ'  # 4 2 ba
adj_noon_voweled_end = 'نۢ بَ'  # 0 3 ba

# TANWEEN
adj_fatha_tanween = 'رًا وَ'  # fatha tanween (always at the end)
adj_fatha_tanween_other = 'صَفًّا صَ'
# fatha tanween (always at the end) + stop **
adj_fatha_tanween_stop = "رًا ۚ وَ"
adj_fatha_tanween_other_stop = "حَقًّا ۚ وَ"

adj_tanween = "نٌ وَ"
adj_tanween_other = 'يَبٌّ لأ'  # tanween with other mark on top
adj_tanween_other_2 = 'صُمٌّۢ بُ'  # tanween with more than 1 mark on top
adj_tanween_other_stop = "حَقٍّ ۚ ذَٰ"  # tanween with other mark on top + stop

# Possible ayah endings
no_marks = 'منة'
one_mark = 'منةٌ'
multiple_marks = 'صُمٌّۢ'
with_fatha_tanween = 'صَفًّا'
with_fatha_tanween_2 = 'سَبِيلًۢا'
includes_stop = "حَقًّا ۚ"
sukoon_after_wow = "قَالُواْ"

class TestPunctuationMarks(unittest.TestCase):
  def test_ending_sukoon_after_wow(self):
    ending_index = PunctuationMarks().calculate_adjustment_from_end(sukoon_after_wow)
    self.assertEqual(ending_index, 5)
    self.assertEqual(sukoon_after_wow[ending_index], 'و')
    
  def test_ending_no_marks(self):
    ending_index = PunctuationMarks().calculate_adjustment_from_end(no_marks)
    self.assertEqual(ending_index, 2)
    self.assertEqual(no_marks[ending_index], 'ة')

  def test_ending_one_mark(self):
    ending_index = PunctuationMarks().calculate_adjustment_from_end(one_mark)
    self.assertEqual(ending_index, 2)
    self.assertEqual(one_mark[ending_index], 'ة')

  def test_ending_multiple_marks(self):
    ending_index = PunctuationMarks().calculate_adjustment_from_end(multiple_marks)
    self.assertEqual(ending_index, 2)
    self.assertEqual(multiple_marks[ending_index], 'م')

  def test_ending_with_fatha_tanween(self):
    ending_index = PunctuationMarks().calculate_adjustment_from_end(with_fatha_tanween)
    self.assertEqual(ending_index, 2)
    self.assertEqual(with_fatha_tanween[ending_index], 'ف')
    
  def test_ending_with_fatha_tanween2(self):
    ending_index = PunctuationMarks().calculate_adjustment_from_end(with_fatha_tanween_2)
    self.assertEqual(ending_index, 5)
    self.assertEqual(with_fatha_tanween_2[ending_index], 'ل')

  def test_ending_includes_stop(self):
    ending_index = PunctuationMarks().calculate_adjustment_from_end(includes_stop)
    self.assertEqual(ending_index, 2)
    self.assertEqual(includes_stop[ending_index], 'ق')

  def test_calculate_punctuation_mark_adj_meem_saakin_middle(self):
    starting_index = 1
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_meem_saakin_middle, starting_index)
    self.assertEqual(adjustment, 2)
    self.assertEqual(adj_meem_saakin_middle[starting_index + adjustment], 'ر')

  def test_calculate_adjustment_from_beginning_adj_meem_saakin_end(self):
    starting_index = 2
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_meem_saakin_end, starting_index)
    self.assertEqual(adjustment, 3)
    self.assertEqual(adj_meem_saakin_end[starting_index + adjustment], 'ي')

  def test_calculate_adjustment_from_beginning_adj_meem_saakin_end_stop(self):
    starting_index = 2
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_meem_saakin_end_stop, starting_index)
    self.assertEqual(adjustment, 5)
    self.assertEqual(adj_meem_saakin_end_stop[starting_index + adjustment], 'إ')

  def test_calculate_adjustment_from_beginning_adj_bare_meem_end(self):
    starting_index = 0
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_bare_meem_end, starting_index)
    self.assertEqual(adjustment, 2)
    self.assertEqual(adj_bare_meem_end[starting_index + adjustment], 'م')

  def test_calculate_adjustment_from_beginning_adj_bare_meem_end_stop(self):
    starting_index = 0
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_bare_meem_end_stop, starting_index)
    self.assertEqual(adjustment, 4)
    self.assertEqual(adj_bare_meem_end_stop[starting_index + adjustment], 'ب')

  def test_calculate_adjustment_from_beginning_adj_noon_bare_middle(self):
    starting_index = 5
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_noon_bare_middle, starting_index)
    self.assertEqual(adjustment, 1)
    self.assertEqual(adj_noon_bare_middle[starting_index + adjustment], 'س')

  def test_calculate_adjustment_from_beginning_adj_noon_bare_end(self):
    starting_index = 2
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_noon_bare_end, starting_index)
    self.assertEqual(adjustment, 2)
    self.assertEqual(adj_noon_bare_end[starting_index + adjustment], 'ي')

  def test_calculate_adjustment_from_beginning_adj_noon_voweled_middle(self):
    starting_index = 4
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_noon_voweled_middle, starting_index)
    self.assertEqual(adjustment, 2)
    self.assertEqual(adj_noon_voweled_middle[starting_index + adjustment], 'ب')

  def test_calculate_adjustment_from_beginning_adj_noon_voweled_end(self):
    starting_index = 0
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_noon_voweled_end, starting_index)
    self.assertEqual(adjustment, 3)
    self.assertEqual(adj_noon_voweled_end[starting_index + adjustment], 'ب')

  def test_calculate_adjustment_from_beginning_adj_fatha_tanween(self):
    starting_index = 0
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_fatha_tanween, starting_index)
    self.assertEqual(adjustment, 4)
    self.assertEqual(adj_fatha_tanween[starting_index + adjustment], 'و')

  def test_calculate_adjustment_from_beginning_adj_fatha_tanween_other(self):
    starting_index = 2
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_fatha_tanween_other, starting_index)
    self.assertEqual(adjustment, 5)
    self.assertEqual(adj_fatha_tanween_other[starting_index + adjustment], 'ص')

  def test_calculate_adjustment_from_beginning_adj_fatha_tanween_stop(self):
    starting_index = 0
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_fatha_tanween_stop, starting_index)
    self.assertEqual(adjustment, 6)
    self.assertEqual(adj_fatha_tanween_stop[starting_index + adjustment], 'و')

  def test_calculate_adjustment_from_beginning_adj_fatha_tanween_other_stop(self):
    starting_index = 2
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_fatha_tanween_other_stop, starting_index)
    self.assertEqual(adjustment, 7)
    self.assertEqual(adj_fatha_tanween_other_stop[starting_index + adjustment], 'و')

  def test_calculate_adjustment_from_beginning_adj_tanween(self):
    starting_index = 0
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_tanween, starting_index)
    self.assertEqual(adjustment, 3)
    self.assertEqual(adj_tanween[starting_index + adjustment], 'و')

  def test_calculate_adjustment_from_beginning_adj_tanween_other(self):
    starting_index = 2
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_tanween_other, starting_index)
    self.assertEqual(adjustment, 4)
    self.assertEqual(adj_tanween_other[starting_index + adjustment], 'ل')

  def test_calculate_adjustment_from_beginning_adj_tanween_other_2(self):
    starting_index = 2
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_tanween_other_2, starting_index)
    self.assertEqual(adjustment, 5)
    self.assertEqual(adj_tanween_other_2[starting_index + adjustment], 'ب')

  def test_calculate_adjustment_from_beginning_adj_tanween_other_stop(self):
    starting_index = 2
    adjustment = PunctuationMarks().calculate_adjustment_from_beginning(adj_tanween_other_stop, starting_index)
    self.assertEqual(adjustment, 6)
    self.assertEqual(adj_tanween_other_stop[starting_index + adjustment], 'ذ')

  def test_is_punctuation_mark(self):
    mark = PunctuationMarks().is_punctuation_mark("ً")
    letter = PunctuationMarks().is_punctuation_mark("س")
    space = PunctuationMarks().is_punctuation_mark(" ")
    self.assertTrue(mark)
    self.assertFalse(letter)
    self.assertFalse(space)


# MEEM SAAKIN "MUST STOP ۘ "
# Voweled
must_stop_idhaar_shafawi_end = 'فَتَوَلَّ عَنْهُمْ ۘ يَوْمَ يَدْعُ ٱلدَّاعِ إِلَىٰ شَىْءٍ نُّكُرٍ'

# MEEM SAAKIN "PERMISSIBLE STOP ۚ "
# Bare
permissible_stop_ikhfa_shafawi_end = 'أَمْ يَحْسَبُونَ أَنَّا لَا نَسْمَعُ سِرَّهُمْ وَنَجْوَىٰهُم ۚ بَلَىٰ وَرُسُلُنَا لَدَيْهِمْ يَكْتُبُونَ'
permissible_stop_idghaam_shafawi_end = 'إِنِّى تَوَكَّلْتُ عَلَى ٱللَّهِ رَبِّى وَرَبِّكُم ۚ مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ ۚ إِنَّ رَبِّى عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ'
# Voweled
permissible_stop_idhaar_shafawi_end = 'قَدْ فَرَضَ ٱللَّهُ لَكُمْ تَحِلَّةَ أَيْمَٰنِكُمْ ۚ وَٱللَّهُ مَوْلَىٰكُمْ ۖ وَهُوَ ٱلْعَلِيمُ ٱلْحَكِيمُ'

# MEEM SAAKIN "POSSIBLE (PERMISSIBLE) STOP ۖ "
# Bare
possible_stop_ikhfa_shafawi_end = 'يَمُنُّونَ عَلَيْكَ أَنْ أَسْلَمُوا۟ ۖ قُل لَّا تَمُنُّوا۟ عَلَىَّ إِسْلَٰمَكُم ۖ بَلِ ٱللَّهُ يَمُنُّ عَلَيْكُمْ أَنْ هَدَىٰكُمْ لِلْإِيمَٰنِ إِن كُنتُمْ صَٰدِقِينَ'
possible_stop_idghaam_shafawi_end = 'أَمْ حَسِبْتُمْ أَن تَدْخُلُوا۟ ٱلْجَنَّةَ وَلَمَّا يَأْتِكُم مَّثَلُ ٱلَّذِينَ خَلَوْا۟ مِن قَبْلِكُم ۖ مَّسَّتْهُمُ ٱلْبَأْسَآءُ وَٱلضَّرَّآءُ وَزُلْزِلُوا۟ حَتَّىٰ يَقُولَ ٱلرَّسُولُ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ مَتَىٰ نَصْرُ ٱللَّهِ ۗ أَلَآ إِنَّ نَصْرَ ٱللَّهِ قَرِيبٌ'
# Voweled
possible_stop_idhaar_shafawi_end = 'قَدْ فَرَضَ ٱللَّهُ لَكُمْ تَحِلَّةَ أَيْمَٰنِكُمْ ۚ وَٱللَّهُ مَوْلَىٰكُمْ ۖ وَهُوَ ٱلْعَلِيمُ ٱلْحَكِيمُ'

# MEEM SAAKIN "PREFERABLE STOP ۗ "
# Bare
preferable_stop_idghaam_shafawi_end = 'وَقَالُوا۟ لَوْ شَآءَ ٱلرَّحْمَٰنُ مَا عَبَدْنَٰهُم ۗ مَّا لَهُم بِذَٰلِكَ مِنْ عِلْمٍ ۖ إِنْ هُمْ إِلَّا يَخْرُصُونَ'
# Voweled
preferable_stop_idhaar_shafawi_end = 'أَلَآ إِنَّهُمْ فِى مِرْيَةٍ مِّن لِّقَآءِ رَبِّهِمْ ۗ أَلَآ إِنَّهُۥ بِكُلِّ شَىْءٍ مُّحِيطٌۢ'

# MEEM SAAKIN "LINKED STOPS ۛ  ۛ"
# Voweled
linked_stops_idhaar_shafawi_end = 'قَالَ فَإِنَّهَا مُحَرَّمَةٌ عَلَيْهِمْ ۛ أَرْبَعِينَ سَنَةً ۛ يَتِيهُونَ فِى ٱلْأَرْضِ ۚ فَلَا تَأْسَ عَلَى ٱلْقَوْمِ ٱلْفَٰسِقِينَ'

# MEEM SAAKIN "FORBIDDEN STOP ۙ "
# Voweled
forbidden_stop_idhaar_shafawi_end = 'ذَٰلِكَ بِأَنَّ ٱللَّهَ لَمْ يَكُ مُغَيِّرًا نِّعْمَةً أَنْعَمَهَا عَلَىٰ قَوْمٍ حَتَّىٰ يُغَيِّرُوا۟ مَا بِأَنفُسِهِمْ ۙ وَأَنَّ ٱللَّهَ سَمِيعٌ عَلِيمٌ'

# ----------------------------------------------------------------------------------------------------
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
