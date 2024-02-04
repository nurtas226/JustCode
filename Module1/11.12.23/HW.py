user_input = int(input("Please, enter positive integer to start bomb timer: "))

if user_input <= 0:
    print("You have entered a negative number or 0. Please try again.")
else:
    while user_input > 0:
        if user_input == 0:
            break
        print(user_input)
        user_input = user_input - 1
    print("Boom!")

