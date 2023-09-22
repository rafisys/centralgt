MENU = {
    "espresso":{
       "ingredients": {
        "water": 50,
        "coffee": 18,
        },
    "cost": 1.5,
     },
    "lette": {
     "ingredients": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
      },
    "cost": 2.5,
    },
    "cuppuccino":{
     "ingredients":{
        "water":250,
        "milk":100,
        "coffee":24,
       },
    "cost":3.0
    }   
}
profit = 0
resources = {
    "water": 300,
    "milk":200,
    "coffee":100,
#//this is is this

def is_resource_sufficient(order_ingredient):
    is_enough = True
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
          print(f"Sorry there is not enough {item}.")
          is_enough= False
    return False  

def process_coins():
    print("please insert coins.")  
    total = int(input("how many quaters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01 
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round( money_received - drink_cost, 2)
        print(f"Thi is change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry nikla ya se")
        return False

is_on = True

while is_on:
    choice = input("what would you like to have (espresso/lette/cuppuccino: )")
    if choice == "off":
         is_on = False
    elif choice == "report":
         print(f" Water : {resources ['water']} ml")
         print(f" Milk : {resources ['milk']}ml")
         print(f" coffee: {resources ['coffee']}g")
         print(f" Money : {profit }")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
             payment = process_coins()
             is_transaction_successful(payment, drink["cost"]) 
            
            
          
          
