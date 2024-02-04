# You need to create a collection with the student's name and 
# a list of subjects that he took.You need to find 
# the student with the largest number of subjects.

s = {
    "John": ["Math", "English"],
    "Emily": ["Science", "History", "Geography"],
    "Tom": ["Physics", "Chemistry"]
}

res = {}

for key, value in s.items():
    res[key] = len(value)

m = max(res.values())
    
for key, value in res.items():
    if value == m:
        print(f"The student with the most subjects is {key}.")