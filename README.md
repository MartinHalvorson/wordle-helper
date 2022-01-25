# Wordle Helper!

A guess generating aid for playing the game [Wordle](https://www.powerlanguage.co.uk/wordle/)!

_Note: This small project is just for my own fun and if I post results from this anywhere I make it clear that the results were produced with the aid of a computer. By no means am I trying to ruin the spirit of Wordle!_

### How to Use:

1. In **main.py** at the bottom, fill in known information in _correct_spots_ (green letters), _wrong_spots_ (yellow letters), and _wrong_letters_ (gray letters).
2. Run **main.py**.
3. Choose the top scored word (or any word at your discretion from the list) and submit to the [Wordle](https://www.powerlanguage.co.uk/wordle/) game.
4. Take any new known information from your submitted guess, add it to the inputs in **main.py**, and generate a new guess from the new information.

## V2 (current version) - Averages 3.2 guesses per word
### With the first two guesses, the program tries to gather maximum information using the frequency of letters in words.
- Uses both dictionary and text relative letter frequencies to score words
- If on the first guess, you get a green letter, you don't need to (necessarily) guess this green letter in the second clue if you are trying to maximize information.
### Starting with the third guess, the program attempts to guess the actual word.
- Two dictionaries: a simpler list of more common five letters words and a rarer, more complete word dictionary. Words on common list score a little higher.
- In scoring, punishes dictionary words ending with an s (higher likelihood of being plural). Wordle doesn't often pick plurals.
- Rare letter bonus kicks into scoring after the first two guesses. It appears to me Wordle tries to include words using unique letters (QUEEN, PROXY, KNOLL) so we will keep this in mind guessing.

### Past results (from always guessing the first recommended word produced in the list)
- 19 guesses to guess words #209-#214
- #215 - KNOLL (arose, cloth, looky, knoll)
- #214 - POINT (arose, point)
- #213 - PROXY (arose, front, proxy)
- #212 - SHIRE (arose, resin, swire, shire)
- #211 - SOLAR (arose, solar)
- #210 - PANIC (arose, paint, panic)
- #209 - TANGY (arose, paint, janty, tanzy, tangy)

### Optimization to make upon V1
- Rather than always switching to guessing the word on the third clue, could base when the switch happens on the number of possible words remaining (i.e. with lots of words remaining, you may still want to guess for maximizing information).
- Find an even better dictionary. Every time the word was in the dictionary the word was guessed in 2-3 guesses. The 4-5 guesses are from Wordle words not in the more common dictionary I use.

## V1 - Averages 4.5 guesses per word
- Uses dictionary letter frequencies to score words
### Past results (from always guessing the first recommended word produced in the list)
- 27 guesses to guess words #209-#214
- #214 - POINT (aires, louin, doing, joint, point)
- #213 - PROXY (aires, yourt, droyl, crony, frowy, grovy, proxy)
- #212 - SHIRE (aires, reist, shire)
- #211 - SOLAR (aires, rosat, sofar, solar)
- #210 - PANIC (aires, lanti, canid, manic, panic)
- #209 - TANGY (aires, laton, tangy)

### Optimization to make upon V1
- Early guesses should prioritize maximizing information over attempting to guess actual words. Later guesses should attempt to guess actual words. (V1 always just guesses based on trying to maximize information.)
- Find a better dictionary to use with more realistic potential Wordle words
- Explore whether calculating dictionary letter frequencies vs text letter frequencies improves guessing results. Another possibility is to use letter frequencies from historical Wordle answers... maybe worth exploring.
