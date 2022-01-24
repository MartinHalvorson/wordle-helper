'''
method(
correct spot['', '', '', '', '']
wrong spots['', '', '', '', '']
wrong letters[''])

incorporate letter frequencies
'''

with open('all_words.txt', 'r+') as f:
    data = f.read().replace(' ', '').split('\n')
    for i, word in enumerate(data):
        for letter in word:
            if letter in '1234567890&-\'./,' or len(word) != 5:
                data[i] = ''
    data = [x.lower() for x in data if len(x) == 5]
    with open('five_letter_words.txt', 'w+') as g:
        g.write('\n'.join(data))




