# variables
age=34
name ='Mayor'
mayor_friend= 'Bisola'

# data types
# integers
age = 34
print(age,type(age))
# float
height = 5.9
print(height,type(height))
# boolean
is_mayor = True
print(is_mayor,type(is_mayor))

not_mayor = False
print(not_mayor,type(not_mayor))

# string
name = 'Mayor'
print(name,type(name))



# typecasting means converting one data type to another
# converting integer to string
print("#########################################################")
print('typecasting for integer to string')

age = 34
age_str = str(age)
print(age_str,type(age_str))

print("#########################################################")
print('typecasting for integer to float')

age = 34
age_float = float(age)
print(age_float,type(age_float))

print("#########################################################")
print('typecasting for float to integer')
height = 5.9
height_int = int(height)
print(height_int,type(height_int))

print("#########################################################")
print('typecasting for float to string')
height = 5.9
height_str = str(height)
print(height_str,type(height_str))

print("#########################################################")
print('typecasting for string to integer')
age_str = '34.9'
age_float= float(age_str)
age = int(age_float)
print(age,type(age))
print("#########################################################")

try:
    name = "79"
    print(int(name))
except :
    print("Error: Cannot convert string to integer. Please provide a valid number.")



print("################################################################################################################")

# String Concatenation
# string concatenation means joining two or more strings together
# string concatenation using + operator
first_name = 'Mayor'
last_name = 'Ogunyemi'
full_name = first_name + '' + last_name
print(full_name)
sentence = 'My name is ' + first_name + ' ' + last_name
# to concatenate int or float with string, we need to convert it to string first
sentence2='I am ' + str(age) + ' years old.'
class_name = 'Python Developer'
sentence3 = 'I am in ' + class_name + ' class.'
full_sentence = sentence + ' ' + sentence2 + ' ' + sentence3
print(full_sentence)


print("#########################################################")

# f-string
# f-string is a new way of formatting strings in python

# f-string is a string literal that is prefixed with the letter 'f'
# f-string is used to evaluate expressions inside string literals
# f-string is used to format strings in a more readable way
# f-string is used to format strings in a more efficient way
# f-string is used to format strings in a more flexible way
aka= 'Mayor-droid'
sentencewhat = f'My names are {first_name} {last_name}, aka {aka} with a steeze, I am {age} years old, and I am in {class_name} class.' 
print(sentencewhat)