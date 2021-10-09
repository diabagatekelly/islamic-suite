from use_cases.mapper import Mapper
from controllers.input_factory import InputFactory
from presenters.output_factory import OutputFactory

class IdhaarShafawiRule(Mapper):
  def __init__(self, input_factory, output_factory):
    self
    self.input = input_factory
    self.output = output_factory

  def generate_rule_file(self):
    content_for_rule = {}
    idhaar_shafawi_locations = []

    quran = self.input.open_quran_file()
    
    for line in quran:
      parsed_line = self.parse_quran_script(line)
      surah_number = parsed_line['surah_number']
      ayah_number = parsed_line['ayah_number']
      ayah_text = parsed_line['ayah_text']

      map = Mapper(surah_number, ayah_number, ayah_text)

      meem_idhaar_locations = map.get_all_rule_locations('م')      
      idhaar_shafawi_locations = idhaar_shafawi_locations + meem_idhaar_locations

    # quran.close()
    
    content_for_rule["idhaar_shafawi"] = idhaar_shafawi_locations 
    output_file = self.output.create_absolute_output_path('idhaar_shafawi')
    self.output.write_to_output_file(content_for_rule, output_file)

idhaar_shafawi = IdhaarShafawiRule(InputFactory('idhaar_file'), OutputFactory('file'))