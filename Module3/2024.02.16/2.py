data = [

    {'id': 1, 'name': 'Ulan', 'age': 25},

    {'id': 2, 'name': 'Max', 'age': 99},

    {'id': 3, 'name': 'Alex', 'age': 77},

    {'id': 4, 'name': 'John', 'age': 88},

    {'id': 5, 'name': 'Mike', 'age': 33},

]

page_size = int(input("page size = "))
page = int(input("page = "))

def paginate_list(data, page, page_size):

    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return data[start_index:end_index]

result = paginate_list(data, page, page_size)
print(result)