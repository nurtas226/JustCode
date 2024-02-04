x = 7
User_guess = 0

while User_guess < x:
    User_guess = int(input("Please guess the number from 1 to 10: "))
    if User_guess == x:
        print("Congratulations! You guessed correctly!")
        break
    else:
         print("Your guess is too low. Please try again.")
         User_guess += 1
         
     
while User_guess > x:
    User_guess = int(input("Please guess the number from 1 to 10: "))
    if User_guess == x:
        print("Congratulations! You guessed correctly!")
        break
    else:
         print("Your guess is too high. Please try again.")
         User_guess += 1