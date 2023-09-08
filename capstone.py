# project guessing an number
from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
# make a funtion to check answer
def check_answer(guess, answer):
    if guess > answer:
        print("To High")
    elif guess < answer:
        print("Too low")
    else:  
        print(f"You got it ; The answer is {answer} ")      


# set a difficulty level
def set_difficulty():
    level = input("Choose a difficulty type 'easy' or 'hard':")
    if level == "easy":
        global turns
        return  EASY_LEVEL_TURN
    else:
        return   HARD_LEVEL_TURN    
    
def game():
    print("Welcome to the Number Guessing Game !")
    print("I am thinkung of number between 1 to 100")
    answer = randint(1, 100)
    print(f"passt the correct answer {answer} ")

    turns = set_difficulty
    print(f"You have {turns} : attempts remains")
    guess = 0
    while guess != answer :
        
      guess = int(input("Make a guess:"))

    check_answer(guess, answer)

game()