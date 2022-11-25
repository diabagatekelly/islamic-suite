from git import Repo
import os

class ChooseRuleMapsToCreate():
	"""Choose Rule Maps To Create

	The entities folder contains entity modules, each defining the following for a single tajweed rule:
	  1. how to find that rule in the quran
	  2. save all the locations of that rule as a map

	This module chooses which tajweed rules need their map created.
	DEV: depends on whether there have been updates to that rule's entity file,
	or if it doesn't already have a map in the 'outputs' directory.
	PROD: depends on whether there have been updates to that rule's DEV map
	in the outputs directory, or if it doesn't already have a map in the 'dist' directory

	Constructor:
	  *files_and_dir: object containing relevant directories
	  *factory: dev or prod factory

	Factory methods:
	  *_file_to_rule_maps (private) - gets file_to_map gateway from factory
	  *_file_system (private) - gets file_system from factory

	Module methods:
		*_get_classnames_list_for_local - For local env, use git to find all new and modified files in the entities diectory,
  	and return a list of the class names
		*_get_new_or_modified_files - Get list of files in entities directory that are new
		or have been modified since last git commit
		*_get_class_name_from_file - Get class name from file
		*_get_tajweed_rules_with_recent_updates - Use git to find all files in the entities directory that are new
  	or have been modified 
		*_remove_duplicates(self, recently_updated) - Cleans up list of file paths by removing duplicates
		*_remove_specs_and_init(self, recently_updated) - Cleans up list of file paths by removing spec and init files

	  *get_list_of_json_maps_to_create (public) - get list of rules that need new maps depending on whether its entity (in dev)
		is new or has been modified, or all files in the 'outputs' directory in prod
	"""
	GIT_REPO = os.path.join(os.path.dirname((os.path.dirname(os.getcwd()))), '.git')

	def __init__(self, factory, files_and_dirs):
		self
		self.factory = factory
		self.files_and_dirs = files_and_dirs

	# Methods from factory
	def _file_to_rule_maps(self):
		"""Returns file_to_map gateway from pre-initialized dev or prod factory"""
		return self.factory.get_file_to_map_gateway()

	def _file_system(self):
		"""Returns file_system gateway from pre-initialized dev or prod factory"""
		return self.factory.get_file_system()

	# Module methods
	def get_list_of_json_maps_to_create(self):
		"""In DEV, use git to find all new and modified files in the entities diectory, and return a list of the class name
			for the class defined in those files
		  In PROD, get a list of the files in the 'outputs' directory, so they can be copied to the 'dist' folder
			- returns: array of classNames (dev) or array of rule objects {name: 'name', absolute_path: 'path.json'}
		"""
		if self.factory.env == 'local':
			return self._get_classnames_list_for_local()
		elif self.factory.env == 'prod':
			# Modifies the file details' dict in place by removing the extension from the file name property
			return list(map(lambda item: {'name': item['name'].split('.')[0], 'absolute_path': item['absolute_path']}, self._file_system().get_files_in_directory(self.files_and_dirs['local_outputs'])))

	def _get_classnames_list_for_local(self):
		"""For local env, use git to find all new and modified files in the entities diectory, and return a list of the class names
			- returns: array of classNames (dev)
		"""
		list_of_class_names = []
		file_list = self._get_new_or_modified_files()
		for item in file_list:
			list_of_class_names.append(self._get_class_name_from_file(item))
		return list_of_class_names	

	def _get_new_or_modified_files(self):
		"""Get list of files in entities directory that are new or have been modified since last git commit
			- returns: array of file paths
		"""
		all_recently_updated = self._get_tajweed_rules_with_recent_updates()

		without_duplicates = self._remove_duplicates(all_recently_updated)
		without_specs = self._remove_specs_and_init(without_duplicates)

		return list(map(lambda str: str.strip(), without_specs))

	def _get_tajweed_rules_with_recent_updates(self, directory_string='src/entities'):
		"""Use git to find all files in the entities directory that are new or have been modified 
			- parameters: directory_string (string in directory path to help filtering)
			- returns: array of file paths
		"""
		repo = Repo(self.GIT_REPO)
		untracked_new_files = [item for item in repo.untracked_files if directory_string in item]
		modified_and_deleted_files = [item.a_path for item in repo.index.diff(None) if directory_string in item.a_path]
		entities_files = [file['name'] for file in self._file_system().get_files_in_directory(self.files_and_dirs['entities_dir'])]
		modified_only = [file for file in modified_and_deleted_files if [name for name in entities_files if name in file]]
		final_modified_and_new_files = untracked_new_files + modified_only
		return final_modified_and_new_files
  
	def _remove_duplicates(self, recently_updated):
		"""Cleans up list of file paths by removing duplicates
			- parameters: name_list --> ['path/to/one', 'path/to/one', 'path/to/two']
			- returns: list of file paths ['path/to/one', 'path/to/two']
		"""
		return list(set(recently_updated))

	def _remove_specs_and_init(self, recently_updated):
		"""Cleans up list of file paths by removing spec and init files
			- parameters: name_list --> ['path/to/one', 'path/to/one_spec', 'path/to/two']
			- returns: list of file paths ['path/to/one', 'path/to/two']
		"""
		return list(filter(lambda file: (not 'test' in file) and (not 'init' in file), recently_updated))

	def _get_class_name_from_file(self, file_path):
		"""Get class name from file
			- returns: className
		"""
		class_name_in_file_path = self._file_to_rule_maps().get_name_from_file(file_path.split('/')[5])
		return self._file_to_rule_maps().get_rule_class_from_name(class_name_in_file_path)