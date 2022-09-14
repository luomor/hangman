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
            continue

        pos = 0  # for the position of word
        matched = True  # whether totally matched with pattern
        for ch in pattern:
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

        # the word is matched with pattern,
        # putting possible letters into the dict and increasing the count for each letter,
        # and the letter with max count will be the possible letter.
        if matched:
            for key in temp_letters_dict:
                possible_letters_dict.setdefault(key, 0)
                possible_letters_dict[key] += temp_letters_dict[key]
                if possible_letters_dict[key] > max_count:
                    max_count = possible_letters_dict[key]
                    possible_letter = key

        temp_letters_dict.clear()
    print("ok,the letter:" + possible_letter)
    return possible_letter


if __name__ == '__main__':

    game_word_list = ['about', 'abound', 'abundant', 'python', 'hangman']
    letter = guess_next_letter(pattern='____t', used_letters=['c', 'e', 's'], word_list=game_word_list)
    print("possible letter is: %s" % letter)

    letter = guess_next_letter(pattern='____t', used_letters=['a', 'c', 'e', 's'], word_list=game_word_list)
    print("possible letter is: %s" % letter)

    letter = guess_next_letter(pattern='____t', used_letters=['a', 'b', 'c', 'e', 's'], word_list=game_word_list)
    print("possible letter is: %s" % letter)