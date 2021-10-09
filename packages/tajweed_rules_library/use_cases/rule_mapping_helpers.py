class RuleMappingHelpers():

  def construct_rule_location_map(self, surah, ayah, start_index, end_index):
    ayah_rule_info = {}
    ayah_rule_info["surah"] = surah
    ayah_rule_info["ayah"] = ayah
    ayah_rule_info["start"] = start_index
    ayah_rule_info["end"] = end_index
    return ayah_rule_info
 
  def get_rule_end_index(self, start_index, move_by_spaces):
    return start_index + move_by_spaces
