
import hangman_art
import hangman_words
import random

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
valid_letters = "abcdefghijklmnopqrstuvwxyz"
end_of_game = False
lives = 6
print("To see the solution enter secret code")
print(hangman_art.logo)
letters_guessed = ''
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess == "12345678":
        print(f'Pssst, the solution is {chosen_word}.')
        continue
    if guess not in valid_letters:
        print("Not valid letter")
        continue
    if guess in letters_guessed:
        print(guess+" alredy guessed this letter before")
        continue
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    letters_guessed+=guess

    if guess not in chosen_word:
        print("Wrong "+guess)
        lives -= 1

    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You win.")
    if lives == 0:
            end_of_game = True
            print("You lose.")
