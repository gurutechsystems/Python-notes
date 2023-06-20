#Used to store multiple data or items in a single variable

#list of variables
fruits = ['banana', 'apple', 'mango', 'pear']
prices = ['$100', '$150', '$200', '$50']
numbers = [1,2,3,4,5]
my_list = [5, 'car', 10.58, True]

#print the list items
print('\n# print items on list')
print(fruits, id(fruits))
print(prices)
print(numbers)
print(my_list, id(my_list))

#check data type of list
print('\n# check data type of list items')
print(type(fruits))
print(type(prices))
print(type(numbers))
print(type(my_list))

#Nested list(list within a list)
print('\n# nested list')
custom_list=[fruits, prices, [1,2,3]]
print(custom_list)

#length of list
print('\n# length of list')
print(len(fruits))
print(len(numbers))

#Accessing a particular element in a list(use index value)
print('\n# Access a specific item in a list')
print(fruits[2])  #[-2] this will return 2nd to last item on the list
print(prices[1])  #[-1] this will return last item on the list
print(my_list[3])

#Slicing a list(these are items in the list between  the index values)
print('\n# slicing lists')
print(fruits[0:2])  #ans=0,1 index values EXCLUDES THE MAPPED INDEX VALUE
print(numbers[1:4]) #ans=1,2,3 index values
print(my_list[1:])  #ans=1,2,3.... index values
print(fruits[:]) # this assumes 0 as the default index and will return all items in the list

##Performing actions on an existing list
#Checking the methods and attributes available for the list variable.
#Return attributes and methods of an object.Attributes are data values that are associated with an object.
print('\n# dir() method') #The dir() method is a built-in Python function that returns a list of all the valid attributes and methods of an object
print(dir(fruits)) #This will print out a list of all the attributes and methods of the fruits object using the dir() method.

#Modifying index values of a list item
print('\n# modify particular index value of a list with new items')
print(prices)
prices[1]='$1000'
print(prices)

#Append(add) items to an existing list
print('\n# append() method')
fruits.append('watermelon')
print(fruits)

#copy items to an existing list to a new list
print('\n# copy method')
fruits2 = fruits.copy() #this will copy items in fruits to fruits2
fruits.append('watermelon') #this item will be added only to the fruits variable without affecting fruits2
print(fruits)

#Sort a list(this will sort out a particular list and display the items in the list)
print('\n# sort list')
fruits.sort()
print(fruits)

#Sort a list(this will sort out a particular list and display the items in the list in reverse order)
print('\n# sort list')
fruits.sort()
fruits.reverse()
print(fruits)

#Insert items to a list with particular index value(this will add the item in the list and assign it the index value while the previous item having the index value will move forward)
print('\n# insert items to a particular index value')
fruits.insert(1, 'grapes')
print(fruits)

#Removing an item from a list
print('\n# delete an item from a list')
fruits.remove('pear')
print(fruits)

#Removing the last item in a list
print('\n# delete last item in a list')
fruits.pop()
print(fruits)

#checking the existence of an item in a list
print('\n# check if item exist in a list')
fruits.index(0)
print(fruits)

#Iterate(go through) over all items in a list, one after the other
print('\n# go through over all items in a list, one after the other ')
for fruit in fruits:
    print(fruit)

#Iterate(go through) each items in a list along with item index value
print('\n# Go through each item in the list along with item index value')
for index, each_item in enumerate(fruits):
    print(index, each_item)

#list with dictionaries inside
print('\n# list with dictionaries inside')
students=[{'name': 'Obase', 'marks': 75}, {'name': 'Ngembane', 'marks': 80}, {'name': 'Bnebella', 'marks': 75}]
print(students)

#Clear a list(this will remove all the variable in a list varaible without deleting the list itself)
print('\n# clear a list')
custom_list.clear()
print(custom_list)

#write a program to find the highest number in a list
print('\n# get highest number')
number = [3,6,2,8,4,10]
max=number[0]

for item in number:
    if item> max:
        max=item
print(max)   

#WRITE A PROGRAM TO REMOVE DUPLICATES IN A LIST
items = [2,2,4,6,3,4,6,1]
unique=[] #empty list.  So we iterate over the 'items' and add the unique items in the "unique" list

for item in items:
    if item not in unique:
        unique.append(item)
print(items)        
#Delete the complete list
print('\n# delete a complete list')
del my_list
print(my_list) #NameError: name 'my_list' is not defined


