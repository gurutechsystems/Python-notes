#None data type(used to create null value or no value at all)
a=1
b='obase'
c=False
d=None

print(a)
print(b)
print(c)
print(d)

#verifying the types of data using python keyword "type"
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Use case for data type None
blood_group = None

blood_group = 'B+'

if blood_group is None:
    print('blood_group value not available')
else:
    print('blood_group:' , blood_group)    