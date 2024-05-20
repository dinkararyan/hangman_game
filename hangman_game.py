from visual import lives_visual_dict
from word_list import words
import random
import string

def get_word(words):
    word = random.choice(words)
    return word.upper()

def game():
    word = get_word(words)
    word_letter = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    turns = 7

    while turns>0 and len(word_letter)>0:
        print(f"You have {turns} turns left.\n You have choosen the following letters so far : {' '.join(used_letters)}\n")

        current_word = []
        for letter in word:
            if letter in used_letters:
                current_word.append(letter)
            else:
                current_word.append("-")
        
        print(lives_visual_dict[turns])
        print(f"Current word is : {' '.join(current_word)}")

        user_choice = input(f"Enter a letter from the following letter {alphabets}\n")
        user_choice = user_choice.upper()

        if user_choice not in alphabets:
            print(f"The letter has already been selected !!\n")
            print(f"Please enter the letter from within the following alphabets {alphabets}\n")

        elif user_choice in word_letter:
            word_letter.remove(user_choice)
            used_letters.add(user_choice)
            alphabets.remove(user_choice)

        else:
            used_letters.add(user_choice)
            alphabets.remove(user_choice)
            print(f"The selected letter is not in the word !!\n")
            turns -= 1
    
    if turns==0:
        print(lives_visual_dict[turns])
        print(f"You died ! The word is :  {word}")
    else:
        print(f"You won! The word is : {word}")

if __name__ == '__main__':
    game()


                


