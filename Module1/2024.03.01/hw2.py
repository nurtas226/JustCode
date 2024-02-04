import string

def is_valid(password):
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digits = False
    has_punctuation = False
    
    for char in password:
        if char in string.ascii_uppercase:
            has_uppercase = True
        elif char in string.ascii_lowercase:
            has_lowercase = True
        elif char in string.digits:
            has_digits = True    
        elif char in string.punctuation:
            has_punctuation = True
    
    if len(password) < min_length:
        return "Password is too short!"
    elif not has_uppercase:
        return "Password must contain at least one uppercase letter!"            
    elif not has_lowercase:
        return "Password must contain at least one lowercase letter!"            
    elif not has_digits:
        return "Password must contain at least one digit!"            
    elif not has_punctuation:
        return "Password must contain at least one special character!" 
    else:
        return "You got strong password!"           
            
user_input = input("Create strong password: ")

result = is_valid(user_input)

print(result)
