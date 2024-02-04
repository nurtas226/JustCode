d = [
{
    "age": 12,
    "name": "John",
    "email": "john@example.com",
    "phone": "123-144-513"
},
{
    "age": 23,
    "name": "James",
    "email": "James@example.com",
    "phone": "125-164-513"
},
{
    "age": 19,
    "name": "Mateusz",
    "email": "Mateusz@example.com",
    "phone": "151-414-513"
}
]

for elem in d:
    if elem['age'] > 18:
        for key, value in elem.items():
            print(f"{key}: {value}")
    print()
