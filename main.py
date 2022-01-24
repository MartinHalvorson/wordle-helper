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


# correct_spots: ['s', 't', '', '', '']
# wrong_spots: ['', '', '', 'a', 'r']
# wrong_letters: 'xgn'
def potential_word(word, green, yellow, gray):
    for i, letter in enumerate(green):
        if (letter != '' and word[i] != letter) or word[i] in yellow[i] or word[i] in gray:
            return False
    for letter in ''.join(yellow):  # Letters in wrong spots must be present in the word though
        if letter not in word:
            return False
    return True


def wordle_helper(green, yellow, gray):
    with open('five_letter_words.txt', 'r') as f:
        all_words = f.read().split('\n')
        valid_words = [word for word in all_words if potential_word(word, green, yellow, gray)]
        print(valid_words)


correct_spots = ['s', '', '', '', '']  # Green letters
wrong_spots = ['', 'a', 'm', 'm', 'm']  # Yellow letters
wrong_letters = 'c'  # Gray letters

wordle_helper(correct_spots, wrong_spots, wrong_letters)




'''
method(
correct spots['', '', '', '', '']
wrong spots['', '', '', '', '']
wrong letters[''])

determine valid words
take letter frequencies of valid words
make a list of words with highest letter frequencies (ignore bonus from repeated letters)
make recommendation

incorporate letter frequencies
'''

