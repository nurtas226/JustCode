n = int(input('n = '))
a = 0
result = 0
while a < n:
    #a = a + 1
    a += 1
    if a % 2 == 0:
        print(a)
        #result = result + a
        result += a
        
print(f"Result: {result}")
