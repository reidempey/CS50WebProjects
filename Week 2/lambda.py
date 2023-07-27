people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# def f(person):
#     return person["name"]

# TQ: How does the sort function work? How does it know to take an array-like thing that gets returned from f as the input?
# people.sort(key=f)

people.sort(key= lambda person: person["name"])

print(people)