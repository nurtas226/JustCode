s = 'hello'

# res = {
#     'h': 0,
#     'e': 0,
#     'l': 0,
#     'o': 0,
# }

# for char in s:
#     res[char] = res[char] + 1
    
# print(f"{res}")

res = {
}

for char in s:
    if char not in res.keys():
        res[char] = 1
    else:
        res[char] += 1
    
print(f"{res}")