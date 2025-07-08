# . Create a dictionary called student with keys: name, age, school, grade, nationality.
# 2. Use the keys(), values(), and items() methods to print respective parts of the dictionary.
# 3. Use get() to check if the key "hobby" exists; if not, print "No hobby recorded".
# 4. Try accessing a missing key using square brackets [] and handle the KeyError using try-except.
# 5. Write your own function called find key(key) that returns the value of a key from the dictionary
# or None if it doesn’t exist.

student = {
    "name": "John Doe",
    "age": 20,
    "school": "ABC University",
    "grade": "A",
    "nationality": "Nigerian"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())