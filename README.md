# Wordle Helper!

A guess generating aid for playing the game [Wordle](https://www.powerlanguage.co.uk/wordle/)! 

_Note: This small project is just for my own fun and if I post results from this anywhere I make it clear that the results were produced with the aid of a computer. By no means am I trying to ruin the spirit of Wordle!_

## How to Use:
For now (and probably always) it just writes to the CLI. There are a few different capabilities in Wordle Helper:
### **Single Guess Helper** 
Input known information (green, yellow, gray letters) in the correct spots and have Wordle Helper help you pick your next word (the algorithm/scoring system is explained a bit more below). You can uncomment the code below at the bottom of the file _main.py_ (or just copy and paste from here). Fill in the letters in the correct spots and run _main.py_!
```
correct_spots = ['', '', '', '', '']  # Green letters
wrong_spots = ['', '', '', '', '']  # Yellow letters
wrong_letters = ''  # Gray letters
next_guess_count = 1  # e.g. 1 -> 1st guess

scored_list = wordle_helper(correct_spots, wrong_spots, wrong_letters, next_guess_count)
for word, score in scored_list[:20]:  # Only prints the top 20 words
    print(word, score)
```
### **Simulate Guessing a Wordle (Multi Guess)** 
Using the _simulate_word(word)_ function, you can simulate continuous guesses until the Wordle is guessed. The output is a list of every guess, (hopefully) ending with the Wordle!

In **main.py**:
```
simulate_single_word('apple')
simulate_single_word('enjoy')
```
Output:
```
Guesses:  ['arose', 'alien', 'amble', 'apple']
Guesses:  ['arose', 'noted', 'enjoy']
```
### **Simulate Guessing Many Wordles** 
To test the above function across many Wordles, fill the file **past_answers.txt** with Wordles and run the function _calculate_average_guess_metric()_ in **main.py**. You can also specify the number of Wordles to simulate.

Calculating an "average # of guesses" metric across many words is useful for benchmarking and measuring improvements to the simulator.

In **main.py**:
```
simulate_many_words(10)
```
Output:
```
Inputs:  ['solar', 'shire', 'proxy', 'point', 'robot', 'prick', 'wince', 'crimp', 'knoll', 'sugar']
Guesses:  ['arose', 'solar']
Guesses:  ['arose', 'shirt', 'shire']
Guesses:  ['arose', 'until', 'broch', 'proxy']
Guesses:  ['arose', 'tonic', 'point']
Guesses:  ['arose', 'intro', 'throw', 'robot']
Guesses:  ['arose', 'until', 'crimp', 'prick']
Guesses:  ['arose', 'until', 'hinge', 'mince', 'vince', 'wince']
Guesses:  ['arose', 'until', 'crimp']
Guesses:  ['arose', 'until', 'knoll']
Guesses:  ['arose', 'stair', 'sugar']
Average Num Guesses per Wordle: 3.5
Max Num Guesses: 6   Word: wince
Distribution:
	 1 guess(es): 0
	 2 guess(es): 1
	 3 guess(es): 5
	 4 guess(es): 3
	 5 guess(es): 0
	 6 guess(es): 1
```
