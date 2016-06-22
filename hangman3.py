from random import choice

#definition of functions:

def encode_word_to_find(word_to_find):

    encode_word_list = list(word_to_find)

    for i in range(0, len(encode_word_list)):
        encode_word_list[i] = "_ "

    return encode_word_list

def choose_word(word_list):

    word_to_find = choice(word_list)
    return word_to_find

def round_initialise(this_rounds_word):

    display_lines = encode_word_to_find(this_rounds_word)

    return display_lines

def get_search_char(list_of_guesses):

    user_input = input("Guess a letter:")

    user_input = user_input.lower()

    if len(user_input) != 1:
        print("Choose ONE letter!")

    if user_input.isalpha() == False:
        print("Choose a letter, not a number!")

    if user_input in list_of_guesses:
        print("You've tried that letter already!")

    else:
        return user_input

def check_search_char(search_char, word_to_find, display_lines):

    for i in range(0, len(word_to_find)):

        if search_char == word_to_find[i]:
            display_lines[i] = search_char + " "

    print("".join(display_lines))
    return display_lines

def play_a_round():
    word_list = []

    with open('/Users/D_Admin/Desktop/new_hangman_list.txt', 'r') as f:
        for line in f:
            for word in line.split():
                word_list.append(word)

    # Set list_of_guesses to an empty list:
    list_of_guesses = []

    # Reset number_of_guesses to 5:
    number_of_guesses = 5

    # Get a word for this round:
    this_rounds_word = choose_word(word_list)

    # Set up the letter lines:
    display_lines = round_initialise(this_rounds_word)
    print("".join(display_lines))

    # Play the game:
    while "_ " in display_lines:

        # show how many guesses are left:
        print("You have %s guesses left." % number_of_guesses)

        # get user input, and check it:
        search_char = get_search_char(list_of_guesses)

        # add item to list_of_guesses, if there is anything to add (i.e. if search_char is set), and check for game end:
        if search_char:
            if search_char.isnumeric() == False:

                if search_char not in this_rounds_word:
                    list_of_guesses.append(search_char)
                    number_of_guesses -= 1
                    # the user lost:
                    if number_of_guesses == 0:
                        print("Game over! You lose this time.")
                        print("The word was:")
                        print("".join(this_rounds_word))
                        #ask if they want to play again:
                        want_to_play()

                        break
        # display guesses, if there is one:
        if list_of_guesses:
            print("Your wrong guesses:")
            print(" ".join(list_of_guesses))

        # check to see if user's guess is in the word:
        check_search_char(search_char, this_rounds_word, display_lines)

    # If the user won that round:
    if "_ " not in display_lines:
        print("You solved it!")
        print("The word was:")
        print("".join(this_rounds_word))
        #ask if they want to play again:
        want_to_play()

def want_to_play():

    play_now = str(input("Another round? Y/N?"))
    play_now = play_now.lower()
    if len(play_now) != 1:
        print("Type Y or N only!")

    if play_now.isalpha() == False:
        print("Type Y or N, not a number!")

    if play_now == "y":

        play_a_round()

    elif play_now == "n":

        print("Goodbye!")

#main program:

play_a_round()





