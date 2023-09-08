# def format_name(f_name, l_name):
#     if f_name =="" or l_name == "":
#       return "You didnot enter any thing"
#     formated_f_name=f_name.title()
#     formated_l_name=l_name.title()
    
#     return f"{formated_f_name} {formated_l_name}"
    

# print(format_name(input("Enter your name?"),input("Enter last ?")))

# LEap year -------------------------------0000000000-9-0=-0------------------===================------------------------------------------------
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False      
      
                
def days_in_month(year, month):
    month_day =[31, 28, 31, 30, 31, 30, 31, 31,]
    if is_leap(year)and month ==2:
        return 29
    return month_day[month - 1]    

year = int(input("Enter the year : "))
month = int(input("Enter the month"))
days = days_in_month(year, month)
print(days)