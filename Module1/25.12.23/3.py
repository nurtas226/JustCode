#Create three sets: prime numbers up to 10, 
#even numbers up to 10 and odd numbers up to 10:

a = {1, 3, 5, 9}
b = {2, 4, 5, 9}
c = {3, 9}

print(f"a: {a}")
print(f"b: {b}\n")

res_u = a.union(b)
print(f"union: {res_u}")

res_i = a.intersection(b)
print(f"intersection: {res_i}")

res_dif1 = a.difference(b)
print(f"difference a-b: {res_dif1}")

res_dif2 = b.difference(a)
print(f"difference b-a: {res_dif2}")
print(f"difference b-a v2: {b - a}")

res_sym_dif = a.symmetric_difference(b)
print(f"symmetric difference: {res_sym_dif}")

res_issubset1 = a.issubset(c) 
print(f"a issubset c: {res_issubset1}")
res_issubset2 = c.issubset(a) 
print(f"c issubset a: {res_issubset2}")

res_issuperset = a.issuperset(c)
print(f"a issuperset c: {res_issuperset}")

a.clear()
print(f"new a: {a}")