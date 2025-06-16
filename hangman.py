import random

def get_word():
    while True:
        error = False
        accepted_letters = "abcdefghijklmnopqrstuvwxyz"
        word = input('Enter a word: ')
        word = word.lower()
        for char in word:
            if char not in accepted_letters:
                error = True
        if error:
            print("sorry no spaces, numbers, or special characters allowed")
        else:
            return word
            break


def start_game(word):
    for i in range(20):
        print("hide "*10)
    print("...." * 10)
    show_word = []
    for _ in word:
        show_word.append("?")
    already_guessed = []
    lives = 5
    word = list(word)
    x = ""
    while show_word != word and lives != 0:
        rand = random.randint(1,10)
        print("The word is... ", "".join(show_word))
        guess = input("guess a letter then press enter: ")
        print("<><>"*10)
        already_guessed.append(guess.upper())
        indices = [i for i, x in enumerate(word) if x == guess]
        if guess in word:
            for i in indices:
                show_word[i] = guess
            print("Good Guess")
            if rand == 1:
                lives += 1
                print("wow lucky you, there was an extra life on that letter")
        else:
            print("Nope Not That Letter")
            lives -= 1

        print(f"you've guessed these letters:\n{already_guessed}")
        print(f"lives left:\n{lives}")

        print("...." * 10)

    if lives == 0:
        print("oof looks like your out of lives you lost better luck next time")
    else:
        print("Congrats! You Won!")

    print("The word was...")
    print(''.join(word).upper())


start_game(get_word())
