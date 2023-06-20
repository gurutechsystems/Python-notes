#These are conditions taken into consideration before executing a particular block of code
# python program to illustrate the 'If' condition statement

#IF condition statement- example 1
print('\n# IF condition-example-1')
age=32

if age>18:
    print('Allow inside')

#IF condition statement- example 2    
print('\n# IF condition-example-2')
is_the_train_two_miles_away=True

if is_the_train_two_miles_away==True:
    print('close the gate')

#IF condition statement- example 2
print('\n# IF condition-example-3')
people=20
cats=40
dogs=10

if people<cats:
    print('each person is entitled to 2 cats')
if people>cats:
    print('each household should own a cat')   
if people<dogs:
    print('too many dogs,danger to the society')
if people>dogs:
    print('vaccinate your dog regularly')
if people<=dogs:
    print('people are less than or equal to dogs')
if people>=dogs:
    print('seems we have equal number of people and dogs')
if people==dogs:
    print('each household needs a dog')                     

#IF condition statement- example 3
"""
if it's hot
    it's a hot day
    drink plenty of water
otherwise if it's cold
    it's a cold day
    wear warm clothes
otherwise
    it's a lovely day         
"""
is_hot = False #True  
is_cold =True  #False 

if is_hot:
    print("it's a hot day")
    print('drink plenty of water')
elif is_cold:
    print("it's a cold day")
    print('wear warm clothes')
else: 
    print('Enjoy ur day')    