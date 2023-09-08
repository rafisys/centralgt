# students_scores = {
#     "harry": 99,
#     "ron" : 99,
#     "hermione":99,
#     "draco": 70,
#     "Neville":62
# }


# # students score are in student and transfer in student_grades
# student_grades = {}

# for student in students_scores:
#     score = students_scores[student]
#     if score > 90:
#         student_grades[student]= "Outstanding"
#     elif score > 80:
#         student_grades[student]="Exceeds Expectation"
#     elif score > 70:
#         student_grades[student]="Acceptable"
#     else:
#         student_grades[student]= "fail"              
            
# print(student_grades)  



# traavel_logs ={
#     "France":{"cities_visited":["paris", "lille", "Dijon"], "Total_visite":12},
#     "gerany":["Berlin","Hamburg","Tolichwoki"]
# }


# Rafi_Travel = {
#     "mehdipatnam" :{"placesINmehdi": ["muradnagar","chotimasjid","mehrajfuntionhall"],"Total": 10}
# }

# Travel_logs = [
# {
#     "country":"France",
#     "Visited": "12",
#     "cities":["paris","lille","dijon"]
# },
# {
#     "country":"Germany",
#     "Visited": 5,
#     "cities":["Berlin","hamburg","stuttgart"]
# }
# ]

# def add_new_country (country_visited, times_visited, cities_visited):
#     new_country ={}
#     new_country["country"]= country_visited
#     new_country["visited"]= times_visited
#     new_country["cities"]= cities_visited
#     Travel_logs.append(new_country)
    
# add_new_country("Russia",2,["moscow","saint petersburg",])    
# print(Travel_logs)
    
    # Projecttt-----------------------////////////////////-----------------
# import clear

# bids= {}
# bidding_finish = False

# def find_highest_bidder(bidding_record):
#     highest_bid =0
#     winner =""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner= bidder
#     print(f"winner is{winner} with bid {highest_bid}")        

# while not bidding_finish:
#     name = input("Enter the name?:")
#     price = int(input("Enter bid price $?: "))
#     bids[name]= price
#     Should_continue=input("Are any others bidders? yes or no \n")

#     if Should_continue == "no":
#         bidding_finish = True
#         find_highest_bidder(bids)



        