def guess_next_letter(pattern='', used_letters=[], word_list=[]):
    """ Returns a letter from the alphabet
    :param pattern: current state of the game board, with underscores "_" in the
           places of spaces (for example, "____e", that is, four underscores followed by 'e').
    :param used_letters: letters you have guessed in previous turns for the same word (for example,
           ['a', 'e', 's']).
    :param word_list: list of words from which the game word is drawn.
    :return:
    """
    if len(pattern) < 1 or len(used_letters) < 1 or len(word_list) < 1:
        return ''

    possible_letters_dict = {}  # possible letters in the dict
    temp_letters_dict = {}      # temp dict for possible letters
    p_len = len(pattern)        # ____t 5
    max_count = 0               # max count for possible letter
    possible_letter = ''        # possible letter

    for word in word_list:
        if len(word) != p_len:  # length is not matched with that of pattern
            print("continue word:" + word)
            continue

        pos = 0  # for the position of word
        matched = True  # whether totally matched with pattern
        for ch in pattern:
            # print("ch:" + ch)
            # print("word[pos]:" + word[pos])
            if ch != '_' and ch != word[pos]:
                matched = False
                break
            if ch == '_' and word[pos] in used_letters:  # should not include used letters
                matched = False
                break
            if ch == '_':
                temp_letters_dict.setdefault(word[pos], 0)
                temp_letters_dict[word[pos]] += 1

            pos += 1

        print(temp_letters_dict)
        # the word is matched with pattern,
        # putting possible letters into the dict and increasing the count for each letter,
        # and the letter with max count will be the possible letter.
        if matched:
            for key in temp_letters_dict:
                print("key:" + key)
                # a b u o
                possible_letters_dict.setdefault(key, 0)
                possible_letters_dict[key] += temp_letters_dict[key]
                # print(possible_letters_dict)
                # print(max_count)
                if possible_letters_dict[key] > max_count:
                    max_count = possible_letters_dict[key]
                    possible_letter = key

        temp_letters_dict.clear()
    print("ok, the letter:" + possible_letter)
    return possible_letter


if __name__ == '__main__':

    game_word_list = ['about', 'abound', 'abundant', 'python', 'hangman']
    letter = guess_next_letter(pattern='____t', used_letters=['c', 'e', 's'], word_list=game_word_list)
    print("possible letter is: %s" % letter)

    letter = guess_next_letter(pattern='a___t', used_letters=['c', 'e', 's'], word_list=game_word_list)
    print("possible letter is: %s" % letter)

    letter = guess_next_letter(pattern='ab__t', used_letters=['c', 'e', 's'], word_list=game_word_list)
    print("possible letter is: %s" % letter)

    letter = guess_next_letter(pattern='abo_t', used_letters=['c', 'e', 's'], word_list=game_word_list)
    print("possible letter is: %s" % letter)

    letter = guess_next_letter(pattern='about', used_letters=['c', 'e', 's'], word_list=game_word_list)
    print("possible letter is: %s" % letter)

    letter = guess_next_letter(pattern='_______t', used_letters=['a'], word_list=game_word_list)
    print("possible letter is: %s" % letter)