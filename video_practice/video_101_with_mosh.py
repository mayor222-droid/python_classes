print('hello world')
print("*" * 10)




#running python code
#play button
#open keyboard shortcut
#run python file




#variables
#use to store data in computers memory
students_count = 1000
rating = 4.99
is_published =True
course_name = "python programming"
print(students_count)
#data types(primitive types)
#numbers(float,integers)
#booleans(to make decisions)
#stings

#srings
course = "python programming"
#a funtion is a reusable piece of code out a task
#len funtion
print(len(course))
print (course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

#escape sequence
#back slash\
#back slash \""
#back slash \'
#double back slash \\
#back slash \n for new line
course = "python \"programming"
print(course)
course = "python \\programming"
print(course)
course = "python \nprogramming"
print(course)

#formatted strings
first = "mayor"
last = "glory"
#concatenation
full = first + " " + last
print(full)
#f strings
full = f"{first} {last}"
print(full)
#len function
full = f"{len(first)} {last}"
print(full)

#strings function
course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())
#stip
course = "  python programming"
print(course.strip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("class" not in course)

#numbers(intrgers,float,complex numbers)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
x += 3

#useful functions to work with numbers
import math


print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))

#input
# y = x + 1

# int(x)
# float(x)
# bool(x)
# str(x)

#falsy(empty string "",0,none)
#truthy


#fundamentals of programming
#comparison operator
10 > 3
10 >= 3
10 < 20
10 <= 20
10 == "10"
10 != "10"
"bag" > "apple"
"bag" == "bag"

#conditional statement
temperature = 15
if temperature > 30:
    print("it's warm")
    print("drink water")
elif temperature > 20:
    print("it's nice")
else:
    print("it's cold")
print("done")

#ternary operator
age = 22
if age >= 18:
    print("eligible")
else:
    print("not eligible")
   

age= 22
if age >= 18:
    message = "eligible"
else:
    message = "not eligible"

message = "eligible" if age >= 18 else "not eligible"
print(message) 

#logical operator(and,or,not)

high_income = False
good_credit = True
student = False


if not student:
    print("eligible")
else:
    print("not eligible")

#chain comparsion operators
# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("eligible")

#loops
for number in range(1,10, 4):
    print("attempt", number + 1, (number + 1) * ",")

successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")

    # nested loops
    for x in range(5):
        for y in range(3):
            print(f"({x}, {y})")

#iterables
print(type(5))
print(type(range(5)))

# iterable
for x in [1,2,3,4]:
    print(x)

# while loop
number = 100 
while number > 0:
    print(number)
    number //= 2

# how to write funtions
# types of funtion(perform a task and return a value)
def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
     return f"Hi {name}"
    

message = get_greeting("mayor")
file = open("content.txt","w")
file.write(message)

#increment function
def increment(number, by=1):
    return number + by


result = increment(2,5)
print(result)

