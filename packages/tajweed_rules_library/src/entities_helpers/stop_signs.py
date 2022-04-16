class StopSigns():
  """Stop Signs

  This class finds the index of a stop sign. It takes into account whether 
  the letter before the stop sign is bare or voweled. Most stop signs occur after a word.
  One stop sign can also be found inside words.

  Stop signs:
   ۘ - Must stop
   ۚ - Permissible stop (can stop or continue)
   ۖ - Allowed to stop but better to continue
   ۗ - Preferred to stop
   ۜ - The silence symbol, indicates the reader should take a brief pause without breaking its breath
   ۛ ۛ- The linked stops; must stop at one or the other
   ۙ - Forbidden to stop

  Methods:
    *find_stop_sign_for_bare_letter (public) - returns adjustment to add to bare letter before stop sign
    *find_stop_sign_for_voweled_letter (public) - returns adjustment to add to voweled letter before stop sign
  """
  def __init__(self):
    self.list_of_signs = ['ۭ', "ۗ", "ۚ", "ۜ", "ۛ", "ۙ", "ۘ", "ۖ"]

  def find_stop_sign_for_bare_letter(self):
    """Returns adjustment to add to bare letter before stop sign
			- returns 2
    """
    return 2

  def find_stop_sign_for_voweled_letter(self): 
    """Returns adjustment to add to voweled letter before stop sign
			- returns 3
    """
    return 3