# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# direction = input("type 'encode' to encrypt, type 'decode' to decrypt\n")

# text = input("type your mesage\n")

# shift = int(input("type shift number:\n"))
    
# def encrypt (plane_text, shift_amount):
#     cipher_text= ""
#     for letter in plane_text:
#         position = alphabet.index(letter)
#         new_position= position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"Encode is {cipher_text}")    
    
# def decrypt (cipher_text , shift_amount):
#     plane_text =""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plane_text += new_letter
        
#     print(f"Decode is {plane_text}")    
    
    
# if direction == "encode":
#     encrypt(plane_text=text, shift_amount=shift)    
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)    

# def encrypt (plane_text, shift_amount):
#     cipher_code = ""
#     for letter in plane_text:
#         position= alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_code += new_letter
#     print(f"Encode is {cipher_code}")    
# encrypt(plane_text= text , shift_amount= shift)    

# def decode (cipher_text , shift_amount):
#     plane_text =""
#     for letter in cipher_text:
#         position= alphabet.index(letter)
#         new_position = position - shift_amount
#         plane_text += alphabet[new_position]
#     print(f"decode {plane_text}")    
    
# decode (cipher_text= text, shift_amount= shift)        


# bids ={}

# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner =""
#     for bidder in bidding_record:
#         bids_amount = bidding_record[bidder]
#         if bids_amount > highest_bid:
#             highest_bid = bids_amount
#             winner = bidder
#     print(f"winner is {winner} and bid is {highest_bid}")

# bidding_finish = False
# while not bidding_finish:
#     name = input("Enter the name : ")
#     price = int(input("Enter the bid amount: ?" ))
#     bids[name]= price
#     should_end = input("If other are there enter yes or no")
#     if should_end == "no":
#         bidding_finish = True
#         find_highest_bidder(bids)




# # Create a calculator
# # ADD function
# def add(n1, n2):
#     return (n1+n2)

# # SUB funtions
# def substract(n1, n2):
#     return(n1-n2)

# #Multiply functions
# def multiply(n1, n2):
#     return(n1*n2)

# # Divide funtions
# def divide(n1, n2):
#     return(n1/n2)


# operations={
#     "+": add,
#     "-": substract,
#     "*": multiply,
#     "/": divide
# }


# num1 = int(input("Enter the number :"))
# num2 = int(input("Enter the number :"))

# operation_symbols = input("Enter the symbol: ")
# for symbols in operation_symbols:
#     print(symbols)
    
 
# calculation = operations[operation_symbols]   
# result = calculation(num1, num2)
# print(f"{num1} {operation_symbols} {num2} = {result} ")

        
        
# Practice of capstone fuile
# from random import randint
# EASY = 10
# HARD = 5
# turns = 0

# # make a function to check the answer
# def check_answer (guess, answer, turns):
#     if guess > answer:
#         print("Too high")
#         return turns - 1
#     elif guess < answer:
#         print("Too low")  
#         return turns - 1  
#     else:
#         print(f"You got it: Answer is {answer}")    
        
        
# def set_difficulty():
#     level = input("Select level : 'easy' to 'hard': ")
#     if level == "easy":
#         return EASY
#     elif level ==  "hard":
#         return HARD       
    
# def game():
#     print("welcome to the guessing game")     
#     print("I am thinking of a number between 1 to 100")
#     answer = randint(1, 100)
#     print(f"ANSWER IS {answer}")

#     turns = set_difficulty()
    
#     guess = 0
#     while guess != answer:
#         print(f"you have {turns} ateempts to guess the number.")
#         guess = (int(input("MAke a guess: ")))
#         turns= check_answer(guess, answer, turns)
#         if turns == 0 :
#             print("OVER")
#             return False
         
        

# game()

# ------------------COFFEE---------------------------

# MENU = {
#     "espresso":{
#        "ingredients": {
#         "water": 50,
#         "coffee": 18,
#         },
#     "cost": 1.5,
#      },
#     "lette": {
#      "ingredients": {
#         "water": 200,
#         "milk": 150,
#         "coffee": 24,
#       },
#     "cost": 2.5,
#     },
#     "cuppuccino":{
#      "ingredients":{
#         "water":250,
#         "milk":100,
#         "coffee":24,
#        },
#     "cost":3.0
#     }   
# }
# profit = 0
# drink = 0
# resource = {
#     "water": 300,
#     "milk": 200,
#     "coffee":100,
    
