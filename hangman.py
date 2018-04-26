import random
import read_me  # Module with list of 3 letter words


def hangman(word):
    wrong = 0
    stages = ["",
              "______     ",
              "|    |     ",
              "|    |     ",
              "|    O     ",
              "|   /|\    ",
              "|   / \    ",
              "|          "]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! The word was {}.".format(word))


# Challenge 1
pool = len(read_me.pool)  # get number of words
# print(pool)
rnd_wrd = read_me.pool[random.randint(0, pool - 1)]  # pick random word from list
# print("Debug:" + str(rnd_wrd))
hangman(rnd_wrd)
