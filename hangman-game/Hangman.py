import random as rd

words = ("apple","mango","orange","banana","lemon","pears","kiwi")

hangman_art= {0: (" ========= ",
                  " |    |    ",
                  " |         ",
                  " |         ",
                  " |         ",
                  " |         ",
                  "_|________"),

              1:  (" ======== ",
                  " |    |    ",
                  " |    o    ",
                  " |         ",
                  " |         ",
                  " |         ",
                  "_|________"),
              2: (" ========= ",
                  " |    |    ",
                  " |    o    ",
                  " |    |    ",
                  " |         ",
                  " |         ",
                  "_|________"),
              3: (" ========= ",
                  " |    |    ",
                  " |    o    ",
                  " |   /|    ",
                  " |         ",
                  " |         ",
                  "_|________"),
              4: (" ========= ",
                  " |    |    ",
                  " |    o    ",
                  " |   /|\\  ",
                  " |         ",
                  " |         ",
                  "_|________"),
              5: (" ========= ",
                  " |    |    ",
                  " |    o    ",
                  " |   /|\\  ",
                  " |   /     ",
                  " |         ",
                  "_|________"),
              6: (" ========= ",
                  " |    |    ",
                  " |    o    ",
                  " |   /|\\  ",
                  " |   / \\  ",
                  " |         ",
                  "_|________")}
def display_man(wrong_guesses):
    print("-----------------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
def display_hint(hint):
    print(" ".join(hint))
def display_ans(answer):
    print(" ".join(answer))
def main():
    print("  Welcome To Hangman Game  ")
    while True:
        answer = rd.choice(words)
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()
        is_running = True
        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)

            guess = input("Enter a letter : ").lower()
            if len(guess)  != 1 or not guess.isalpha():
                print("Invalid Input")
                continue
            if guess in guessed_letters:
                print(f"{guess} had already guessed!")
                continue
            guessed_letters.add(guess)
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i]  == guess :
                        hint[i] = guess
            else:
                wrong_guesses += 1
            if "_" not in hint:
                display_man(wrong_guesses)
                print(f"The Correct answer was : {answer}")
                print("You WIN!")
                is_running = False
            elif wrong_guesses >= len(hangman_art) - 1 :
                display_man(wrong_guesses)
                print(f"The Correct answer was : {answer}")
                print("You LOSE!")
                is_running = False
        if input("Wanna Play Again ? (y/n) ") != "y":
            break
if __name__ == "__main__":
    main()
