import random
import os

class Game_User :

    def __init__(self, name) :
        self.name = name
        self.score_file = f"{self.name}_score.txt"
        self.attempts = 1
        print("\n","Guess The Number Game".center(80, "-"),end="\n\n")
        self.welcome()

    def welcome(self) :
        print(f"Welcome {self.name.title().strip()}")
        print("Guess a number between 1 and 100.")
        print("Type 'exit' anytime to quit the game.\n")

    def guess_the_number_game(self) :

        computer_choice = random.choice(range(1,101))
        
        #GUESS NUMBER
        while True :

            user_input = input("\nGuess the number : \n  ")
            
            if (user_input.lower() == "exit") :
                print("You have exit the game!")
                return
            
            try :
                user_choice = int(user_input)
            except ValueError :
                print("Invalid Input! Please enter number (1-100) or 'exit' to quit.")
                continue

            if (user_choice == computer_choice) :
                break
            elif (user_choice < computer_choice) :
                self.attempts += 1
                print("Too Low!")
            else :
                self.attempts += 1
                print("Too High!")


        print(f"\nCorrect it take you {self.attempts} attempts!\n")

        #MAKING FILE
        if (os.path.exists(self.score_file)) :
            with open(self.score_file, "r+") as f :
                score = int(f.read().strip())
                if (score > self.attempts) :
                    print("NEW HIGH SCORE")
                    f.seek(0)
                    f.write(str(self.attempts))
                    f.truncate()
        else :
            with open(self.score_file, "w") as f :
                f.write(str(self.attempts))

#OBJECTS
me = Game_User("Priyansh")
me.guess_the_number_game()