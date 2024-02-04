# Find the vowels from the sentence "hello world from justcode" 
# and save to the set

s = "hello world from justcode"

a = ['a', 'e', 'u', 'o'] 

# result = []
# for char in a:
#     if char in a and char not in result: 
#         result.append(char)

result = set()
for char in s:
    if char in a:
        result.add(char)
        
        
print(result)