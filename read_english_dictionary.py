from string import ascii_lowercase


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = word_file.read().split('\n')
    return valid_words


if __name__ == '__main__':
    # 370100 words in list
    ALLWORDS = load_words()
    pairs = {}
    # Generated Letter Pairings prioritizing reverse commonality (Z 1st etc): "zqxjkvbpygfwmucldrhsnioate"
    # This gives Z the most combinations and E the least when creating summed pairs (ZE vs EZ)
    # when generating both_pairs
    for x in "zqxjkvbpygfwmucldrhsnioate":
        for y in "zqxjkvbpygfwmucldrhsnioate":
            if x != y:
                pairs[x+y] = 0

    for x in ALLWORDS:
        x = x.lower()
        for i in range(len(x)-1):
            if (x[i:i+2] in pairs):
                pairs[x[i:i+2]] = pairs.get(x[i:i+2]) + 1
    both_pairs = {}
    for x in pairs:
        if not(x in both_pairs) and not(x[::-1] in both_pairs):
            both_pairs[x] = pairs.get(x)+pairs.get(x[::-1])

    buttons = {}
    keys = sorted(both_pairs)[::-1]
    for x in "zqxjkvbpygfwmucldrhsnioate":
        button_pair = ""
        button_score = 1000000
        for y in keys:
            if x in y:
                if both_pairs.get(y) < button_score:
                    button_pair = y
                    button_score = both_pairs.get(y)
                keys = [z for z in keys if z != y]
        if (button_pair != ""):
            buttons[button_pair] = {button_score}
        for y in keys:
            if (button_pair != ""):
                if (button_pair[1] in y):
                    keys = [z for z in keys if z != y]
    # For Excel Analysis:
    # for x in sorted(both_pairs):
    #     print(x,both_pairs.get(x))
    # for x in sorted(both_pairs):
    #     print(x)
    # for x in sorted(both_pairs):
    #     print(both_pairs.get(x))
    for x in sorted(buttons):
        print(x, buttons.get(x))
    # for x in sorted(buttons):
    #     print(x)
    # for x in sorted(buttons):
    #     print(buttons.get(x))
