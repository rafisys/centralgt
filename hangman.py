# step1
word_list=["ardvark", "baboon", "camel"]

# Randomly choose a word from a word list



import random
choosen_word = random.choice(word_list)
print(f"choosen word {choosen_word}")


display=[]
word = len(choosen_word)
for _ in range(word):
    display += "_"
print(display)    

end_of_game = False

while not end_of_game:
    guess = input("Enter a letter : ").lower()


    for position in range(word):
        letter = choosen_word[position] 
        print(f"")
        if letter == guess:
            display[position]=letter
            
    print(display)  
          
    if "_" not in display:
        end_of_game = True
        print("you win.")


# tobe continue-----------------------