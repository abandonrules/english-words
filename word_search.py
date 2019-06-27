word_file_path = 'words.txt'

def filter(word, letters=None, length=None, positions=None):
    found = True

    if length is not None and len(word) != length:
        return False

    if letters is not None:
        try:
            letters = list(letters.lower())
            for letter in word:
                letters.remove(letter)
        except:
            return False

    if positions is not None:
        for key in positions:
            if word[key - 1] is not positions[key]:
                return False

    return found

i_letters = input("Letters: ")

while True:
    i_num_letters = int(input("Num. of letters (0 to quit): "))

    if i_num_letters == 0: break

    dict_pos = {}
    for i in range(1, i_num_letters + 1):
        letter_at_pos = None
        letter_at_pos = input("Letter at position {:d}: ".format(i))
        if letter_at_pos is not '':
            dict_pos[i] = letter_at_pos

    with open(word_file_path, 'r') as word_file:
        for line in word_file:
            word = line.strip().lower()
            if filter(word, i_letters, i_num_letters, dict_pos):
                print(word)
