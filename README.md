# pitchfork_game

A simple trivia/guessing game that uses data from Pitchfork's most popular album reviews page to generate a list of album names and prompts the user to guess the artist. Made for Flawless Hacks in NYC.

albums.py is a scrapy spider that scrapes the first five pages of the most popular album reviews, retrieving album names and artists. Then, album names and artist names are written into album_names.txt and artists.txt. game.py contains the code for the guessing game, where a user can input the number of questions they want.

After the user inputs their number of questions, game.py creates a random list of indices (with values 0-59) with the list size equal to the number of questions the user wants. Then, each album's title is printed to the terminal and the user can input their answer (capitalization does not matter). If the user's answer is wrong, the correct answer will be displayed. Once all questions have been answered, the user will see their score out of the total number of questions asked.

# Issues to fix

ampersands are not correctly displayed

in albums with more than one artist, the names of the artists are smushed together with no space or "and"