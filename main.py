import random

word_library = ["stellar", "exquisite"]

def main():

        HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

        print("""Welcome to Hangman!
You know the rules!
Would you like to play? (y/n)""")

        play_again = input()

        while(play_again.lower() == "y"):
                hangman_stage = 0
                word_list = []
                blank_list = []
                word = random.choice(word_library)
                true_correct = 0

                for i in range (0, len(word), 1):
                        word_list.append(word[i])
                        blank_list.append("_")

                round_loop = 1

                while(round_loop == 1):

                        correct_choice = 0

                        print(HANGMAN[hangman_stage])
                        print(blank_list)
                        print(f"You have {11 - hangman_stage} guesse(s) left!")

                        
                        Guess = str(input("Guess a letter:\n"))
                        
                        if(Guess.isalpha() != True or len(Guess) != 1):
                                print("This input is invalid!")
                                continue

                        
                        for i in range(0, len(word_list), 1):
                                if(Guess.lower() == blank_list[i]):
                                        print("You already guessed this letter!")
                                        correct_choice += 1
                                        continue
                                elif(Guess.lower() == word_list[i]):
                                        blank_list[i] = word_list[i]
                                        correct_choice += 1
                                        true_correct += 1
                        
                        if(correct_choice == 0):
                                hangman_stage += 1
                        elif(true_correct == len(word_list)):
                                print("You won! Press enter to continue")
                                print("______________________________")
                                input()
                                round_loop = 0
        
                        if(hangman_stage > 10):
                                print("You lost! Press enter to continue")
                                print("______________________________")
                                input()
                                round_loop = 0

                print("""Welcome to Hangman!
You know the rules!
Would you like to play? (y/n)""")

                play_again = input()




        #if __name__ == "__main__":
main()
