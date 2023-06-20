#2D list is a list where each item in the list is another 
items =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(items[0] [1]) #this will return the 2nd item in the 1st index value 0

#changing item values in a string inside another string
items[0][1]=20
print(items[0][1])

#using nested loop to iterate over a items in a list within a list
for row in items:
    for item in row:
        print(item)