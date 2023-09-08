# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)


 
 
# lovecalc = random.randint(1, 100)
# print(f"Your love Score is{lovecalc}")

# '''Write a code using random funtion'''
# import random

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")    





'''        List        '''
# states_of_america = ["Delawar","pennsylvania", "hyderabad", "nampally", "tolichowki" ]

# states_of_america[4] = "Tolichowki"

# states_of_america.extend(["meraj colony", "hakimpet"])
# print(states_of_america)



# Code Project

# import random

# #split string method

# names_string = input("Give me every body names here :")

# names = names_string.split(", ")
# print(names)

# numb_item=(len(names))

# random_choice=random.randint(0, numb_item - 1)
# pnames=names[random_choice]
# print(pnames + "is going to bill today")


# dirty_dozen =["strawberry", "spinach", "kale","nectarianes", "Apple", "grapes", "peaches", "cherries", "pears", "Tomatoes", "celery","potatoes"]

# fruits= ["strawberry", "nectarianes", "apple", " grapes", "peaches", "cherries", "pears"]
# vegetables=["spanich", "kale", "Tomatoes", "celery", "potatoes"]

# dirty_dozen= [fruits, vegetables]

# print(dirty_dozen)


# ----------------//////////////-----------------------------ROCK PAPPER SCISORS__----------------------------------------/////////////------------------------------------------

import random

# user_choice = input("What do you choose? Type 0 for Rock 1 for paper and 2 for scissors .\n" )


# computer_choice = random.randint(0, 2)
# print(f"computer choose{computer_choice}")


# user_choice = int(input("What you want to choose ? 0 for Rock 1 paper 2 scissors.\n"))

# computer_choose = random.randint(0, 2)
# print(f"computer choose{computer_choose}")


# if user_choice >3 or user_choice < 0:
#     print("its invalid number  you lose")  
# elif user_choice == 0 and computer_choose == 2:
#     print("you win 1")
# elif user_choice >3 or user_choice < 0:
#     print("its invalid number")        
# elif computer_choose == 0 and user_choice == 2:
#     print("You lose")    
# elif computer_choose > user_choice:
#     print("You lose")  
# elif  user_choice > computer_choose:
#     print("You win")
# elif computer_choose == user_choice:
#     print("Draw")  


# First prigram done by syed rafi //////////////////////////////////////////// yesss ///////////////////////////////////////////////////////////////////
import random

user = int(input("What you want to take ? 0 for Rock , 1 for paper and 2 foer scissor  :\n"))

computer = random.randint(0, 1)

print(f"computer chooses {computer}")


if user >3 and user < 0:
    print("Invalid number")
if user == computer:
            print("Draw")
elif user == 0 and computer == 1:
            print("you win")    
elif user == 1 and computer== 2:
            print("you loose ")    
elif user == 2 and computer == 0:
            print("you loose")    
elif user ==1 and computer == 0:
            print("you win")   
elif user ==2 and computer == 1:
            print("you win") 
else:
    print("invalid")