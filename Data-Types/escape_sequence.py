#Escape sequence make a string to go across multiple lines in a python file.
'''
\n = linefeed(next line)
\t = horizotal tab
\v = vertical tab
\\ = backslash(\)
\' = single-qoute(')
\" = double-quote(")
\a = bell
\b = backspace
Etc
'''

#Example-1
print('\n#Escape sequence example-1')
name = "\tI'm Ngembane Benbella" #\t will start the first line with a paragraph
profession = "I'm a DevOps Engineer\nAnd also a Cloud Engineer" #\n will split the string into 2 lines
orientation = "I'm very good\\at what\\i do" #\\ will print just 1 backlash 
Hobbies = '''
I'll do a list:
\t*Watching and Playing football
\t*Studying new technologies
\t*Going to the gym\n\t*Taking a nap
'''

print(name)
print(profession)
print(orientation)
print(Hobbies)

#Example-2
print('\n#Escape sequence example-2')
print('you\'d need to know \'bout escape with \\ that do \nnewlines and \t tabs.')#(\') help use use qoutes between words
poem='''
\tThe lovely world 
with logic so firmly planted cannot discern \nthe needs of love 
nor comprehend passion from intuition
and requires an explanation
\twhere there is none
'''
print('......................')
print(poem)
print('......................')

'''
while True:
    for i in ['/','-','|','\\','|']:
        print('%s\r' %i)
'''        