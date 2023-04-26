def my_reduce(func, lst, initial=None):
    if initial is None:
        result = lst[0]
        lst = lst[1:]
    else:
        result = initial
    for item in lst:
        result = func(result, item)
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

count_above_50 = my_reduce(lambda count, person: count + 1 if person['age'] > 50 else count, persons, 0)

print(count_above_50)
