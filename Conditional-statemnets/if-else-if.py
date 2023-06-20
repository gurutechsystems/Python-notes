# if --> to handle single case
# if-else --> to handle two cases
# if-else-if --> to handle more than two cases

"""
syntax:
if (condition):
    statement
elif (condition):
    statement
elif (condition):
    statement
.
.
else:
    statement
"""
# if-else-if example-1
print('\n# if-else-if example-1')
people=30
cars=40
buses=15

if cars<people:
    print('manage the people to fill all the cars')
elif cars>people:
    print('each person should own a car')
else:
    print('we should ensure equal number of people and cars')

if people>buses:
    print('2 persons per bus')
elif people<buses:
    print('There will be an empty boss')
else:
    print('ensure that all the buses arrive destination') 

# if-else-if example-2
print('\n# if-else-if example-2')
marks=int(input('what is your exam score?'))
print(marks, type(marks))
grade=None

if marks>=80 and marks<=100:
    print('congrats,U got an A')
    grade='A'
elif marks>=70 and marks<=100:
    print('congrats, U go a B')
    grade= 'B'
elif marks>=60 and marks<=100:
    print('Average, you got a C+')
    grade='C+'
elif marks>=50 and marks<=100:
    print('Average, u got a C but can do better')
    grade='C'
else:
    print('Sorry, u did not pass the exam.work harder')
    grade='F'   

    print('Fill grade:{} in the sheet'.format(grade))  



# if-else-if example-3
print('\n# if-else-if example-3')
print('u enter a dark room with 2 doors.Do u go through door #1 or #2?')
door=input('what\'s the door number u chosed?')

if door=='1':
    print('there\'s a big cat here eating a mouse, what do i do?')
    print('1=scream at the cat')
    print('2=chase the cat away from the mouse')
  
    cat=input('>')

    if cat=='1':
        print('It\'s a stubborn cat')
    elif cat=='2':
        print('the mouse is already dead')
    else:
        print('the cat ran away after i screamed')  

elif door=='2':
    print('what are the items you want to buy here?')
    print('1> A good suit')
    print('2> Quality black shoes')
    print('3> immaculate white shirt')

    items=input('>')

    if items=='1':
        print('Sir, we\'ve got the best suits in the world')
    elif items=='2':
        print('Here are quality gentleman shoes')
    elif items=='3':
        print('these are the shirts we got')
    else:
        print('sorry sir, we sell only female dresses here')
else:
    print('Switch on the light to see the 2 doors clearly')                

