### Spellcheck

Anki add-on to check spellings in card editor and suggest correct words. A simple verison of deprecated add-on SpellingPolice-[lovac42] and updated to be compatible with Qt6.

#### Installation

Copy the `spellcheck` directory to your `addons21` folder. Move the `spellcheck/dictionaries` subdirectory to the parent folder of `addons21` which should be `Anki2`. It comes with UK and US English but will recognise and load any other .bdic dictionaries that are placed within `dictionaries`.

Dictionaries can be found here: https://github.com/cvsuser-chromium/third_party_hunspell_dictionaries

#### Use

Select the current dictionary by going to `Tools>Spellcheck Options` in the Anki menu bar. Right-click misspelled words to see a list of suggestions and left-click to replace. Spellcheck can be toggled off and on from this menu for when cards contain a lot of non-conventional syntax and the misspelled-highlighting becomes unhelpful.

Currently tested and working on `macOS Qt5.14 Anki 2.1.64` and `Windows Qt6.4.3 Anki 2.1.64`
