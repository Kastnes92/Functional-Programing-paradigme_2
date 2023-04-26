def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

persons = [
    {"name":"Paula Key", "age":23},
    {"name":"Riya Dickerson" , "age":99},
    {"name":"Layne Colon" , "age":53},
    {"name":"Pranav Giles" , "age":51},
    {"name":"Kamryn Davis" , "age":27},
    {"name":"Taniyah Yu" , "age":17},
    {"name":"Brendon Porter" , "age":23},
    {"name":"Jordin Hancock" , "age":86},
    {"name":"Shawn Vargas" , "age":88},
    {"name":"Sawyer Copeland" , "age":14},
    {"name":"Gustavo Baldwin" , "age":7},
    {"name":"Renee Wilson" , "age":29}
]

new_persons = my_map(lambda x: {"name": x["name"], "age": x["age"]+1}, persons)
print(new_persons)
