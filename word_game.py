import argparse
import collections
import copy

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def init(req, other):
    c = collections.Counter(list(other))
    c.update([req])
    return c

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Stupid word game solver')
    parser.add_argument("req", help="Required character.")
    parser.add_argument("other", help="All the other stuff.")
    args = parser.parse_args()

    col = init(args.req, args.other)
    english_words = load_words()

    found = []

    for word in english_words:
        word_length = len(word)
        if word_length < 4 or word_length > 9:
            continue
        temp = copy.deepcopy(col)
        valid = True

        for letter in word:
            if letter not in temp or temp[letter] == 0:
                valid = False
                break

            temp[letter] -= 1

        if valid and temp[args.req] == 0:
            found.append(word)

    print(found)
