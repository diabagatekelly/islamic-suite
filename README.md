# Tajweed App
The Tajweed app is a Quran Tajweed teaching app which allows students and teachers to learn, practice and get tested on a variety of tajweed rules. A specified number of random, consecutive ayaat are provided, and the user has to identify the rule being practiced. Stats about the user's performance for each rule is saved. 

## Structure
The app is structured as a monorepository comprised of 3 packages:
1. The client-side app built with Angular.
2. The server-side app built with Python and a PostgreSQL database.
3. A tajweed rules' library, which is a collection of JSON files and simple CLI functionalities to transform them. The original files were provided by https://github.com/cpfair/quran-tajweed. Those files were processed to return a different JSON output more suitable to the purpose of this app.
