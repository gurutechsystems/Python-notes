#Used for sequential traversal e.g traversing a list,string etc
#for_loops are used when doing operations on elements of a sequence in order
#while_loops are used when doing operations on multple elements of a sequence out-of-order,operate on multiple elements simultaneously

"""
Syntax:
for iterator_var in sequence:
    statements
"""

# Iterating over a string
print('\n# iterate over a string variable')
name='Ngembane' #string variable

for each_letter in name:
    print(each_letter.upper())

# Iterating over a list
print('\n# iterate over a list variable')
fruits=['apple', 'mango', 'banana', 'grapes']

for each_fruit in fruits:
    print(each_fruit.lower())

# range() function
# range funtion will return the sequence of numbers one lesser than what we have mentioned
# range(5) will return-->  0,1,2,3,4 in a list
print('\n# range() method example')
for i in range(5):
    print(i)


# so if we want numbers from 0-9 we dont have to create a specific list for it we can simply write the code as below
print('\n# range from 0-5')
for i in range(5):
    print('enter ur pin:', i)

# if we need a starting number from 2
print('\n# range from 2-9')
for i in range(2,10):
    print(i)

# if we need a starting number from 2,and if we want to specify the incremental value from 1 to any other number (3 for example)    
print('\n# range from 2-9 & with increment of 3')
for i in range(2, 10, 3):
    print(i)

# so the range method syntax is --> range(start_value, stop_value, increment_value)   


#Example-2
print('\n# for loop example-2')
count=[1,2,3,4,5]
fruits=['apple','banana','mango']

for number in count:
    print('this is count %d' %number) #this prints the statement and list the numbers alongside
    #OR
    print(number) #this just print the numbers only

for fruit in fruits:
    print('this fruit is %s' %fruit)    
    #OR
    print(fruit)

#Example-3
for item in 'python':
    print(item)

#Example-4
for item in ['Ngembane', 'Benbella', 'Obase']:
    print(item)        

#WRITE A PROGRAM TO CALCULATE THE TOTAL COST OF ITEMS IN A SHOP
prices=[10,20,30]
total = 0

for item in prices:
    total = total + item # total += item
print(total)    