# }
# def is_resource_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if order_ingredients[item] >= resource[item]:
#            print("Sorry")
#            return False
#     return True

# def coins():
#     print("Enter coins")
#     tatal = int(input("how many quarters")) * 0.25
#     tatal += int(input("how many dimes")) * 0.1
#     tatal += int(input("how many nickles")) * 0.05
#     tatal += int(input("how many pennies")) * 0.01
#     return tatal

# def is_transaction_successful(money_received, drink_cost):
#     if money_received >= drink_cost:   
#         change = round(money_received - drink_cost, 2)
#         print(f"here is the change {change}")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry paise aur lao")
#         return False
    
# def make_coffee (drink_name, order_ingredients):
#     for item in order_ingredients:
#         resource[item]-= order_ingredients[item]
#     print(f"here is coffee {drink_name}")    
        
    
# is_on = True

# while  is_on :
#     choice = input("Enter you choice(lette/cuppuccino/ espresso)")
#     if choice == "bye":
#         is_on = False
#     else:
#         drink = MENU[choice]    
#         if is_resource_sufficient(drink["ingredients"]):
#            payments= coins()
#            if is_transaction_successful(payments, drink["cost"]):
#                make_coffee(choice, drink["ingredients"])
           


# MYSIRG------------------------\\
    
import turtle 
import random
import time    

delay = 0.1
score = 0
highestscore =0
bodies = []
direction = []
distance =[]

# snakebody
snake =0

# getiing a screen | caanvas
s= turtle.Screen()
s.title("SnakeGAME")
s.bgcolor("grey")
s.setup(width=600 , height=600)


# create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.fillcolor("white")
head.penup()
head.goto(0,0)
head.position="stop"



# snakefoood
food =turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# scoreboard
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("white")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("Score : 0  | highest Score :0 ")


def moveup():
    if head.position!="down":
       head.position = "up"

def movedown():
    if head.position!="up":
        head.position = "down"
        
def moveleft():
    if head.position!="right":
        head.position = "left"
        
def moveright():
    if head.position!="left":
        head.position = "right"                

def movestop():
    head.position="stop"
    
def move() :   
    if head.position == "up":
        y=head.ycor()
        head.sety(y+20)
    if head.position == "down":
        y=head.ycor()
        head.sety(y-20)    
    if head.position == "left":
        x=head.xcor()
        head.sety(x+20)
    if head.position == "right":
        x=head.xcor()
        head.sety(x+20)     
        
# evenhandling - key mapping
s.listen()
s.onkey(moveup,"up")           
s.onkey(movedown,"down")           
s.onkey(moveright,"right")           
s.onkey(moveleft,"left")           
s.onkey(movestop,"space")           

# main Look
# s.mainloop
son = True
while son:
    s.update() #this is to update the screen 
    # to check collision with border
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)            
        
    # to check collision with food
    if head.distance(food) <20:
            # move food to new random
        x= random.randint(-290, 290)
        y= random.randint(-290, 290)
        food.goto(x,y)
    # check collision with snake body
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("orange")
        body.fillcolor("black")
        bodies.append(body) #appwnd new body
            
            #increase the score
        score += 10
            
            #change in delay
        delay-=0.001
            
            #updarte the highest score
        if score> highestscore :
            highestscore=score
            sb.clear()
            sb.write("score: {} hightest: {}")    
            
    # move the snake
        for index in range(len(bodies) -1,0,-1):
            x = bodies[index -1].xcor()
            y = bodies[index -1]
            bodies[0].goto(x,y)
        move()
    
    # check collision with snake body
        for body in bodies:
            if body.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.position="stop"
            
            # hidebodies
            for body in bodies:
                body.ht()
                bodies.clear()    
            
                score = 0
                delay = 0.1
            
            # update score board
            sb.clear()   
            sb.write("score: {}  highestscore: {}")
            time.sleep(delay)
            son= False

             
s.exitonclick()                














