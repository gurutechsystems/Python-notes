'''
+  = addition
-  = subtraction
/  = float division i.e display rational numbers
// = floor divsion 1.e does not display rational numbers
*  = multiplication
** = exponent i.e raised to the power e.g print(10 ** 3) wc gives 1000
%  = modulo(remainder of the division)
>  = greater than
>= = greater than equal to
<  = less than
<= = less than equal to
'''
#==>INCREMENT OPERATIONS
#Example Arithmetical Operations
print('\n#Total number of chicken')
print('My total chicken is?')
print('Hens:', 10+20/2) #10+(20/2)
print('Roosters:', 100-20/4*2) #100-(20/4(*2)

print('\n#Total number of eggs')
print(3+2+1-5+4%2-1/4+6)

#True or False
print('\n#Is it True or False')
print(3+2<5-7)
print('is it greater than?', 5>-2)
print('is it greater or equal?', 5>=-2)
print('is it less than?', 5<-2)
print('is it less than or equal?', 5<=-2)

#What is
print('\n#what is')
print('what is 3+2?', 3+2)
print('what is 5-7?', 5-7)

#==>AUGMENTED OPERATIONS
print('/n# Increment operation')
x=10
x=x+3
print(x)
#
print('/n#Augmented operation')
x=10
x+=3
print(x)

#operations using the round() build-in function
print('/n#Rounding up floats')
x=2.8
print(round(x))

#operations using abs() built-in function.abs=absolute
#this always returns a positive value even if the value is negative
print('/n#abs function')
x=2.9
print(abs(-2.9))