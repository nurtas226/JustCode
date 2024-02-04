# file = open(r'test.txt', 'r')  # read only

# file = open(r'test.txt', 'w', encoding='utf-8')  # w = write. It creates a file
# file.write("Hello world!")


# file = open(r'test.txt', 'r')
# data = file.read()
# print(data)

file = open(r'test.txt', 'r', encoding='utf-8')  # w = write. It creates a file
file.write("Hello world!")

data = file.read()

print(data.text())

file.close()