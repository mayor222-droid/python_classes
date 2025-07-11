# assignment = 45

adddition = 45 + 200
print(adddition)#
# subtraction
a = 45
b = 200
c = b - a
print(c) # 155


# multiplication  
a= 45
b= 200
c= a * b
print(c)


# division / returns float
d = b/ a
print('d: ' ,d)    
# floor division // returns int
e = b // a
print('e: ',e)

# modulus returns remainder 
f = b % a
print('f: ',f)

# exponentiation ** returns power
g = a ** 5
print('g: ',g)
print(45*45*45*45*45)

# comparison operators return boolean values
# == checks if two values are equal
print(45 == 45) # True
print(45 == 46) # False
print(a == b) # False

# != checks if two values are not equal
print(45 != 45) # False
print(45 != 46) # True
print(a != b) # True

# > checks if left value is greater than right value
print(45 > 45) # False
print(45 > 46) # False
print(b > a) # True

# < checks if left value is less than right value
print(45 < 45) # False
print(45 < 46) # True
print(b < a) # False

# >= checks if left value is greater than or equal to right value
print(45 >= 45) # True
print(45 >= 46) # False
print(b >= a) # True

# <= checks if left value is less than or equal to right value
print(45 <= 45) # True
print(45 <= 46) # True
print(b <= a) # False

# logical operators return boolean values
# and returns True if both values are True
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
# eg 
print(45 > 46 and 45 < 46) # False
print(a <b and 46>a) # True


# or returns True if at least one value is True
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
# eg
print(45 > 46 or 45 < 46) # True
print(a <b or 46>a) # True  

# not returns True if value is False and vice versa
print(not True) # False
print(not False) # True
# eg
print(not (45 > 46)) # True
print(not (a < b)) # False  

# short hand operators
# += adds value to variable
number_ =13 

number_ = number_ + 2 # long hand
print(number_) # 15
number_ += 2 # short hand

print(number_) # 17
# -= subtracts value from variable
number_ = number_ - 2 # long hand
print(number_) # 15
number_ -= 2 # short hand 
print(number_) # 13

# *= multiplies value to variable
number_ = number_ * 2 # long hand
print(number_) # 26
number_ *= 2 # short hand
print(number_) # 52

# /= divides value from variable
number_ = number_ / 2 # long hand
print(number_) # 26.0
number_ /= 2 # short hand
print(number_) # 13.0 

# membership operators return boolean values
# in checks if value is in iterable
list_of_numbers = [1, 2, 3, 4, 5]
print(1 in list_of_numbers) # True
print(6 in list_of_numbers) # False

# not in checks if value is not in iterable
print(1 not in list_of_numbers) # False
print(6 not in list_of_numbers) # True


