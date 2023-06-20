#Comaprison of Relational operators.Used to compare 2 values. The result is either true or false depending on the condition

a=13
b=33

#conditions
#a>b is False
#a>=b is Flase
#a==b is False
#a!=b is True(!= not equal to in python)
#a<b is True
#a<=b is True

#Results
print(a>b)
print(a>=b)
print(a==b)
print(a!=b)
print(a<b)
print(a<=b)

#EXAMPLE 2
temperature = 30

if temperature>25: # change comparison signs and check result
    print("it's a hot day")
else:
    print("it's a normal weather")    

#Example 3: write a program to control username xters in creating a username
"""
if name is less than 9 xters
    name must be at least 9 xters
otherwise if name is more than 50 xters long
    name cannot be above 50 xters
otherwise
    username created successfully        
"""
username= "Benbella"

if len(username) < 9:
    print('username must be atleast 9 characters')
elif len(username) > 50:
    print('username cannot be above 50 characters')
else:
    print('username created successfully')    