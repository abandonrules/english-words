def load_words():
    with open('words_alpha.txt') as word_file:
    # valid_words = set(word_file.read().split())
        valid_words = word_file.read().split('\n')

    return valid_words


if __name__ == '__main__':
    ALLWORDS = load_words()
    pairs = {}
    # print(len(ALLWORDS))
    # 370100 words in list

    for x in ALLWORDS:
        x = x.lower()
        print(x)
        for i in range(len(x)-1):
            if (x[i:i+2] in pairs):
                pairs[x[i:i+2]] = pairs.get(x[i:i+2]) + 1
            else:
                pairs[x[i:i+2]] = 1

    minimumCount = 10000
    for pair in sorted(pairs):
        if pairs.get(pair) > minimumCount:
            print(pair, pairs.get(pair))
