import os

def get_rules():
  return os.environ.get('RULE_LIST')

get_rules()
