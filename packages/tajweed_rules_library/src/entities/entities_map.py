from src.entities.madd_rules.madd_246 import Madd246
from src.entities.madd_rules.madd_6 import Madd6
from src.entities.madd_rules.madd_munfasil import MaddMunfasil
from src.entities.madd_rules.madd_muttasil import MaddMuttasil
from src.entities.misc_letter_rules.idghaam_mutajanisayn import IdghaamMutajanisayn
from src.entities.misc_letter_rules.idghaam_mutaqaribayn import IdghaamMutaqaribayn
from src.entities.misc_letter_rules.idghaam_no_ghunnah import IdghaamNoGhunnah
from src.entities.misc_letter_rules.qalqalah import Qalqalah
from src.entities.noon_saakin_rules.idghaam_ghunnah import IdghaamGhunnah
from src.entities.noon_saakin_rules.idhaar import Idhaar
from src.entities.noon_saakin_rules.ikhfa import Ikhfa
from src.entities.noon_saakin_rules.iqlab import Iqlab
from src.entities.shaddah_rules.ghunnah import Ghunnah
from src.entities.meem_saakin_rules.idghaam_shafawi import IdghaamShafawi
from src.entities.meem_saakin_rules.idhaar_shafawi import IdhaarShafawi
from src.entities.meem_saakin_rules.ikhfa_shafawi import IkhfaShafawi

RULES = {
  'Madd6': Madd6,
  'Madd246': Madd246,
  'MaddMunfasil': MaddMunfasil,
  'MaddMuttasil': MaddMuttasil,
  'IdghaamShafawi': IdghaamShafawi,
  'IdhaarShafawi': IdhaarShafawi,
  'IkhfaShafawi': IkhfaShafawi,
  'IdghaamMutajanisayn': IdghaamMutajanisayn,
  'IdghaamMutaqaribayn': IdghaamMutaqaribayn,
  'IdghaamNoGhunnah': IdghaamNoGhunnah,
  'Qalqalah': Qalqalah,
  'IdghaamGhunnah': IdghaamGhunnah,
  'Idhaar': Idhaar,
  'Ikhfa': Ikhfa,
  'Iqlab': Iqlab,
  'Ghunnah': Ghunnah
}

class EntitiesMap():
  def fetch_entity(self, class_name):
    return RULES[class_name]