#DO NOT RUN THIS SCRIPT ON IDLE.RUN on gitbash,cmd prompt etc

#Getting(adding) data to programs
#%r is format string operator used to represent a string using "repr" representation

#==>adding data to a python file(script) Example-1
print('\n#Adding data into a python file example-1')
print('How old are you?',)
age = input() 
print('How tall are you?',)   
height = input()
print('what is your weight?',)    #Notice the comma(,) at the end of each print line.
weight = input()            #This is so,so that print does not end the line with a new line xter and go to next line 

print('So you are %s years old,%scm tall and weigh %s kg' %(age,height,weight))

#OR
age = input('How old are you?')
height = input('How tall are you?')
weight = input('what is your weight?')

print('I am %s years old, i am %scm tall and i am over %s of weight.' %(age, height, weight))


#==>Passing variables in a python file(script)Example-2
#writing scripts that aaccept arguments
from sys import argv   #where 'argv' is argument variable.This variable holds the arguments u pass in ur python script when u run it
script, first, second, third = argv  #This unpacks the 'argv' to get assigned to omly the 4 variables u want to work with rather than holding all arguments

print('The script is called:', script)
print('The first variable is:', first)
print('The second variable is:', second)
print('The third variable is:', third)
#worked on gitbash,cmd prompt etc and u can replace the first,second and third arguments with any 3 arguments of ur choice
#i.e python input.py <fisrt second third> OR <grape banana mango>


#==>Using 'argv' and 'input' together to ask user something specific
#Here we use 'input' slightlt different by having it just print a simple prompt('>')
from sys import argv
script, user_name = argv
prompt = '>'

print('Hi %s, i am the %s script.' %(user_name, script))
print('I will like to ask u some few questions')
print('Do u like me %s?' %user_name)
likes = input(prompt)

print('where do u live %s?' %user_name)
lives = input(prompt)

print('%s, what type of computer do u have?' %user_name)
computer = input(prompt)

print('''
Alright, so u said %r about liking me.
And u live in %r. Far from me.
Also, u have %r computer. Nice choice
'''%(likes,lives,computer))
#worked on gitbash,cmd prompt etc and u can replace the name with any name of ur choice
#i.e python input.py <ben> OR <Guru>
