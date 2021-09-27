from use_cases.rule import Rule
from controllers.input_factory import InputFactory
from presenters.output_factory import OutputFactory

class Idhaar(Rule):
  def __init__(self, input_factory, output_factory):
    self
    self.input = input_factory
    self.output = output_factory

  def generate_rule_file(self):
    content_for_rule = {}
    idhaar_locations = []

    quran = self.input.read_quran_file()
    
    for line in quran:
      parsed_line = self.input.get_input().parse_quran_script(line)
      surah_number = parsed_line['surah_number']
      ayah_number = parsed_line['ayah_number']
      ayah_text = parsed_line['ayah_text']

      noon_saakin_indices = self.find_letter_in_text('ن', ayah_text)
      noon_idhaar_locations = self.get_all_rule_locations_for_letter_base(noon_saakin_indices, ayah_text, surah_number, ayah_number)
      idhaar_locations + noon_idhaar_locations

      kasra_dummah_tanween_indices = self.find_tanween_in_text('ٌٍ' , ayah_text)
      kasra_dummah_tanween_idhaar_locations = self.get_all_rule_locations_for_tanween_base('kasra', kasra_dummah_tanween_indices, ayah_text, surah_number, ayah_number)
      idhaar_locations + kasra_dummah_tanween_idhaar_locations

      fatha_tanween_indices = self.find_tanween_in_text('ً' , ayah_text)
      fatha_tanween_idhaar_locations = self.get_all_rule_locations_for_tanween_base('fatha', fatha_tanween_indices, ayah_text, surah_number, ayah_number)
      idhaar_locations + fatha_tanween_idhaar_locations

    quran.close()
    
    content_for_rule["idhaar"] = idhaar_locations 
    output_file = self.output.get_output().create_absolute_output_path('idhaar')
    self.output.get_output().write_to_output_file(content_for_rule, output_file)

idhaar = Idhaar(InputFactory('idhaar_file'), OutputFactory('file'))