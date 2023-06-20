#Used to list a multple items in a variable avoiding duplication of any items.It is an unordered collection of data that is iterable, mutable and has no duplicate element

numbers = {10, 20, 5, -3}
students = {"Ngembane", "Benbella", "Obase"}
fruits = {"apple", "banana", "orange"}
my_set = {10, 20, 'apple', 'car'}

#Print set
print('\n# print the sets')
print(numbers)
print(students)
print(fruits)
print(my_set)

# what will happen when we try to add duplicate element to the set
# even though we try it wont let as add it as the same item already exists in the set
# we can compare set to a playlist of songs
print('\n# test item duplication in set')
duplicate_item_set={10, 20, 30, 10}
print(duplicate_item_set)

# Indexing --> set doesnt suppport indexing like lists & tuples do
# Therefore You cannot access items in a set by referring their index value or a key.
#  But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""
print('\n #indexing check in the set') #does not support indexing like list and tuple
print(students[0])
"""

#Checking if an item exists in the set
print('\n# check if an item exist in a set')
if 'Obase' in students:
    print('yes')
else:
    print('no') 

print('orange' in fruits)       

# check type of the set variables with type() method
print('\n # check data type of the set variables with type() method')
print(numbers, type(numbers))  #OR just print(type(numbers))
print(students, type(students)) #OR just print(type(students))

#Checking the methods and attributes available for the set variable
print('\n# dir() method')
print(dir(fruits))

#Checking length of set variables
print('\n# check the length of a set variable')
print(len(my_set))
print(len(students))

# adding a new item or modifying an item in set 
# wont happen because we have already seen that set doesnt support indexes so we cant assign values with index
print('\n # adding an a new item or modifying an item in set')
# students[0]='jenny'
# print(students)

# so the correct way to do it is via the set built-in method add()
print('\n# adding a new item in a set')
students.add('mega')
print(students)

# what will happen if we try to add the same value (remember set cant have a duplicate value)
print('\n # what will happen if we try to add the same value (remember set cant have a duplicate value)')
students.add('mega')
print(students)

# adding multiple values to an existing set using update() built-in method
print('\n# add mutiple items to an esisting set')
fruits.update(['mango', 'pear', 'grapes'])
print(fruits)

# remove an existing item from the set using remove() built-in method
print('\n# remove an item from a list')
fruits.remove('grapes') #can only remove one item at a time
print(fruits)

# lets understand what will happen when we try to delete an item that doesnt exists in the set
# it will throw an error saying that the item key isnt found in the set
# students.remove("jenny")

# lets understand how to easily delete if a key exists otherwise ignore instead of raising an error
print('\n# understand how to easily delete if a key exists otherwise ignore instead of raising an error')
if 'mango' in fruits:
    fruits.remove('mango')
    print(fruits)
else:
    print('given item not found')   
    print(fruits) 

# other way to do the same step as above is using discard() method which is really simple
print('\n #trying deletion via discard')
students.discard('mega')
students.discard(12345)
print(students)

# iterate over all items in set and access individual items
print('\n# go through all items in a set and access individual items')
for a in students:
    print(a)

for n in fruits:
    print(n)    

# set union
# reminder --> set wont have duplicates so even after union no duplicates
print('\n# set union')
u=numbers.union(my_set) #adding the numbers and my_set variables
print(u)

# setting intersection --> to get common data between two sets
print('\n# get common data between 2 sets')
i=numbers.intersection(my_set)
print(i)

# clear all items from set
print('\n# clear all items from a set')
fruits.clear()  #takes no argument
print(fruits)

# delete the complete set
print('\n# delete the complete set')
del fruits
print(fruits)

