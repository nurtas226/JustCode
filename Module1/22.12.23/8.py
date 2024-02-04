s = "Hello World"
print(f"s: {s}")

#res = s.find('ld')
#res = s.index("ld")
#res = s.replace('l', '*')
#res = s.split()

splitted = s.split(' ')
print(f"Splitted: {splitted}")

joined = '_'.join(splitted)
print(f"Joined: {joined}")