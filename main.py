text_relative_frequencies = {'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.13, 'f': 0.022, 'g': 0.02,
                             'h': 0.061, 'i': 0.07, 'j': 0.0015, 'k': 0.0077, 'l': 0.04, 'm': 0.025, 'n': 0.067,
                             'o': 0.075, 'p': 0.019, 'q': 0.00095, 'r': 0.06, 's': 0.063, 't': 0.091, 'u': 0.028,
                             'v': 0.0098, 'w': 0.024, 'x': 0.0015, 'y': 0.02, 'z': 0.00074}


# Uses word file of all English words and produces word file of all five letter English words (lowercase)
def all_words_to_five_letter_words():
    with open('all_words.txt', 'r+') as f:
        data = f.read().replace(' ', '').split('\n')
        for i, word in enumerate(data):
            for letter in word:
                if letter in '1234567890&-\'./,' or len(word) != 5:
                    data[i] = ''
        data = [x.lower() for x in data if len(x) == 5]
        with open('five_letter_words.txt', 'w+') as g:
            g.write('\n'.join(data))
    return


# Given the known information, is this word a valid potential word? Returns True/False
def potential_word(word, green, yellow, gray):
    for i, letter in enumerate(green):
        if (letter != '' and word[i] != letter) or word[i] in yellow[i] or word[i] in gray:
            return False
    for letter in ''.join(yellow):  # Letters in wrong spots must be present in the word though
        if letter not in word:
            return False
    return True


# Calculates the frequency score of a word based on the letters in the other valid words
# Only counts repeated letters once
def calculate_word_score(word, frequencies):
    letters = [x for i, x in enumerate(word) if word.index(x) == i]
    return sum(frequencies.get(x, 0) for x in letters) + sum(text_relative_frequencies[x] for x in letters)


# Takes a list of valid words and returns a sorted list of valid words based on letter-frequency of the original list
def order_by_frequency(valid_words):
    frequencies = {}
    for word in valid_words:
        for letter in word:
            frequencies[letter] = frequencies.get(letter, 0) + 1
    total = sum(frequencies.values())
    for letter in frequencies.keys():
        frequencies[letter] /= total
    scored_list = [(word, calculate_word_score(word, frequencies)) for word in valid_words]
    scored_list.sort(key=lambda x: x[1], reverse=True)
    return scored_list


# Takes known information, produces a list of valid words. Also produces frequencies of letters in remaining valid words
# and returns an ordered list of high letter-frequency words to help gather maximum information with future clues.
def wordle_helper(green, yellow, gray):
    with open('five_letter_words.txt', 'r') as f:
        all_words = f.read().split('\n')
        valid_words = [word for word in all_words if potential_word(word, green, yellow, gray)]
        return order_by_frequency(valid_words)


correct_spots = ['', '', '', '', '']  # Green letters
wrong_spots = ['', '', '', '', '']  # Yellow letters
wrong_letters = ''  # Gray letters

scored_list = wordle_helper(correct_spots, wrong_spots, wrong_letters)
for word, score in scored_list[:20]:  # Only prints the top 20 words
    print(word, score)
