user_i = input("Enter polindrom word: " )

if user_i == user_i[::-1]:
    print(f"The entered word is a palindrome. {user_i} ")
else:
    print(f"The entred word is NOT a palindrome.")