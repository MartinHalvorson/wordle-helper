# Wordle Helper!

A guess generating aid for playing the game [Wordle](https://www.powerlanguage.co.uk/wordle/)!

_Note: This small project is just for my own fun and if I post results from this anywhere I make it clear that the results were produced with the aid of a computer. By no means am I trying to ruin the spirit of Wordle!_

### How to Use:
There are a few different capabilities in Wordle Helper:
1. **Single Guess Helper:** Input known information (green, yellow, gray letters) in the correct spots and have Wordle Helper help you pick your next word (the algorithm/scoring system is explained a bit more below). You can uncomment the code below at the bottom of the file _main.py_ (or just copy and paste from here). Fill in the letters in the correct spots and run _main.py_!
```
correct_spots = ['', '', '', '', '']  # Green letters
wrong_spots = ['', '', '', '', '']  # Yellow letters
wrong_letters = ''  # Gray letters
next_guess_count = 1  # e.g. 1 -> 1st guess

scored_list = wordle_helper(correct_spots, wrong_spots, wrong_letters, next_guess_count)
for word, score in scored_list[:20]:  # Only prints the top 20 words
    print(word, score)
```
2. **Simulate Guessing a Wordle:** Using the _simulate_word(word)_ function, you can simulate continuous guesses until the Wordle is guessed. The output is a list of every guess, (hopefully) ending with the Wordle!

In **main.py**:
```
simulate_word('apple')
simulate_word('enjoy')
```
Output:
```
Guesses:  ['arose', 'alien', 'amble', 'apple']
Guesses:  ['arose', 'noted', 'enjoy']
```
3. **Simulate Guessing many Wordles:** To test the above function across many Wordles, fill the file **past_answers.txt** with Wordles and run the function _calculate_average_guess_metric()_ in **main.py**.

In **main.py**:
```
calculate_average_guess_metric()
```
Output:
```
Inputs:  ['knoll', 'crimp', 'wince', 'prick', 'robot', 'point', 'proxy', 'shire', 'solar', 'panic', 'tangy', 'abbey', 'favor', 'drink', 'query', 'gorge', 'crank', 'slump', 'banal', 'tiger', 'siege', 'truss', 'boost', 'rebus']
Average Num Guesses per Wordle: 4.041666666666667
```

## V2 (current version) - Averages 4.0 guesses per word
### With the first two guesses, the program tries to gather maximum information using the frequency of letters in words.
- Uses both dictionary letter frequencies and text letter frequencies to score words
- If on the first guess, you get a green letter, you don't need to (necessarily) guess this green letter in the second clue if you are trying to maximize information.
- Duplicate letters in a guess are punished (they likely obtain less information than guessing two different letters)
### Starting with the third guess, the program attempts to guess the actual word.
- Two word lists: a simpler list of more common five letters words and a larger, more complete word list. Words on common list score a little higher.
- In scoring, punishes dictionary words ending with an s (higher likelihood of being plural). Wordle doesn't often pick plurals. There are some false positives with this and the program attempts to correct for this (i.e. if the word ends in "ss" or "us" it is less likely to be a plural and so these although they end with "s" aren't punished by the word scoring system).
- A small rare letter bonus kicks into scoring after the first two guesses. It appears to me Wordle tries to include words using unique letters (QUERY, PROXY, KNOLL) so we will keep this in mind when evaluating potential words.

### Past results (from always guessing the first recommended word produced in the list)
- #219 - KNOLL (arose, tonic, blown, knoll)
- #218 - CRIMP (arose, until, frizz, brick, crimp)
- #217 - WINCE (arose, unite, binge, mince, vince, wince)
- #216 - PRICK (arose, until, frizz, brick, prick)
- #215 - ROBOT (arose, intro, throw, robot)
- #214 - POINT (arose, tonic, joint, point)
- #213 - PROXY (arose, intro, proxy)
- #212 - SHIRE (arose, resin, spire, swire, shire)
- #211 - SOLAR (arose, solar)
- #210 - PANIC (arose, latin, mania, panic)
- #209 - TANGY (arose, latin, gaunt, tangy)
- #208 - ABBEY (arose, alien, abbey)
- #207 - FAVOR (arose, ratio, major, favor)
- #206 - DRINK (arose, until, wring, briny, drink)
- #205 - QUERY (arose, inert, query)
- #204 - GORGE (arose, other, forge, gorge)

### Optimizations to make upon V2
- Rather than always switching to guessing the word on the third clue, I could base when the switch happens on the number of possible words remaining (i.e. with lots of words remaining on the third guess, you may still want to guess for maximizing information).
- Find an even better dictionary. Every time the word was in the dictionary the word was guessed in 2-3 guesses. The 4-5 guesses are from Wordle words not in the more common dictionary I use.

## V1 - Averages ~5.0 guesses per word
- Uses dictionary letter frequencies to score words
### Past results (from always guessing the first recommended word produced in the list)
- #214 - POINT (aires, louin, doing, joint, point)
- #213 - PROXY (aires, yourt, droyl, crony, frowy, grovy, proxy)
- #212 - SHIRE (aires, reist, shire)
- #211 - SOLAR (aires, rosat, sofar, solar)
- #210 - PANIC (aires, lanti, canid, manic, panic)
- #209 - TANGY (aires, laton, tangy)

### Optimizations to make upon V1
- Early guesses should prioritize maximizing information over attempting to guess actual words. Later guesses should attempt to guess actual words. (V1 always just guesses based on trying to maximize information.)
- Find a better dictionary to use with more realistic potential Wordle words
- Explore whether calculating dictionary letter frequencies vs text letter frequencies improves guessing results. Another possibility is to use letter frequencies from historical Wordle answers... maybe worth exploring.
