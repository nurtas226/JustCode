file = open(r'test.txt', 'r', encoding='utf-8')

data = file.read()
print(data)

file.close()

# ==================================================

with open(r'test.txt', 'r', encoding='utf-8'):  # context manager(cm) - with
    data = file.read()

print(data)

