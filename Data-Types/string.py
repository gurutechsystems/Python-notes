#string data type(used when dealing with words,characters,names,sentences etc)

#String variables example-1
print('\n#string variable example-1')
print('hello world')
print('hi Obase')
object='car'
print(object)
fruit_type='mango'
print(fruit_type)

c='' #This is an empty string. Meaning 'c' stores the value of a string containing no character
print(c)
print(len(c))
print(len(fruit_type))
#verifying the type of data using python keyword "type"
print(type('hello world'))
print(type('hi Obase'))
print(type(object))
print(type(fruit_type))
print(type(c))
print(type(''))

#string variableexample-2
print('\n#String variable exapmle-2 using format string')
x = 'there are %d types of people in this world.' %10
binary = 'binary'
do_not = 'do_not'
y = 'those who know %s and those who %s.' %(binary,do_not)

print(x)
print(y)

print('i said: %r.' %x) #%r is format string operator used to represent a string using "repr" representation
print("i also said: '%s'." %y)

#String variable example-3
print('\n#String variable example-3')
hilarious =  False
joke_evaluation = "Isn't that joke funny? %r"
print(joke_evaluation % hilarious)

#string variable example-4
print('\n#String variable example-4')
w = 'this is the left side of '
x = 'a string with a right side.'
print(w+x)

print('.'*20)

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'
print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

#String variable example-5
print('\n#String variable example-5')
days = 'Mon Tue Wed Thur Fri Sat Sun'
#OR days = '\nMon \nTue \nWed \nThur \nFri \nSat \nSun'(to have them in seperate lines)
months = '\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec'
#OR months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'

print('Here are the days of the week;', days)
print('Here are the months of the year;', months)
print ('''
With this three qoutes, we can write as many lines of code as possible in a single python script
My name is Ngembane
i am a devops engineer
i am 32 years of age
i am a husband and a parent
God over everything   
''')