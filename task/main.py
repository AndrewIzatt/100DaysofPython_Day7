import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[1]
# chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder=""
for char in range(len(chosen_word)):
    placeholder += "_"

display = list(placeholder)

guess = input("Guess a letter:\n").lower()
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
counter = 0
for letter in chosen_word:
    print(f"The letter is: {letter}\n")
    print(f"The index is: {counter}\n")
    if letter == guess:
        display[counter] = letter
        print("Right\n")
    else:
        print("Wrong")
    print(f"The display is currently: {display}\n")
    counter +=1


