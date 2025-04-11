# variables
age=24
name='glory'
glory_friend='omowumi' 

# data types
#integer
age = 24
print(age, type(age))

#float
weight = 30.9
print(weight, type(weight))

#boolean
is_glory = False
print(is_glory,type(is_glory))
not_glory = True
print(not_glory,type(not_glory))

#string
name ='glory'
print(name,type('glory'))


age = 24
age_str =str(age)



print("#################################################################")
print("typecasting from integer to string")

age = 24
age_str =str(age)
print(age_str, type(age_str))

print("###############################################################")
print("typecasting from integer to float")

age = 24
age_float =float(age)
print(age_float, type(age_float))


print("#####################################################################")
print("typecasting from float to integer")

weight = 30.9
weight_int =int(weight)
print(weight_int, type(weight_int))

print("#####################################################################")
print("typecasting from float to string")

weight = 30.9
weight_str =str(weight)
print(weight_str, type(weight_str))


print("########################################################################")
print("typecasting for string to integer")
age_str = '30.9'
age_float= float(age_str)
age = int(age_float)
print(age,type(age))



try:
  hello="19"
  print(int(hello))
except:
  print(int(hello))



print("########################################################################")


# string concatenation using + operator
first_name ='glory'
last_name  = 'alabi'
full_name = first_name + ' ' + last_name
print(full_name)  
sentence1 = 'My name is ' + first_name + ' ' + last_name
# to concatenate to string, we need to convert it to string first
sentence2= 'I am ' + str(age) + ' years old.'
class_name = 'python developer'
sentence3 = 'I am in ' + class_name + ' class. '
full_sentence = sentence1 + ' ' + sentence2 + ' ' + sentence3
print(full_sentence)

print("#############################################################################")

# f -spring
aka= "mayor-driod"
sentencewhat = f'my names are {first_name} {last_name}, aka {aka} with a composure, I am {age} years old, I am in {class_name} class.'
print(sentencewhat)