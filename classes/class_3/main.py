
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
# print(student)
# print(student['name'])
# print(student['age'])
# print(student['level'])
# print(student['department'])
# print(student.get('city'))
# print(student.get('name'))
# print(student.get('country'))


composition=f'My name is {student.get("name")} and I am {student.get("age")} years old. I am from {student.get("city")} and I am in {student.get("department")} department. My Father\'s name is {student.get("surname")}'
# print(composition)



composition2=f"My name is {student.get("name")} and I am {student.get("age")} years old. I am from {student.get("city")} and I am in {student.get("department")} department. My Father\'s name is {student.get("surname")}. I love the quote \"Almost Done is not Done\" "
# print(composition2)

# \n means new line
# composition3=f"My name is {student.get("name")} and I am {student.get("age")} years old. \n I am from {student.get("city")} and I am in {student.get("department")} department.\n My Father\'s name is {student.get("surname")}. \n I love the quote \"Almost Done is not Done\" "
# print(composition3)

# dictionary methods
# keys()
print(f'keys are: {student.keys()}')
# values()
print(f'values are: {student.values()}')
# items()
print(f'items are: {student.items()}')

#get 
print(student.get('nationality'))
key_to_find='country'
try:
    print(student[key_to_find])
except KeyError:
    print(f'KeyError, {key_to_find} not found')

def get(key):
    try:
        return student[key]
    except KeyError:
        return None
    
print(get('country'))

# pop
# name= student.pop('name')
# print(name)
# print(student)

# update 
student.update({'secondary_school':'VISA','name':'John', 'age': 25, 'city': 'Lagos', })
# print(student)
# assigning 
student['name']='Seun'
student['food']= 'rice'
# print(student)


# set
set_of_numbers={1,2,3,4,5,6,7,8,6,7,6,8,8,8,}
print(set_of_numbers)

# methods
# add() is used to add 1 
set_of_numbers.add(23)

print(set_of_numbers)
# update is used to add list of values 
set_of_numbers.update(['shoe','bag', 45.347,'rice'])
print(set_of_numbers)

# set operation 
even_numbers={2,4,6,8,10,12,14,16,18,20}
odd_numbers={1,3,5,7,9,11,13,15,17,19}
# print(even_numbers.union(odd_numbers))
# print(even_numbers.intersection(set_of_numbers))
# print(even_numbers.difference(odd_numbers))

# typecasting
# list to set 
list_of_clubs=['Man u','Barca','Real','Chelsea','Arsenal']
# print(list_of_clubs)
set_of_clubs=set(list_of_clubs)
print(set_of_clubs)

#set to list 
list_of_clubs=list(set_of_clubs)
# print(list_of_clubs)
# set to tuple
tuple_of_clubs=tuple(set_of_clubs)
# print(tuple_of_clubs)
# tuple to set
set_of_clubs=set(tuple_of_clubs)
# print(set_of_clubs)

# set to dict







# range(from, to+1, steps)
list_of_numbers=[]
print(list_of_numbers)

for number in range(11):
    list_of_numbers.append(number)
print(list_of_numbers)

# for number in range(1,11,):
#     print(number)
for number in range(1,11,3):
    print(number)

#