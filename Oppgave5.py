def sum_persons_age(persons):
    age_sum = 0
    for person in persons:
        age_sum += person["age"]
    return age_sum

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

total_age = sum_persons_age(persons)
print(total_age)
