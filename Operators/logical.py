#Used to combine conditional statements.AND,OR, and NOT are logical operators. 
#Reseult is either True or False depending on the condition
a=True
b=False

#print a AND b is False
print(a and b)

#print a OR b is True
print(a or b)

#print NOT a is False
print(not a)

#Example 2
has_high_income= False #True
has_good_credit= True #False
has_criminal_record= False #True

if has_high_income and has_good_credit:
    print('eligible for loan')
elif has_high_income or has_good_credit:
    print('still eligible for loan')
elif has_high_income and not has_criminal_record:
    print('eligible for loan')   
else:
    print('Not eligible for loan')
