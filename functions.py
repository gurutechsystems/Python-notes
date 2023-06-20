#Functions are used to modularize our code.Hence we can easily test our code,debug our code if there is any problem and we can re-use our code.
#The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to re-use code contained in it over and over again.

"""
Syntax:
def function_name(parameters):
    statement
    return expression
"""

#Simple python function example 1
print('\n#Simple python function example 1')

def hello():
    print('hello Ngembane, welcome to USA')

#Calling the existing function
print('\n#Caliing the function defined')
hello() 

#Simple python function example 2
def greet_user():
    print('Hi there')
    print('welcome aboard')
print('start')
greet_user()
print('finish')   

#Passing information to a python function(when a function has a parameter, we must pass a value for the parameter)
def greet_user(name): #the "name parameter is a place holder for receiving information"
    print(f'Hi {name} !')
    print('welcome aboard')
print('start')
greet_user("John") #so we can use this single python script to greet multiple use
greet_user('Guru')  #this makes the code re-usable
print('finish') 

#Note that these are positional arguments and the positions matter
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name} !')
    print('welcome aboard')
print('start')
greet_user('obase', 'Guru')
print('finish') 

#function with arguments(A simple python function to check if a "number" is positive or negative)
#Here, the "number" data that is passed to the function is called arguments
print('\n#Function with arguments example 2')

def check_number(number):
    if number>0:
        print('positive number')
    elif number<0:
        print('negative number')
    else:
        print('neither positive or negative number')  
#calling the function
check_number(0)
check_number(3)
check_number(-4)

#==>FUNCTIONS AND VARIABLES EXAMPLE-1
#when you dont use functions
print('\n#when u dont use function')
height=160
weight=56
bmi=((height/weight)/height)*1000
print(bmi) #static

#When u use a function
print('\n#when u use function')
def calculate_bmi(height, weight):
    bmi=((height/weight)/height)*1000
    print(bmi) #This wont give any result cuz it was defined as a function.Hence,we have to call the function

calculate_bmi(160,56)
calculate_bmi(175, 76) #This implies with functions, our codes are dynamic and can be used in different envs

#==>FUNCTIONS AND VARAIABLES EXAMPLE-2
print('\n#Functions and variables example-2')
def cheese_and_crackers(cheese_count, boxes_of_cracker):
    print('you have %d cheese' %cheese_count)
    print('you have %d boxes of cracker' %boxes_of_cracker)
    print('we are good to go')
    print('That is enough for a party.')

print('#we can give the function number directly/dynamically')
cheese_and_crackers(20,30) #U must move the function call outside of the function definition
    #cheese_and_crackers(20,30)  ==> calling the function inside the function definitio will not give results

print('#OR, we can use variables defined in the scripts')
cheese_count=20
boxes_of_crackers=30

cheese_and_crackers(cheese_count,boxes_of_crackers)

print('#we can even do maths inside too')
cheese_and_crackers(20+10, 30+5)

print('#Also, we can combine the two;variables and maths')
cheese_and_crackers(cheese_count+40, boxes_of_crackers+50) 

#==>Return statement in function example-1
print('\n#Using return statement in function-1')
def sum_the_numbers(a,b):
    c=a+b
    print(c)   #By default, all functions return a value
    return c   #if we don't define the return value, python will retuen the default value "None"

final_result=sum_the_numbers(10,5)
print(final_result*4)
#OR
print(sum_the_numbers(10,5)*4)

#Return statement in function example-2
print('\n#return statement in funtions-2')
def add(a,b):
    print('adding %d + %d' %(a,b))
    return a+b
def subtraction(a,b):
    print('subtract %d - %d' %(a, b))
    return a-b
def multiplication(a,b):
    print('mul %d * %d' %(a,b))
    return a*b
def division(a,b):
    print('div %d / %d' %(a,b)) 
    return a/b       

add=30+10
subtraction=30-10
multiplication=30*10
division=30/10

#Calling the function
print(add)
print(subtraction)
print(multiplication)
print(division)
#OR
final_result=add,subtraction,multiplication,division
print(final_result)

#==>Return statement in function example-3
print('\n#return statement in funtions-3')
def secret_formula(started):
    beans=started*10
    jars=beans/2
    crates=jars/4
    return(beans,jars,crates)

start_point=100
beans,jars,crates=secret_formula(start_point)

print(secret_formula(start_point))
#OR
print(beans,jars,crates)
#OR
print('With the starting point of; %d' %start_point)
print('we\'d have %d beans, %d jars and %d crates' %(beans,jars,crates))
#OR
print('we\'d have %d beans, %d jars and %d crates' %(secret_formula(start_point)))



'''
#==>Return statement in function example-4(This particular example is performed in the terminal(page103))
print('\n#return statement in funtions-4')
def break_words(stuff):  #this function will break up words
    words=stuff.split(' ')
    return words
def sort_words(words):
    return sorted(words)
def print_first_words(words):
    word=words.pop(0)
    print(word)
def print_last_words(words):
    word=words.pop(-1)
    print(word) 
def sort_sentence(sentence):
    words=break_words(sentence)
    return sort_words(words)
def print_first_and_last_sentence(sentence):
    words=break_words(sentence)
    print_first_words(words)
    print_last_words(words)
def print_first_and_last_sorted(sentence):
    words=sort_sentence(sentence)
    print_first_words(words)
    print_last_words(words)    

#==>FUNCTIONS AND FILES
#Calling functions from other files Example-1
# https://www.w3schools.com/python/ref_string_format.asp


# dependencies
import util

print('\n#Calling functions from other files')
def store_invoice_details(name, price, invoice_id):
    print('storing invoice details of customers;{}, price:{},invoice_id:{}'.format(name, price, invoice_id))
    db_credentials=util.get_db_credentials_param(name='abcd')
    print('got db credentials secret {}'.format(db_credentials))
    print('establishing db connections....')
    print('sorting the details into db....')
    print('successfully stored invoice details in the db')
    return True

result=store_invoice_details(name='Ngembane', price='$150', invoice_id='invoice-12345')
if result==True:
    print('Your invoice details are stored successfully')
else:
    print('Errors encountered while trying to store your invoice details. We have to redo it')    

#Calling functions from other files Example-2
print('\n#Functions and files')
from sys import argv #'argv' stands for "argument variable" and  is a list in the "sys" module.
                     #It contains the command-line arguments passed to a Python script.
script, input_file = argv

def print_all(f):
    print(f.read())
def rewind(f):
    print(f.seek(0))    
def print_a_line(line_count, f):
    print(line_count,f.readline())

current_file=open(input_file)   

print('#>First let us pirnt the whole file')
print_all(current_file)

print('#>Let us rewind ,kind of rewinding a tap')
rewind(current_file)

print('#>let us print 3 lines of the file')
current_line=1
print_a_line(current_line,current_file)
current_line=current_line+1
print_a_line(current_line, current_file)
current_line=current_line+1
print_a_line(current_line,current_file)
'''