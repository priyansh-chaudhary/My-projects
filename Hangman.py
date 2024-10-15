import random as rd


print('''
                         _                                             
                        | |                                            
                        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                        | | | | (_| | | | | (_| | | | | | | (_| | | | |
                        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                           __/ /                      
                                          |___/                       
    ''')

words = ["elephant", "building", "notebook", "computer", "umbrella",
    "backpack", "sandwich", "airplane", "football", "hospital",
    "pencil", "car", "garden", "dog", "glass","apple", "banana", "grape", "elephant", "guitar",
    "bicycle", "mountain", "river", "pencil", "umbrella",
    "flower", "butterfly", "window", "football", "teacher",
    "house", "garden", "school", "ocean", "coffee"]

guessed_words = []

choosen_word = rd.choice(words)
display = ["_" for _ in choosen_word]
max_attempts = 6
wrong_guesses = 0

print(f"\n\nWord have {len(choosen_word)} letters.")
while wrong_guesses < max_attempts and "_" in display:
    print(" ".join(display),"\n\n")
    guess = input("Guess a letter : ").lower()

    if guess in choosen_word :
        guessed_words.append(choosen_word)
        for index, letter in enumerate(choosen_word) :
            if letter == guess :
                display[index] = guess
        
    else :
        wrong_guesses += 1
        if wrong_guesses < 6 :
            print(f"Wrong Guess! You have {max_attempts - wrong_guesses} attempts left!!")

if "_" not in display:
    print(" ".join(choosen_word),"\n")
    print(f"Congratulations! You won!\nYou guessed it only in {wrong_guesses} attempts.")
    words.remove(choosen_word)
    
else:
    print(f"\nYou lost! The word was: {choosen_word}")

if (not words) :
    print(f"Yeeey you won the whole game!")
    print("  ".join("CONGRATULATIONS"))

print(guessed_words)