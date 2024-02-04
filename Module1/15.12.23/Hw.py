rows = 4
columns = 6

for i in range(rows):
    for j in range(columns):
        if (i + j) % 2 == 0:
            print("X", end="")
        else:
            print("O", end="")
    print()