# wordle-helper

In main.py at the bottom, fill in known information in correct_spots, wrong_spots, and wrong_letters and run main.py.
Continue adding new known information to narrow down potential words.


Notes:
The original dictionary I used contains a lot of words that probably aren't really going to be picked as Wordle words so I could potentially find a better source dictionary to use.

Future improvements:
Find a better OG dictionary
Improve sourcing algo for calculating letter frequencies


v1 - Past results (from always guessing the first recommended word)
#214 - POINT (aires, louin, doing, joint, point)
#213 - PROXY (aires, yourt, droyl, crony, frowy, grovy, proxy)
#212 - SHIRE (aires, reist, shire)
#211 - SOLAR (aires, rosat, sofar, solar)
#210 - PANIC (aires, lanti, canid, manic, panic)
#209 - TANGY (aires, laton, tangy)
One optimization
* Early guesses should prioritize maximizing information over attempting to guess actual words
* Later guesses should attempt to guess actual words
* (v1 always just guesses based on trying to maximize information)
