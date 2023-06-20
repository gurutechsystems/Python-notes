#Helps to make different data types compatible.We have implicit and explicit data types

#1)implicit type conversion example
print('\n#Example for implicit type conversion')
x=10
print('x is of type:', type(x))

y=10.5
print('y is of type:', type(y))

z=x+y
print('z is of type:', type(z))

#2)Explicit type conversion example
print('\n#Example for explicit type conversion')

#initialising string
s='1020'

#convert string to int
i=int(s)

#===>'{}' This creates a dictionary with no key-value pairs in it.You can add new key-value pairs to the dictionary
print('After converting to integer:{}, type:{}, name:{}'.format(i, type(i), 'Obase'))
print('After converting to integer:', i, 'type:', type(i), 'name:', 'Obase')

#convert string to float
f=float(s)

print('After converting to integer:{}, type:{}, name:{}'.format(f, type(f), 'Obase'))


#Example of explicit type conversion using input

print('\n# Example for implicit type conversion using input')

age=input('enter your age?')
print('age:{}, type:{}'.format(age, type(age)))
new_age=int(age)
print('age:{}, type:{}'.format(new_age, type(new_age)))