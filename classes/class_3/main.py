
# tupules 
colors = ("red", "green", "blue", 'yellow', 'red', 'red' ,'black', 'green', )
print(colors[1])
# colors[1]='yellow'
# print(colors)   

#  tupule methods
# count()
# print(colors.count('green'))
# index()
print(colors.index('green'))
# len()
print(len(colors))


# dictionary 
student ={
    "name": "Mayor",
    "surname": "Alaba",
    "age": 89,
    "level": 300,
    "department": "Biochemistry",
    "city": "Akure",
    "state": "Ondo",
    "country": "Nigeria",
}
print(student)
print(student['name'])
print(student['age'])
print(student['level'])
print(student['department'])
print(student.get('city'))
print(student.get('name'))
print(student.get('country'))


composition=f'My name is {student.get("name")} and I am {student.get("age")} years old. I am from {student.get("city")} and I am in {student.get("department")} department. My Father\'s name is {student.get("surname")}'
print(composition)



composition2=f"My name is {student.get("name")} and I am {student.get("age")} years old. I am from {student.get("city")} and I am in {student.get("department")} department. My Father\'s name is {student.get("surname")}. I love the quote \"Almost Done is not Done\" "
print(composition2)

# \n means new line
composition3=f"My name is {student.get("name")} and I am {student.get("age")} years old. \n I am from {student.get("city")} and I am in {student.get("department")} department.\n My Father\'s name is {student.get("surname")}. \n I love the quote \"Almost Done is not Done\" "
print(composition3)



