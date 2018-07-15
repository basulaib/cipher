
ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the
# code that you submit.  Do not use break or continue statements.


def clean_message(message):
    """ (str) -> str

    Return a message that only includes uppercase alphabetical characters.

    >>> clean_message('good morning')
    'GOODMORNING'
    >>> clean_message('1975 commercial')
    'COMMERCIAL'
    """
    new_message = ''

    for char in message:
        if char.isalpha():
            new_message += char.upper()
    return new_message


def encrypt_letter(letter, value):
    """ (str, int) -> str

    Precondition: len(letter) == 1 and letter.isupper()

    Returns the letter as an encrypted letter by applying the keystream value.

    >>> encrypt_letter('F', 10)
    'P'
    >>> encrypt_letter('Z', 19)
    'S'
    """
    # Change the letter to a number in the range 0-25. 'A' changes to 0, 'B'
    # changes to 1, 'C' changes to 2 and so on...
    # After changing the number, we add it to the keystream value given, and
    # we use modulo 26 to handle the end of the alphabet.
    i = ((ord(letter) - ord('A')) + value) % 26

    return chr(ord('A') + i)


def decrypt_letter(letter, value):
    """ (str, int) -> str

    Precondition: len(letter) == 1 and letter.isupper()

    Returns the letter as a decrypted letter by applying the keystream value.

    >>> decrypt_letter('P', 10)
    'F'
    >>> decrypt_letter('S', 19)
    'Z'
    """
    # Change the letter to a number as described in encrypt_letter.
    i = ((ord(letter) - ord('A')) - value) % 26

    return chr(ord('A') + i)


def swap_cards(deck, cut):
    """ (list of int, int) -> NoneType

    Swap the card at the index (cut) of the deck with the card that follows it.

    >>> deck = [2, 1, 5, 8, 9, 7, 3, 2, 1, 4]
    >>> swap_cards(deck, 6)
    >>> deck
    [2, 1, 5, 8, 9, 7, 2, 3, 1, 4]

    >>> deck = [1, 5, 3, 4, 6, 2, 9, 10, 7, 8, 11, 13, 12]
    >>> swap_cards(deck, 9)
    >>> deck
    [1, 5, 3, 4, 6, 2, 9, 10, 7, 11, 8, 13, 12]
    """

    card = deck[cut]

    if deck[cut] == deck[-1]:
        # If the given index matches the last card's index, then it will swap
        # the last card in the deck with the first card as we are treating
        # the deck as circular.
        deck[cut] = deck[0]
        deck[0] = card

    else:
        # If it doesn't match the last card's index, it will simply swap the
        # card at given index, with the card that follows it.
        deck[cut] = deck[cut + 1]
        deck[cut + 1] = card


def get_small_joker_value(deck):
    """ (list of int) -> int

    Gets the value of the small joker, which is the second highest value in
    the deck.

    >>> get_small_joker_value([1, 3, 2, 5, 4])
    4
    >>> get_small_joker_value([6, 4, 10, 8, 9, 2, 5, 1, 7, 13, 11, 12, 14, 18,
    15, 17, 16, 3])
    17
    """

    return max(deck) - 1


def get_big_joker_value(deck):
    """ (list of int) -> int

    Gets the value of the big joker, which is the highest value in the deck.

    >>> get_big_joker_value([1, 3, 2, 5, 4])
    5
    >>> get_big_joker_value([1, 3, 2, 5, 4, 8, 6, 7])
    8
    """

    return max(deck)


def move_small_joker(deck):
    """ (list of int) -> NoneType

    Swaps the small joker with the card that follows it. If the small joker is
    the last card in the deck, then it becomes the first as we are treating
    the deck as circular.

    >>> deck = [2, 4, 1, 3, 5, 6, 9, 8, 10, 7]
    >>> move_small_joker(deck)
    >>> deck
    [2, 4, 1, 3, 5, 6, 8, 9, 10, 7]

    >>> deck = [6, 7, 2, 1, 3, 4, 15, 16, 8, 9, 10, 12, 5, 11, 13, 14]
    >>> move_small_joker(deck)
    >>> deck
    [6, 7, 2, 1, 3, 4, 16, 15, 8, 9, 10, 12, 5, 11, 13, 14]
    """
    # This will find the value of the small joker, and the index of the card
    # at the value of the small joker and then swap them.
    small_joker = get_small_joker_value(deck)
    card_swap = deck.index(small_joker)

    swap_cards(deck, card_swap)


