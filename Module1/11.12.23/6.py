passwd = 'qwerty'
n = 0

while n < 3:
    user_input = input('Please enter password: ')
    if user_input == passwd:
        print("Access granted!")
        break
    else:
        print(f"Wrong password, try again. (Attempt number {n+1}/3)")
        n += 1
        
       
'''
if user_input != passwd:
    print("Wrong password!")
else:
    while user_input == passwd:
        print("Password is correct!")
        break
'''

               

    
