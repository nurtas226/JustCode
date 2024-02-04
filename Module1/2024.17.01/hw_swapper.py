
with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read()

modified_words = ['***' if 'z' in word else word for word in text.split()]

modified_text = ' '.join(modified_words)

with open("output1.txt", "w", encoding="utf-8") as file:
    file.write(modified_text)