def move_big_joker(deck):
    """ (list of int) -> NoneType

    Moves the big joker two cards down the deck. We also treat the deck as
    circular.

    >>> deck = [1, 2, 3, 4, 5, 6, 7, 10, 8, 9]
    >>> move_big_joker(deck)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> deck = [5, 6, 7, 8, 4, 3, 2, 1, 9, 10]
    >>> move_big_joker(deck)
    >>> deck
    [6, 10, 7, 8, 4, 3, 2, 1, 9, 5]
    """
    # This will move the big joker by performing two card swaps.
    # We treat the deck as circular. If the big_joker is the last card in the
    # deck, then it will move to be the 2nd as the two card swaps are
    # performed.

    big_joker = get_big_joker_value(deck)
    swap_cards(deck, deck.index(big_joker))
    swap_cards(deck, deck.index(big_joker))


def triple_cut(deck):
    """ (list of int) -> NoneType

    This will perform the triple cut on the given deck of cards. The joker that
    is closest to the top of the deck is called the first joker and the one
    closest to the bottom of the deck is called the second joker. This function
    will swap the cards above the first joker with the cards below the second
    joker.

    >>> deck = [1, 2, 3, 10, 5, 6, 7, 4, 9, 8]
    >>> triple_cut(deck)
    >>> deck
    [8, 10, 5, 6, 7, 4, 9, 1, 2, 3]

    >>> deck = [5, 6, 7, 8, 9, 10, 14, 1, 2, 3, 4, 13, 11, 12]
    >>> triple_cut(deck)
    >>> deck
    [11, 12, 14, 1, 2, 3, 4, 13, 5, 6, 7, 8, 9, 10]
    """
    # This will find the value of the big joker and the index of the big joker.
    big_joker = get_big_joker_value(deck)
    bj_index = deck.index(big_joker)

    # This will find the value of the small joker and the index of it.
    small_joker = get_small_joker_value(deck)
    sj_index = deck.index(small_joker)

    # If the small joker index is greater than the big joker, that means
    # the big joker is the first joker and the small joker is the second joker.
    if bj_index < sj_index:
        new_deck = deck[sj_index + 1:] + deck[bj_index:sj_index + 1] + deck[:bj_index]
        deck.clear()
        for value in new_deck:
            deck.append(value)

    # If the big joker index is greater than the small joker, that means the
    # small joker is the first joker and the big joker is the second joker.
    if bj_index > sj_index:
        new_deck = deck[bj_index + 1:] + deck[sj_index:bj_index + 1] + deck[:sj_index]
        deck.clear()
        for value in new_deck:
            deck.append(value)


def insert_top_to_bottom(deck):
    """ (list of int) -> NoneType

    Examines the value of the bottom card of the deck; move that many cards
    from the top of the deck to the bottom, inserting them just above the bottom
    card. If the bottom card is the big joker, use the value of the small joker
    instead.

    >>> deck = [1, 2, 3, 4, 5, 6, 7, 10, 9, 8]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [9, 1, 2, 3, 4, 5, 6, 7, 10, 8]

    >>> deck = [5, 6, 7, 8, 9, 10, 14, 1, 2, 3, 4, 13, 11, 12]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [11, 5, 6, 7, 8, 9, 10, 14, 1, 2, 3, 4, 13, 12]
    """
    # This is the special case of this function. This basically means that if
    # the value of the last card is the big joker, then take the value of the
    # small joker instead and insert the top cards to the bottom of the deck.
    if deck[-1] == max(deck):
        value = max(deck) - 1
        new_deck = deck[value: -1] + deck[:value] + deck[-1:]
        deck.clear()
        for value in new_deck:
            deck.append(value)

    # If it's not the value of the big joker, then simply insert the number of
    # cards from top to the bottom of the deck.
    else:
        value = deck[-1]
        new_deck = deck[value: -1] + deck[:value] + deck[-1:]

        deck.clear()
        for value in new_deck:
            deck.append(value)


