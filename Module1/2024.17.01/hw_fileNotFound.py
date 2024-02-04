try:
    with open("nonexistent_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File read.")
    print(content)
finally:
    print("Completed.")