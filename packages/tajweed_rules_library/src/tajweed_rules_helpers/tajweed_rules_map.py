# from src.entities.madd_rules.madd_246 import Madd246
# from src.entities.madd_rules.madd_6 import Madd6
# from src.entities.madd_rules.madd_munfasil import MaddMunfasil
# from src.entities.madd_rules.madd_muttasil import MaddMuttasil
# from src.entities.misc_letter_rules.idghaam_mutajanisayn import IdghaamMutajanisayn
# from src.entities.misc_letter_rules.idghaam_mutaqaribayn import IdghaamMutaqaribayn
# from src.entities.misc_letter_rules.qalqalah import Qalqalah

# Noon Saakin Rules
from src.entities.noon_saakin_rules.noon_saakin_rule_factory import NoonSaakinRuleFactory
from src.entities.noon_saakin_rules.idghaam_ghunnah import IdghaamGhunnah
from src.entities.noon_saakin_rules.idghaam_no_ghunnah import IdghaamNoGhunnah
from src.entities.noon_saakin_rules.idhaar import Idhaar
from src.entities.noon_saakin_rules.ikhfa import Ikhfa
from src.entities.noon_saakin_rules.iqlab import Iqlab

# Meem Saakin Rules
from src.entities.meem_saakin_rules.meem_saakin_rules import MeemSaakinRules

TAJWEED_RULES = {
  'MeemSaakinRules': MeemSaakinRules,
  'NoonSaakinRuleFactory': NoonSaakinRuleFactory
}