def get_card_at_top_index(deck):
    """ (list of int) -> int

    Using the value of the top card as an index, return the card in the deck at
    that index. If the top card is a big joker, then use the value of the small
    joker instead.

    >>> deck = [1, 2, 3, 4, 5, 6, 7, 10, 9, 8]
    >>> get_card_at_top_index(deck)
    2

    >>> deck = [5, 6, 7, 8, 9, 10, 14, 1, 2, 3, 4, 13, 11, 12]
    >>> get_card_at_top_index(deck)
    10
    """
    # This is again, the special case of this function.
    if deck[0] == max(deck):
        value = max(deck) - 1
        card = deck[value]
    # This will simply get the card using the top card's index.
    else:
        value = deck[0]
        card = deck[value]

    return card


def get_next_keystream_value(deck):
    """ (list of int) -> int

    This function will repeat the five steps of the algorithm (Move small joker,
    move big joker, triple cut, insert top to bottom and get card at top index)
    to generate the next keystream value.

    >>> deck = [6, 7, 2, 1, 3, 4, 15, 16, 8, 9, 10, 12, 5, 11, 13, 14]
    >>> get_next_keystream_value(deck)
    9

    >>> deck = [5, 6, 7, 8, 9, 10, 14, 1, 2, 3, 4, 13, 11, 12]
    >>> get_next_keystream_value(deck)
    12
    """
    # We recall the five steps of the algorithm to generate the next keystream
    # value.
    move_small_joker(deck)
    move_big_joker(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    keystream_value = get_card_at_top_index(deck)

    # If the keystream value is the big or small joker, then the algorithm
    # restarts again.
    while keystream_value == max(deck) or keystream_value == max(deck) - 1:
        move_small_joker(deck)
        move_big_joker(deck)
        triple_cut(deck)
        insert_top_to_bottom(deck)
        keystream_value = get_card_at_top_index(deck)
    return keystream_value


def process_messages(deck, messages, command):
    """(list of int, list of str, str) -> list of str

    Return a list of encrypted or decrypted messages, in the same order as they
    appear in the given list of messages.

    >>> file = open('deck1.txt', 'r')
    >>> deck = read_deck(file)
    >>> file = open('secret7.txt', 'r')
    >>> message = read_messages(file)
    >>> process_messages(deck, message, DECRYPT)
    ['DOABARRELROLL']

    >>> file = open('deck1.txt', 'r')
    >>> deck = read_deck(file)
    >>> file = open(secret5.txt', 'r')
    >>> message = read_messages(file)
    >>> process_messages(deck, message, DECRYPT)
    ['THECAKEISALIE']
    """
    # If the command is encrypt, it will basically encrypt the message.
    if command == ENCRYPT:
        new_str, encrypt = [], []
        for message in messages:
            new_str.append(clean_message(message))
        for word in new_str:
            for letter in word:
                keystream = get_next_keystream_value(deck)
                encrypt.append(encrypt_letter(letter, keystream))
        # This will take every word in new_str and and add it to the new
        # encrypted message and return the list of strings.
        new_e = []
        for word in new_str:
            new_e.append(''.join(encrypt[0:len(word)]))
            del encrypt[0:len(word)]
        return new_e
    # The same applies to the command decrypt.
    elif command == DECRYPT:
        decrypt = []
        for word in messages:
            for letter in word:
                keystream = get_next_keystream_value(deck)
                decrypt.append(decrypt_letter(letter, keystream))

        new_d = []
        for word in messages:
            new_d.append(''.join(decrypt[0:len(word)]))
            del decrypt[0:len(word)]
        return new_d


def is_valid_deck(deck):
    """(list of int) -> bool

    Checks if the given deck of card is valid.

    >>> deck = [5, 6, 7, 8, 9, 10, 14, 1, 2, 3, 4, 13, 11, 12]
    True
    >>> deck = [1, 2, 3, 5]
    False
    """

    valid_deck = []

    valid_deck = sorted(deck)

    for i in range(1, len(deck)):
        if i not in valid_deck:
            return False
    return True


def read_messages(file):
    """(file open for reading) -> list of str

    Read and return the contents of the file as a list of messages, in the order
    in which they appear in the file.
    """

    messages = []
    for line in file.readlines():
        messages.append(line.strip())
    return messages


def read_deck(file):
    """(file open for reading) -> list of int

    Read and return the numbers that are in the file, in the order in which they
    appear in the file.
    """

    numbers = []
    for line in file:
        line = line.split()
        for num in line:
            numbers.append(int(num.strip()))
    return numbers
