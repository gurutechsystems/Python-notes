#Used to store data that cannot be modified or changed i.e immutable data
#A tuple is a collection of python objects seperated by commas. Similar to a list,nested and repetition objects but immutable

numbers = (1, 2, 3)
names = ('Ngembane', 'Benbella', 'Obase')
fruits = ('apple', 'banana', 'orange', 'grape')
my_tuple = (10, 20, 30, {"name": "Obase", "age": 32}, ['car', 'bike', 'bus'], 10)

#Print Tuples
print('\n# Print the tuples')
print(numbers)
print(names)
print(fruits)
print(my_tuple)

# verify the type of data structure
print('\n# verify tuples data types')
print(numbers, type(numbers))
print(names, type(names))
print(fruits, type(fruits))
print(my_tuple, type(my_tuple))

#Accessing tuple items(To access items in a tuple variable,we use their index values)
print('\n# Access tuple items')
print(names[1])
print(my_tuple[3])
print(numbers[0])

# checking if item exists in the tuple
print('\n# check if an item exist in a tuple variable')
print(10 in numbers)
print('Obase' in names)

if 'banana' in fruits:
    print('yes')
else:
    print('fruit does not exist')    

#Checking the methods and attributes available for the tuple variable    
print('\n# dir() method')
print(dir(fruits))

#Checking length of Tuple variables
print('\n# check the length of a tuple variable')
print(len(my_tuple))
print(len(names))

#Checking number of times an items is present in the tuple using count() methid
print('\n# get how many times an item is present in a turple')
print(my_tuple.count(10))
print(fruits.count('apple'))

# getting the index value of an item in the tuple using index() method
print('\n# get the index value of an item in a tuple')
print(my_tuple.index(30))
print(names.index('Benbella'))

# iterate over items in the tuple
print('\n# go through items in a tuple')
for each_item in my_tuple:
    print(each_item)

# delete the tuple completely
print('\n# delete a tuple completely')
del numbers
print(numbers)
