#used to execute a block of statements repeatedly until a given condition is met.
#for_loops are used when doing operations on each element of a sequence in order
#while_loops are used when doing operations on elements of a sequence out-of-order,operate on multiple elements simultaneously

"""
Syntax:
while expression:
    statement(s)
"""

# while loop example 1
print('\n# while loop example 1')
wrong_pin_count=0

while(wrong_pin_count<6):
    pin_entered=False
    if pin_entered==False:
        wrong_pin_count=wrong_pin_count + 1
        if wrong_pin_count!=6:
            print('please enter your pin', wrong_pin_count)
        else:
            print('your pin got blocked', wrong_pin_count)    

# while loop example -2
print('\n# while loop example 2')
count=10

while(count > 1):
    count=count-1
    print('hello Obase, decreasing', count)
    
# # example of infinite while loop
# print('\n# example of infinite while loop')
# count = 0
# while (count < 5):
# print("Hello obase, infinite loop")    

# while loop example-3 with for_loop
print('\n# while loop example-3')
i=0
numbers=[]

while i<6:
    print('At the top i is %d' %i) #OR print(i)
    numbers.append(i)

    i=i+1
    print('Number now', numbers)

    print('At the bottom i is %d'%i)

print('The following numbers:')  

for number in numbers:
    print(number)


#Examples of while loop-4A
i=1
while i<=5:
    print(i)
    i=i+1
print('while loop ends')  

#Examples of while loop-4B
i=1
while i <=5:
    print('*' * i)
    i=1+i
print('done') 

#USING WHILE LOOP TO BUILD A GUESSING GAME
secret_number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: ')) #convert string to int cuz users input are strings
    guess_count += 1
    if guess == secret_number:
        print('login successful')
        break #use to terminate a loop
else:
    print('error, wait a while and try again')  

#USING WHILE LOOP TO BUILD A CAR GAME  
command = ""
started = False
while True:  #.lower() is to convert whatever xter the user enter to lower-case. For upper-case we say .UPPER() and set the value in upper-case
    command = input('> ').lower() # the .lower() here enable us not to repeat code when passing the condtitions and with this the command will always be in lower-case
    if command == 'start':
        if started:
            print('car already started')
        else:
            started = True
            print('car started')    
    elif command == 'stop':
        if not started:   #using the "not" operator
            print('car is already stopped')
        else:
            started = False   
            print('Car stopped')
    elif command == 'help':
        print("""
start -> to start the car
stop  -> to stop the car
quit  -> to exit the car            
        """)
    elif command == 'quit':
        break    
    else:
        print('Sorry, wrong input')    


 