try:
    number = int(input("Number: "))

    h_number = number / 2
    circle = round(h_number)

    check = circle * 2

    if check == number:
        print("The number is even!")

    else:
        print("The number is not even!")

except ValueError:
    print("You can't divide by zero!")
