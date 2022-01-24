# Wordle Helper!

A guess generating aid for playing the game [Wordle](https://www.powerlanguage.co.uk/wordle/)!

_Note: This small project is just for my own fun and if I post results from this anywhere I make it clear that the results were produced with the aid of a computer. By no means am I trying to ruin the spirit of Wordle!_

### How to Use:

1. In **main.py** at the bottom, fill in known information in _correct_spots_ (green letters), _wrong_spots_ (yellow letters), and _wrong_letters_ (gray letters).
2. Run **main.py**.
3. Choose the top scored word (or any word at your discretion from the list) and submit to the [Wordle](https://www.powerlanguage.co.uk/wordle/) game.
4. Take any new known information from your submitted guess, add it to the inputs in **main.py**, and generate a new guess from the new information.

### Notes to User (and Self):
- The original dictionary I used contains a lot of words that probably aren't really going to be picked as Wordle words. In the future, I could potentially find a better source dictionary to use. You can replace the dictionary in **all_words.txt** with the new dictionary and run the function _all_words_to_five_letter_words()_ in **main.py** to update the file **five_letter_words.txt**.




### V1 (current version)
#### Past results (from always guessing the first recommended word produced in the list)
- #214 - POINT (aires, louin, doing, joint, point)
- #213 - PROXY (aires, yourt, droyl, crony, frowy, grovy, proxy)
- #212 - SHIRE (aires, reist, shire)
- #211 - SOLAR (aires, rosat, sofar, solar)
- #210 - PANIC (aires, lanti, canid, manic, panic)
- #209 - TANGY (aires, laton, tangy)

#### Optimization to make upon this
- Early guesses should prioritize maximizing information over attempting to guess actual words. Later guesses should attempt to guess actual words. (V1 always just guesses based on trying to maximize information.)
- Find a better dictionary to use with more realistic potential Wordle words
- Explore whether calculating dictionary letter frequencies vs text letter frequencies improves guessing results
