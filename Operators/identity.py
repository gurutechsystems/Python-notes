#"Is" and "Is Not" are identity operators Used to check if 2 values are located in thesame part of the memory.
#However, 2 values that are equal does not mean they are identical
a=10
b=20
#c=a
c=10

print(a is not b)
print(a is c)

m="abcd"
print("abc" is m)
print("abcd" == m)