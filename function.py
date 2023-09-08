# def greet( ):
#     print("Hello rafi")
#     print("How do you do")
#     print("isnt teh weather nice today")
    
# greet()

# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how are you {name}")
    
# greet_with_name("chalbey")    


# Functions with multiple inputs
# def greet_with(name, location, ):
#     print(f"hello {name}")
#     print(f"my locations is {location}")
   
    
# # greet_with("rafi", "tolichowki", "chalbey")    


# greet_with(name = "Angela", location = "tolichowki")



# Creat a funtion that calc the paint bottel-------------------------------------------------------
# import math
# def paint_calc (height, weight, cover):
#     area = height*weight
#     num_of_cans = math.ceil(area/ cover)
#     print(f"Youll need number{num_of_cans} of cann")
    
    
# test_h =int(input("Height of wall: "))    
# test_w = int(input("Width of wall: "))
# coverage = 5

# paint_calc(height = test_h, weight=test_w, cover = coverage)


# check the prime number? -------------



# def prime_checker(number):
#     is_prime= True
#     for i in range(2, number):
#       if  number % i == 0:
#           is_prime= False
#     if is_prime:
#         print("It is prime number")    
#     else:
#         print("It is not a prime")      
          
    

# n = int(input("check this number"))
# prime_checker(number=n)



# CEACER CYPHER ---------------///////////////////////////----------------------------//////////////////////////---------------------//////////---------------------------------

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def ceaser (start_text, shift_amount, cipher_direction):
    end_text =""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
        elif cipher_direction == "decode":
            new_position = position - shift_amount
        end_text += alphabet[new_position]    
    print(f"here the {direction} result {end_text}")    
# ceaser(start_text= text, shift_amount=shift , cipher_direction= direction)    



should_continue =True
while should_continue :

    direction = input("type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("type your mesage\n")
    shift = int(input("type shift number:\n"))
    shift = shift % 26
    ceaser(start_text= text, shift_amount=shift , cipher_direction= direction)
    result=input("type 'yes' to again and no.\n")
    if result == "no":
        should_continue = False
        print("goodbye")
    
# def encrypt (plane_text, shift_amout): 
#     cipher_text = ""
#     for letter in plane_text:
#         position=alphabet.index(letter)
#         new_position=position + shift_amout
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"Encode text is {cipher_text}")    
    

# def decrypt (cipher_text, shift_amout):
#     plane_text =""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position= position - shift_amout
#         plane_text += alphabet[new_position]
#     print(f"The decode is {plane_text}")    
    
    
# if direction == "encode":
#     encrypt(plane_text = text, shift_amout= shift)    
# elif direction == "decode":
#      decrypt(cipher_text= text , shift_amout= shift)    
    
#  THE WAY UDEMY TAUGHT-----------------------090098087968587658237649257238927-58627-//////////    
    
# def ceaser(start_text , shift_amount, cipher_direction):
#     end_text=""
#     if cipher_direction =="decode":
#         shift_amount *= -1
#     for letter in start_text:
#         position = alphabet.index(letter)    
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"here the {direction} result {end_text}")    
    
# ceaser(start_text= text, shift_amount=shift , cipher_direction= direction)    

# tHE WAy i dONE wITH iF AnD eLIF .............../////';[[[[[[[]]]]]]]'--------------------3456789======0=-0-0-0=0-0-0=0=0=0=0=0-0-: BOOOOOOOOOOM

# def ceaser (start_text, shift_amount, cipher_direction):
#     end_text =""
#     for letter in start_text:
#         position = alphabet.index(letter)
#         if cipher_direction == "encode":
#             new_position = position + shift_amount
#         elif cipher_direction == "decode":
#             new_position = position - shift_amount
#         end_text += alphabet[new_position]    
#     print(f"here the {direction} result {end_text}")    
# ceaser(start_text= text, shift_amount=shift , cipher_direction= direction)    

# what if user enter symbos spaces and number how to fix ?
# what if user enter a shift more that 45 more than alphabet??????