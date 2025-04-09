friends =["bola","bolu","abiola","abisoye"]
print(friends)
print(friends[2])
print(friends[3])
friends[3]="Aisha"
print(friends)
print(len(friends))

friends.append(3)
name_to_be_in_last_pos="adebayo"
friends.append(name_to_be_in_last_pos)
print(friends)

position = 2
name_to_insert = "Blessing"
friends.insert(position,name_to_insert)
print(friends)

name_to_remove ="adebayo"
friends.remove(name_to_remove)
print(friends)

name_to_pop = friends.pop()
print(name_to_pop)
print(friends.pop())
print(friends)

mixed_cart =[
    "dress",
    90000.00,
    20,
    True,
    "white",
    "blue",
    "pink",
    {"name": "dress" , "quatity": 20}
    ]
print(mixed_cart[7])

print(mixed_cart[-2])

mixed_cart.append(2)
item_to_be_in_last_pos="Hurry up"
mixed_cart.append(item_to_be_in_last_pos)
print(mixed_cart)

position = 3
data_to_insert ="only 5 left"
mixed_cart.insert(position,data_to_insert)
print(mixed_cart)

item_to_remove = True
mixed_cart.remove(item_to_remove)
print(mixed_cart)

items =[20,10,11
]
print(items)

#bonus challenge
items = ["35",32.5,"false","apple","{'int': '35', 'bool': 'false'}"]
print(items)
print(items[4])
items[4]= "egg"
print(items)

item_to_remove =32.5
items.remove(item_to_remove)
print(items)

