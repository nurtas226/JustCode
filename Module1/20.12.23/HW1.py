a = []
x = int(input("Enter sum: "))

for i in range(x):
    a.append(i + 1)
    
res = 0
for i in range(len(a)):
    if i % 2 == 1: 
        res += a[i]
print(f"Reslut: {res}")
print(f"List: {a}")
        