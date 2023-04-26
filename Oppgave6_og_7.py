#Task 6
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

def average_age(persons):
    total_age = sum(person["age"] for person in persons)
    num_persons = len(persons)
    if num_persons > 0:
        return total_age / num_persons
    else:
        return 0
      
avg_age = average_age(persons)
print("Average age:", avg_age)

#task 7

def max_age(persons):
    max_age = persons[0]["age"]
    for person in persons:
        if person["age"] > max_age:
            max_age = person["age"]
    return max_age

def min_age(persons):
    min_age = persons[0]["age"]
    for person in persons:
        if person["age"] < min_age:
            min_age = person["age"]
    return min_age

print(max_age(persons)) 
print(min_age(persons)) 
