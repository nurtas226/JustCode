n = 5

for i in range(n):
    print((n - (i+1)) * " ", end="")
    for j in range(i + 1):
        print("*", end=" ")
    print()