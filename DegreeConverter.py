def Converter():
    UnitUser = input("Enter the unit you want to convert from:(F/C) ")
    NumberUser = input("Enter the number you want to convert: ")

    if UnitUser == "C":
        print("You have selected Celsius")
        NumberUser = int(NumberUser)
        ConvertedNumber = NumberUser * 9/5 + 32
        print(str(ConvertedNumber) + " °C")

    elif UnitUser == "F":
        print("You have selected Fahrenheit")
        ConvertedNumber = (int(NumberUser) - 32) * 5/9
        print(str(ConvertedNumber) + " °F")

    else:
        print("Invalid unit")
        print("Please enter C or F")

Converter()