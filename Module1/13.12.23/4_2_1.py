input = input("Введите текст: ")

result = ""

for i in input:
    if i != " ":
        result = result + i
    else:
        continue

print(result)