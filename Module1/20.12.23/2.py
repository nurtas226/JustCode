b = "Hello!"
print(f"b: {b}")
    
c = ["elem1", "elem2", 3, 4, 5.5, True]
print(f"c: {c}")

res = c[3]
print(f"res: {res}")

c.append("new elem")
print(f"c: {c}")

c.insert(1, "NEW_elem")
print(f"c: {c}")

c.remove("new elem")
print(f"c: {c}")

print(f"len c: {len(c)}")