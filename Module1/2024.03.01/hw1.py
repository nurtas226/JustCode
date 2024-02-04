from math import sqrt

def solver(a, b, c):
    dis = pow(b,2) - 4*a*c
    if dis > 0:
        x1 = (-b + sqrt(dis))/(2*a)
        x2 = (-b - sqrt(dis))/(2*a)
        return x1, x2
    elif dis == 0:
        x1 = -b / (2*a)
        return x1
    else:
        return None
    
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

result = solver(a,b,c)
if result is None:
    print("The equation has no real roots")
elif isinstance(result, tuple):
    print(f"The roots of the equation: x1 = {result[0]} x2 = {result[1]}")
else:
    print(f"The root of equation: x = {result}")