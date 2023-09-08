# Create a calculator
# ADD function
def add(n1, n2):
    return (n1+n2)

# SUB funtions
def substract(n1, n2):
    return(n1-n2)

#Multiply functions
def multiply(n1, n2):
    return(n1*n2)

# Divide funtions
def divide(n1, n2):
    return(n1/n2)


operations={
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1=int(input("Enter the number ? "))

    for symbols in operations:
        print(symbols)

    should_continue = True
    while should_continue :
        
        operation_symbol = input("pinck up the symbol:")    
        num2=int(input("Enter the next number ? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"type 'y' continue {answer}: or 'n: " ) == "y":
            num1 = answer
        else  :
            should_continue = False  
            calculator()
            
calculator()            