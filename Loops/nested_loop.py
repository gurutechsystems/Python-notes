#This is a loop inside another loop i.e a loop inside the body of an outer loop
print('\n# nested loop example 1')
#outer loop
for i in range(0,6):
     #Nested loop
     #To iterate from 1 to 5
     for j in range(0,5):
          print('*', end='') #print multiplication. Default end \n replaced with a space here to stay at same line
     print()  #use debugger to explain

print('\n# nested loop example 2')     
#outer loop
for i in range(1,11):
     #Nested loop
     #To iterate from 1 to 5
     for j in range(1,11):
          print("*", end="") #print multiplication. Default end \n replaced with a space here to stay at same line
          print() #use debugger to explain

#Example-3
print('\n# nested loop example 3')
for x in range(4): #outer loop(here in the first iteration x=0)
     for y in range(3):  #inner loop(here in the first iteration y=0)
          print(f'({x}, {y})')

#Example-4
print('\n# nested loop example 4')
numbers=[5,2,5,2,2]

for x in numbers:
     print('X' * x)

#OR(using nested loop)
print('\n# nested loop example 5')
numbers=[2,2,2,2,7]

for x in numbers:
     output = '' 
     for y in range(x):
          output  = output + 'x'  # output += 'x'
     print(output)         