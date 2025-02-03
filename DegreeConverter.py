def hello():
    Unituser = input("Enter the unit you want to convert from:(F/C) ")
    if Unituser == "C":
        print("You have selected Celsius")
    elif Unituser == "F":
        print("You have selected Fahrenheit")
    else:
        print("Invalid unit")
        hello()

hello()