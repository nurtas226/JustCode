# numbers = [45, 3, 52, 5, 6]

# # print(max(numbers))

# current_max = numbers[0]
# for num in numbers:
#     print(f"current_max: {current_max} current number: {num}")
#     if num > current_max:
#         current_max = num
#         print('changed\n')
#     else:
#         print("not changed\n")
#         continue
    
def custom_max(numbers):
    current_max = numbers[0]
    for num in numbers:
        # print(f"current_max: {current_max} current number: {num}")
        if num > current_max:
            current_max = num
            # print('changed\n')
        else:
            # print("not changed\n")
            continue
    return current_max

numbers = [1,24,56,32,6,26,73]

res = custom_max(numbers)

print(f"Result: {res}")