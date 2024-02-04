user_input = int(input("Please enter number: "))
res = 1
for i in range(1, user_input + 1):
    res = res * i
    
print(f"Result: {res} ")