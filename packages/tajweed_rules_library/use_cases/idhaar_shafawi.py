from use_cases.rule import Rule
from controllers.input_factory import InputFactory
from presenters.output_factory import OutputFactory

class IdhaarShafawi(Rule):
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

      meem_saakin_indices = self.find_letter_in_text('م', ayah_text)
      meem_idhaar_locations = self.get_all_rule_locations_for_letter_base(meem_saakin_indices, ayah_text, surah_number, ayah_number)
      idhaar_shafawi_locations + meem_idhaar_locations

    quran.close()
    
    content_for_rule["idhaar_shafawi"] = idhaar_shafawi_locations 
    output_file = self.output.create_absolute_output_path('idhaar_shafawi')
    self.output.write_to_output_file(content_for_rule, output_file)

idhaar_shafawi = idhaar = IdhaarShafawi(InputFactory('idhaar_file'), OutputFactory('file'))