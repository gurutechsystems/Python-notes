#Used to store data in key value format

#EXAMPLE-1
print('\n#DICTIONARY EXAMPLE-1')
staff = {"name": "Obase", "age": "32 years", "profession": "DevOps-Engineer"}
fruits = {"apple": 5, "banana": 3.50, "watermelon": 2.75}
colleagues = {"DevOps-Engineer": ["Cave", "Elvis"], "Cloud-Engineer": ["Mega", "Momo"]}

#print the dictionary
print('\n# print the dictionary')
print(staff)
print(fruits)
print(colleagues)


#Accessing items in a dictionary
print('\n# access dictioanry items')
print(staff["name"])
print(fruits['apple'])
print(colleagues['Cloud-Engineer'])

#Checking if a key exist in a dictionary and then print the value
print('\n# check if a key exist in a dictioanry')
if 'banana' in fruits:
    print(fruits['banana'])
else:
    print('requested key not found')  

if 'profession' in staff:
    print(staff["profession"])
else:
    print('requested key not found')   

#Checking data type of the values(variables)
print('\n# Check data type of the variables')
print(staff, type(staff))
print(fruits, type(fruits))
print(colleagues, type(colleagues)) 

#Checking the methods and attributes available for the dictionary variable.
print('\n# dir() method')
print(dir(staff))

#Checking length of dictioanry(number of key:value pairs)
print('\n# length of dictionary variable')
print(len(staff))
print(len(colleagues))

#Getting the keys of dictionary with keys() method. This will display all the keys in the staff dictioanry
print('\n# get the key of a dictioanry with the keys() metod')
print(staff.keys())

#Getting the values of dictionary with values() method.This will display all the values in that particular dictionary
print('\n# get the vaules of dictionary usimh the values() method')
print(colleagues.values())

#Copying all the dictionary data in a variable into another variable
print('\n# copy all dictionary data from one variable into another variable')
duplicate_staff=staff.copy()
print(staff)
print(duplicate_staff)

#Modifying an existing key value in a dictionary variable
print('\n# modify existing key value in a dictionary variable')
staff['name']='Ngembane Benbella Obase'
print(staff)
fruits['apple']= 10
print(fruits)

#Removing and returning an item from a dictionary using the pop() method
print('\n# remove a key value from a dictionary variable')
age=staff.pop('age')
print(staff)
print(age)

#Adding a new key value to dictionary variable
print('\n# add a new key value to a dictionary')
staff['Team-lead']= 'Obase'
print(staff)

#Iterate over a dictionary keys using keys() method
print('\n# go throug a dictionary keys')
for key in fruits.keys():
    print(key)

#Iterate over a dictionary values using values() method
print('\n# go through a dictionary values')
for val in staff.values():
    print(val)

#Iterate over a dictionary key,value pairs using items() method
print('\n# go through a dictionary key value pairs')
for key,val in colleagues.items():
    print(key,val)

#Clear all key-value from dictionary using clear() method
print('\n# clear key,value from a dictionary')
fruits.clear()
print(fruits)    

#Deleting a key from a dictionary variable
print('\n# delete a key from a dictionary variable')
if 'banana' in fruits:
    fruits.pop('banana')
    print(fruits)
else:
    print('key not found')

#EXAMPLE-2(WRITE A PROGRAM TO CONVERT NUMBERS TO WORDS)
phone = input('phone: ')  
digits = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four'
}
output = '' #empty string
for digit in phone:                           #the space below is to ensure the words are not close to each other
    output = output + digits.get(digit, "!")  +  " " #output += digits.get(digit. '!')

print(output)

#EXAMPLE-3(emoji converter)
message=input('>') #the ">" is an indicator for a user to type a message
words=message.split(' ') #with the space, the split uses the space as a boundary to seperate multiple words into a list of strings
emojis = {
    ':)':'😂',
    ':(':'😒'
}
output=""
for word in words:
    output += emojis.get(word, word) + ' ' #if the user input is not in emoji, it will return "word"

print(output)
'''
#Delete a complete dictionary
print('\n# delete a complete dictionary')
del colleagues
print(colleagues)
'''
#EXAMPLE-4
print('\n#DICTIONARY EXAMPLE-2')
#Mapping of states to abbreviation
states={'Maryland':'MD', 'Texas':'TX', 'Michigan':'MI', 'California':'CA', 'New York':'NY'}
#Mapping cities to states
cities={'MD':'Baltimore', 'TX':'Austin', 'MI':'Detroit', 'CA':'Los Angeles', 'NY':'New York'}
#Add more cities to state mapping
cities['Oregon']='Portland'
cities['Florida']='Jacksonville'

# print out some cities
print(cities)

print('-'*20)
print('Maryland state has :',cities['MD'])  #ensure to use [ ] over () when dealing with keys and values
print('California state has:',cities['CA'])

# print some states
print('-'*20)
print('California is abbreviated as:',states['California'])
print('Maryland is abbreviated as:', states['Maryland'])

# do it by using the state then cities dict
print('-'*20)
print('Maryland has:', cities[states['Maryland']])

# print every state abbreviation
print('-'*20)
for state, abbrev in states.items():
    print('%s is abbrev %s' %(state,abbrev))

# print every city in state
print('-'*20)
for city, abbrev in cities.items():
    print('%s has capital %s' %(city, abbrev)) 

# now do both at the same time
print('-'*20)
for state, abbrev in states.items():
    print('%s state is abbreviates %s and has %s city' %(state,abbrev,cities[abbrev]))

# safely get an abbreviation by state that might not be there
print('-'*20)
state=states.get('Mississippi', None)

if not state:
    print('sorry, No Mississippi')

# get a city with a default value
city=cities.get('MS','Does not exist')
print("the city for state 'MS': %s" %city )    