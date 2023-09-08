# fruits = ["Apple", "Peach", "Peer"]
# for frut in fruits:
#     print(frut)
#     print(frut + "pie")
# print(fruits)
    
    
#    ------------------ #get the number of height in list--------


# student_height = input("Input the list of students height ").split()
# for n in range(0, len(student_height)):
#     student_height[n]= int(student_height[n])
# print(student_height)

#  # total the number of height ----with loops
# total_height= 0
# for height in student_height:
#     total_height += height
# print(total_height)

# # check how many students are there with loops-----
# number_of_student =0
# for students in student_height:
#     number_of_student += 1
# print(number_of_student)    


# #take out the averahge value of total

# average_of_height = round(total_height / number_of_student)
# print(average_of_height)


# student_height= input("Enter the height of students ").split()
# for n in range(0, len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)    


# number_of_student =0
# for h in student_height:
#     number_of_student+= 1
# print(number_of_student)


# # pracice
# height_of_students = input("Enter the height" ).split()
# for n in  range(0, len(height_of_students)):
#     height_of_students[n]= int(height_of_students[n])
# print(height_of_students)


# Challenge------------------------------------------------------- do it

# range   

#for number in range(1, 10, 3):
    # print(number)
    
# total = 0
# for number in range(1, 101):
#     total = total + number
# print(total)



# total = 0
# for number in range(1, 101, 2):
#     total += number
# print(total)    
    
    
    
# the most asked question
    # fizz and buzz
   
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:   #if we dont uses and here then it wont work
#         print("Fizzbuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 ==0 :
#         print("buzz")    
#     else:
#         print(number)    
        
        
#password generator:


# LETS TRY IT
import random

print("Welcome to the password generator")

letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o' 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K', 'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9',]

symbols=['!','@','#','$','%','&','(',')','*','+']

nr_letters = int(input("enter the length of a password?\n"))

nr_numbers = int(input("How many numbers youwant? \n"))

nr_symbols = int(input("Enter how many sysmbols you want?\n"))


password_list= []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
    
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers) 
    
for char in range(1, nr_symbols + 1):
    password_list+= random.choice(symbols)     
    
print(password_list)         
random.shuffle(password_list)
print(password_list) 

password = ""
for char in password_list:
    password += char
    
print(f"your password is {password}")    
    
    