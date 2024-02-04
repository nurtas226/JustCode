a = []
ent = int(input("enter: "))
for i in range(ent):
    a.append(i+1)
sum = 0
for i in range(len(a)):
    sum += a[i]
print(f"sum: {sum}")
average = sum / len(a)
print(f"average: {average}")
