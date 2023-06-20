#Modules are simple python files that can be used in another python file or program just by referencing it.
#So, when the module is called in a python file, the code control goes to the module python file to excute the module.

"""
To get default python modules
https://docs.python.org/3/py-modindex.html
"""

import uuid     #https://docs.python.org/3/library/uuid.html#module-uuid(Universal unique identifiers=uuid)
import math     #https://docs.python.org/3/library/math.html#module-math(mathematical dunction e.g sin(), etc)
import calendar #https://docs.python.org/3/library/calendar.html#module-calendar
import json     #https://docs.python.org/3/library/json.html#module-json(encode and decode the json format)

# use methods from standard uuid module
print('\n#Use case of uuid module')
print(uuid)
print(uuid.uuid4())

# use methods from standard math module
print('\n#Use case of math module')
print(math)
print(math.ceil(10.05))  #ceil round up the rational number to next whole number(e.g 10.05-10.95=11)
print(math.floor(12.95))  #floor round down the rational number to the next whole number(e.g 12.05-12.99=12)

# use methods from standard calendar module
print('\n#Use case of a calendar module')
print(calendar)
yy=2023
mm=4
print(calendar.month( yy, mm))

# use methods from standard json module
print('\n#Used case of a json module')
print(json)
print(json.dumps({'Name':'Ngembane', 'age':32, 'profession':'DevOps Engineer'}))

#GENERATING RANDOM VALUES(chosing a leader from a list of names) 
import random  

names= ['ngembane','guru','obase','benbella']
leader=random.choice(names)
print(leader)


for i in range(3):
    print(random.random())

#EXERCISE(WRITE A PROGRAM TO GIVE DIFFERENT NUMBERS WHEN  WE ROLL A DICE)
class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first, second
    
dice=Dice()
print(dice.roll())    

