#the variable concept in python example-1
items_count = 100
customer_name = 'Obase'
is_the_bill_paid = False
unit_price = 10.8

print('\n#Variable example-1')
print('items_count:',items_count,  'type of items_count:',type(items_count),  'memory location:',id(items_count))
print('customer_name:',customer_name,  'type of customer_name:',type(customer_name),  'memory location:',id(customer_name))
print('is_the_bill_paid:',is_the_bill_paid,  'type of is_the_bill-paid:',type(is_the_bill_paid),  'memory location:',id(is_the_bill_paid))
print('unit_price:',unit_price,  'type of unit_price:',type(unit_price),  'memory location:',id(unit_price))

print('total bill to be paid:',items_count*unit_price)

#Variable example-2
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars -  drivers
cars_driven = drivers
car_capacity = cars_driven*space_in_a_car
average_passenger_per_car = passengers/cars_driven

print('\n#Variable example-2')
print('There are', cars ,'cars available')
print('There are only', drivers, 'drivers available')
print('There will be',cars_not_driven,'empty cars today')
print('we can transpoart',car_capacity, 'people today')
print('we have', passengers, 'today')
print('we need to put about',average_passenger_per_car, 'in each car')

#Variables example-3 using 'format string'
name = 'Ngembane'
age = 32
height = 2 #cm
weight = 86 #kg
eye_color = "brown"
teeth_color = 'white'
hair_color = 'black'

print('\n#Variable example-3 using format string')
print('Lets us talk about %s.' %name)   #%s is format string operator used to represent string
print('He is %d cm tall.' %height)      #%d is format string operator used to represent int(integer)
print('He is %d kg in weight.' %weight) #%r is format string operator used to represent a string using "repr" representation
print('He has %s eyes, %s teeth and %s hair.' %(eye_color, teeth_color, hair_color))
print('He is %d of age.' %age)

print('If i add %d, %d and %d i get %d.' %(age, height, weight, age + height + weight))