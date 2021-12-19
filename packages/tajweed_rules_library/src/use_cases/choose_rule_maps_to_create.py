class ChooseRuleMapsToCreate():
  def __init__(self, factory, files_and_dirs):
    self
    self.factory = factory
    self.files_and_dirs = files_and_dirs
  
  # Methods from factory
  def _file_to_rule_maps(self):
    return self.factory.get_file_to_map_gateway()

  def _file_system(self):  
    return self.factory.get_file_system()

  def get_list_of_rule_maps_to_create(self):
    if self.factory.env == 'local':
      existing_rules_with_no_updates = self._get_existing_rules_with_no_updates()
      all_rules = self._get_all_rule_names()
      return [rule for rule in all_rules if rule not in existing_rules_with_no_updates]
    elif self.factory.env == 'prod':
      existing_prod_rules_with_no_updates = self._get_existing_rules_with_no_updates()
      all_local_rules_outputs = self._get_transformed_rule_definitions_file_info()
      print([rule for rule in all_local_rules_outputs if rule['name'] not in existing_prod_rules_with_no_updates])
      return [rule for rule in all_local_rules_outputs if rule['name'] not in existing_prod_rules_with_no_updates]

  def _get_all_rule_names(self):
    all_rule_names = [rule['name'] for rule in self._get_transformed_rule_definitions_file_info()]
    return self._remove_non_rule_definitions_files_and_duplicates(all_rule_names)

  def _remove_non_rule_definitions_files_and_duplicates(self, name_list):
    filtered_list = [name for name in name_list if name not in ('__init__.py')]
    final_list = list(set(filtered_list))
    return final_list
  
  def _get_existing_rules_with_no_updates(self):
    existing_rules_with_no_updates = []
    all_existing_rules = [file["name"] for file in self._get_transformed_existing_rules_file_info()]
    for rule in all_existing_rules:
      if self._rule_definition_has_recent_updates(rule) == False:
        existing_rules_with_no_updates.append(rule)
    return existing_rules_with_no_updates
  
  def _rule_definition_has_recent_updates(self, rule_name):
    last_rule_definition_file_update = self._get_rule_definition_file_last_update(rule_name)
    last_existing_rule_file_update = self._get_existing_rules_file_last_update(rule_name)
    return last_rule_definition_file_update >= last_existing_rule_file_update

  def _get_rule_definition_file_last_update(self, rule_name):
    rule_definition_file_path = [file["absolute_path"] for file in self._get_transformed_rule_definitions_file_info() if file["name"] == rule_name]
    return self._file_system().get_file_last_update_date(rule_definition_file_path[0])

  def _get_existing_rules_file_last_update(self, rule_name):
    existing_rule_file_path = [file["absolute_path"] for file in self._get_transformed_existing_rules_file_info() if file["name"] == rule_name]
    return self._file_system().get_file_last_update_date(existing_rule_file_path[0])

  def _get_transformed_rule_definitions_file_info(self):
    all_files = self._get_all_rule_definitions_file_info()
    for file_details in all_files:
      file_details['name'] = self._get_rule_name_from_file(file_details['name'])
    return all_files

  def _get_all_rule_definitions_file_info(self):
    if self.factory.env == 'local':
      return self._file_system().get_files_in_directory(self.files_and_dirs['entities_dir'])
    elif self.factory.env == 'prod':
      return self._file_system().get_files_in_directory(self.files_and_dirs['local_outputs'])
  
  def _get_transformed_existing_rules_file_info(self):
    files = self._get_all_existing_rules_file_info()
    for file_details in files:
      file_details['name'] = self._get_rule_name_from_file(file_details['name'])
    return files

  def _get_all_existing_rules_file_info(self):
    if self.factory.env == 'local':
      return self._file_system().get_files_in_directory(self.files_and_dirs['outputs_dir'])
    elif self.factory.env == 'prod':
      return self._file_system().get_files_in_directory(self.files_and_dirs['outputs_dir'])

  def _get_rule_name_from_file(self, file_name):
    return self._file_to_rule_maps().get_name_from_file(file_name)
  