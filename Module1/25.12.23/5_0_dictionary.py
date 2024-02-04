d = {
    "age": 12,
    "name": "John",
    "email": "john@example.com",
    "phone": "123-144-513"
}
# print(d["age"])

# for elem in d:
#     print(f"{elem}: {d[elem]}")

for key, values in d.items():
    print(f"{key}: {values}")