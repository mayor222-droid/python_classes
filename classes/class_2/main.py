friends =["taye", "kehinde","idowu"]
print(friends)
print(friends[1])
print(len(friends))
friends[2]="omowumi"
print(friends)

# [square brackets] are used to access items in a list
# ( braces) are used to access items in a tuple
#{ curly braces} are used to access items in a dictionary
# {   "key": "value",}
# {set of items}
# {1,2,3,4,5,6,7,8,9,10}
animals =("dog", "cat", "lion", "tiger", "elephant",'cat', 'dog', 'giraffe')
print(animals.count('cat'))
shopping_cart =[
98.99,
"shoes",
10,
"a cover shoe , versace product, "
"heel",
True,
True,
True,
3
]
print(shopping_cart[3])
#how to print the last item
print(shopping_cart[-1])
print(shopping_cart[-2])

#list methods
# method is a function that belongs to an object
# function is a block of code that can be called many times to perform a particular task

#1 append is used to add item to the end of a list
shopping_cart.append(2)
item_to_be_in_last_pos='Hurry to buy now'
shopping_cart.append(item_to_be_in_last_pos)
print(shopping_cart)

#2 insert is used to add item to a list at a specified position
position = 3
data_to_insert ="15 pieces remaining"
shopping_cart.insert(position,data_to_insert)

print(shopping_cart)

#3 remove is used to remove an item from a list
item_to_remove =True
shopping_cart.remove(item_to_remove)
print(shopping_cart)

# 4 pop is used to remove an item from a list and return the item
item_to_pop = shopping_cart.pop()
print(item_to_pop)
print(shopping_cart.pop())

print(shopping_cart)



# 4 sort is used to sort a list in ascending order, is used for int and float
shopping_cart.sort()
print(shopping_cart)






