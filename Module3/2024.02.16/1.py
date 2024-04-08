def paginate_list(data, page_size, page):

    start_ind = (page - 1) * page_size   # ps=2: p=1 -> 0, p=2 -> 2, p=3 -> 4

    end_ind = start_ind + page_size

 

    return data[start_ind: end_ind]

 

 

data = [

    {'id': 1, 'name': 'Ulan', 'age': 25},

    {'id': 2, 'name': 'Max', 'age': 99},

    {'id': 3, 'name': 'Alex', 'age': 77},

    {'id': 4, 'name': 'John', 'age': 88},

    {'id': 5, 'name': 'Mike', 'age': 33},

]

 

 

 

# page_size = int(input("page_size: "))

# page = int(input("page: "))

#

#

# print(paginate_list(data, page_size, page))

 

 

PAGE_SIZE = 1

 

for page in range(1, 6):

 

    print("Start of page")

 

    print(paginate_list(data, PAGE_SIZE, page))

 

    print("End of page\n")