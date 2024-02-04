def get_square(a):
    return a * a
    
    
def get_sum_of_squares(a, b, func):
    return func(a) + func(b)


# print(get_square(5))
# print(get_square)
print(get_sum_of_squares(2, 4, get_square))

