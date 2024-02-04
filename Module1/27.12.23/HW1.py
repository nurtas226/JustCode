a = 'термика'
b = 'керамит'

def anogramma(l1,l2):
    l1 = list(l1)
    l2 = list(l2)
    l1.sort()
    print(l1)
    l2.sort()
    print(l2)
    if l1==l2:
        print("It is annogramma")
    else:
        print(False)
      
    
anogramma(a,b)  

a = [1,2,200,4,100]
for i in a:
    b = 0
    b += i
    if i <= b:
        max = i
    print(f'Max is:{max}')
def num_max(numbers): 
    largest = numbers[0] 
    for i in range(1, len(numbers)): 
        if numbers[i] > largest: 
            largest = numbers[i] 
    return largest 
 
my_list = [1, 5, 2, 7, 3] 
largest = num_max(my_list) 
print(largest)  
