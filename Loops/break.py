#To exit a continous loop when conditions are met, we use the keyword break.
#Break is used to bring control out of the loop when conditions are met

#Using the break statement example 1(for loop)
print('\n# use Break to exit a for loop')
s='obase use an email that ends with @ gmail.com'

for letter in s:
    print(letter)
    #break the loop as soon as it sees '@'
    if letter=='@':
        break
print('out of for loop')

#Using the break statement example 2(while loop)
print('\n# use Break to exit a while loop')
i=0

while True:
       print(s[i])
       #break the loop as soon as it sees '@
       if s[i]=='@':
            break
    
       i+=1

print('out of while loop')       
