#String help us to deal with string related tasks in our environment/built-in methods.
#It is defines as either a sing qoute('') or double qoutes("")
#Understanding string operations and built-in methods

name = "Obase"
price = "$100"
quantity = "10 items"

#Printing string values
print('\n# print string values')
print(name)
print(price)
print(quantity)

#check string data type
print('\n# print string data type')
print(type(price))
print(type(quantity))

#check if specific character present in string
print('\n# check if a particular element present in string')
print('a' in name)

#Finding a specific character in a string variable
print(name.find('O')) #this will give the index value of the xter if present in the string variable

#Length of string
print('\n# length a string variable')
print(len(quantity))
print(len(name))

#Accessing specific element in the string with index values
print('\n# access a particular character in a string with index values')
print(name[0])  #forward indexing
print(name[1])
print(name[-1]) #reverse indexing
#print(name[5])  #string index out of place

# string slicing --> to get the specific subset of string
print('\n# get a specific subset of a string')
print(quantity)
print(quantity[2:5])
print(price[:2])

#Checking the methods and attributes available for the string variable
print('\n# dir() method')
print(dir(quantity))

# replacing a string elements using replace() built-in method
print('\n# replace string element')
new_name=name.replace('i', 'e')
print(new_name)

new_quantity=quantity.replace('10', '20')
print(new_quantity)

# remove white spaces from the beginning or end of a string using strip() built-in method
print('\n# remove empty spaces from beginning and end of strings')
new_quantity=quantity.strip()
print('quantity:',quantity,'length:',len(quantity))
print('quantity:',new_quantity,'length:',len(new_quantity))

# convert string characters to upper or lower case
print('\n# convert string characters to Upper or Lower case')
new_name=name.upper()
print(name, new_name)

new_name=name.lower()
print(name,new_name)

# split string based on values
print('\n# split a string based on values')
message='Hello, Obase!'
new_message=message.split()
print(new_message)

email='ngembane.obase@gmail.com'
new_email=email.split('@')
print(new_email)
print(new_email[1])