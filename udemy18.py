# score = 1
# height = 1.8
# isWin = True
# #f string

# print(f"your score is {score}, your height is {height}  your winning valur is {isWin}")



# age = input("Enter your age :")
# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining *365
# weeks_remaining = years_remaining *52
# months_remaining = years_remaining *12


# message =(f" you have{years_remaining} days,{days_remaining} weeks {weeks_remaining}")
# print(message)



# Tip Calculator
# if the bill was 150.00 split btw 5 peoplw with 12% tip
# Each person should pay 150.00/5 * 1.12

print("Welcome to tip calculator! ")
bill = float(input("What was the total bill"))

tip = int(input("How much tip you like to give"))

people = int(input("how many people splitt bill"))

bill_with_tip = tip /100 * bill + bill
print(bill_with_tip)


