#%s is format string operator used to represent string
#%d is format string operator used to represent int(integer)
#%r is format string operator used to represent a string using "repr" representation

formatter = '%r %r %r %r'

print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))
print('I am Ngembane.', 'a DevOps Engineer by proffession.', 'i am 32 years of age.', 'and i am a father of 2 beautiful girls')