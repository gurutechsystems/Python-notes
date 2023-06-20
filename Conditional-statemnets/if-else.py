#These are conditions taken into consideration before executing a particular block of code
# python program to illustrate the 'If-esle' condition statement

#if-else condition statement- example 1 
print('\n# if-else condition-example 1')
age=32

if (age<18):
    print('Allow inside')
else:
    print('kids not allowed inside')    

#if-else condition statement- example 2    
print('\n# if-else condition-example 2')
is_the_train_in_two_mile=True

if is_the_train_in_two_mile==False:
    print('close the gate')
else:
    print('open the gate')    

#if-else condition statement- example-3    
print('\n# if-else condition-example-3')
people=20
cats=40
dogs=10

if people<cats:
    print('each person is entitled to 2 cats')
else:
    print('each household should own a cat')   
if people<dogs:
    print('too many dogs,danger to the society')
else:
    print('vaccinate your dog regularly')
if people<=dogs:
    print('people are less than or equal to dogs')
else:
    print('seems we have equal number of people and dogs')
if people==dogs:
    print('each household needs a dog')
else:
    print('we need more dogs')         