# Tajweed App
The Tajweed app is a Quran Tajweed teaching app which allows students and teachers to learn, practice and get tested on a variety of tajweed rules. A specified number of random, consecutive ayaat are provided, and the user has to identify the rule being practiced. Stats about the user's performance for each rule is saved. 

## Structure
The app is structured as a monorepository comprised of 3 packages:
1. The client-side app built with Angular.
2. The server-side app built with Python and a PostgreSQL database.
3. A tajweed rules' library, which is a collection of JSON files and simple CLI functionalities to transform them. The original files were provided by https://github.com/cpfair/quran-tajweed. Those files were processed to return a different JSON output more suitable to the purpose of this app.

## Library
### Virtual Env
  source venv/Scripts/activate
### Testing
  1. cd packages/tajweed_rules_library
  2. Run all specs - python -m unittest -v
  3. Run a single spec - python -m unittest -v { path from src to test } (ie. src.entities_helpers.test_punctuation_marks.TestPunctuationMarks.test_calculate_punctuation_mark_adjustment)
  4. Coverage - coverage run -m unittest (from virtual env)
  5. Coverage (omitting specs and factory) - coverage html --omit=venv/*,src/factory.py,src/*/test_*.py,src/__init__.py*,src/*/__init__.py*

### Build JSON maps
  1. cd packages/tajweed_rules_library
  2. git add -N
  2. DEV - python -m src.main run_app local
  3. PROD - python -m src.main run_app prod

  TODO: specs
    test_file_system
    1. self.assertEqual(last_line, '111|4|وَٱمْرَأَتُهُۥ حَمَّالَةَ ٱلْحَطَبِ') - UPDATE

    test_create_rules_maps - ADD
      1. test_getting_correct_map_content_noon_saakin_rules
