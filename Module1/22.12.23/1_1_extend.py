a = ["Hello", 23, "World", 45]
b = [42, 45, 52, 5]
print(f"Old a: {a}")

a.extend(b)

print(f"New a: {a}")