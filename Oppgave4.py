def my_filter(function, iterable):
    result = []
    for item in iterable:
        if function(item):
            result.append(item)
    return result

def is_under_drinking_age(person):
    return person['age'] < 18

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

under_drinking_age = my_filter(is_under_drinking_age, persons)
for person in under_drinking_age:
    print(f"{person['name']} is under the drinking age.")
