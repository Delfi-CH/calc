run = True
print("Welcome to Python Calculator")
print("")
print("Please enter your Numbers below")
print("")
print("Syntax for Operator:")
print("Addition = +")
print("Subtraction = -")
print("Multiplication = *")
print("Division = /")
print("")
print("Copyright 2025 Delfi-CH")

while run:
    i1 = float(input("Number 1 = "))
    i2 = float(input("Number 2 = "))
    how = input("Operator = ")

    if how == "+":
        print(i1+i2)
    elif how == "-":
        print(i1-i2)
    elif how == "*":
        print(i1*i2)
    elif how == "/":
        print(i1/i2)
    else:
        print("Not an Operator")

    runagain = input("New Calcualtion? (Y/N) = ")
    runagain = runagain.upper()
    if runagain == "N":
        exit()
    else:
        i1 = 0
        i2 = 0
        how = ""
