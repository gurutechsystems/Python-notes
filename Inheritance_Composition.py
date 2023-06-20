#==>INHERITANCE[This is the concept that one class can inherit the traits(characteristics/features) of another class(parent class)]
class Animal:
    def walk(self):
        print('walk')

class Dog(Animal):
    def bark(self):
        print('bark')

class Cat(Animal):
    pass

dog1=Dog() 
dog1.bark() #OR dog1.walk()

cat1=Cat()
 
#There are 3 ways in which the parent and child classes interact

#1==>Implicit module(actions on child imply actions on parent)
print('\n#Implicit inheritance')
class parent(object):
    def implicit(self):
        print('this is an implicit inheritance')

class child(parent):
    pass #This tells python u want an empty block i.e nothing to define in it.Instead it should inherit the features from parent

dad=parent()
son=child()

dad.implicit()
son.implicit()

#2==>Override inheritance(actions on child overide actions on parent)
print('\n#Override inheritance')
class parent(object):
    def override(self):
        print('this ia parent class')

class child(parent):
    def override(self):
        print('this is a child class')

dad=parent()
son=child()

dad.override()   
son.override() #Child.override messages because 'son' is an instance of 'Child' and Child overrides that function by defi ning its own version. 

#3==>Alter Before or After Inheritance(actions on child alter the action on the parent)
print('\n#Alter inheritance')
class parent(object):
    def alter(self):
        print('This is the parent class')

class child(parent):
    def alter(self):
        print('this is the before child class')
        super(child,self).alter()  #'super()' will alter the parent version
        print('this is the after child class')

dad=parent()
son=child()

dad.alter()
son.alter()

#4==>Combining all 3 inheritance types
print('\n#All 3 combined')
class parent(object):
    def override(self):
        print('parent override')
    def implicit(self):
        print('parent implicit')
    def alter(self):
        print('parent alter')

class child(parent):
    def overrride(self):
        print('child override')
    def implicit(self):
        print('child implicit')
    def alter(self):
        print('child before alter')
        super(child,self).alter()   
        print('child after alter') 

dad=parent()
son=child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.alter()
son.alter()

#==>MULTIPLE INHERITANCE(this is when u define a class that inherits from 2 or more classes)
#Example
class guru(child,parent): #make class 'guru' that inherit from parent and child classes at same time
    pass
'''
#==>The Reason for super() function['super()' will alter type of actions taken in a class]
#The most common use of super() is in _init_ functions in base classes[_init_()].
#With _init_(), u take actions in the child and complete the initialization in the parent
print('\n#Using super() with _init_()')
class child(parent):
    def __init__(self, guru):
        self.guru=guru
        super(child,self).__init__() #Here we are setting some variables in _init_() b4 having 'parent class' initialize with the parent._init_ in the child class
'''
#==>COMPOSITION(This is the concept that a class be composed of other classes as parts)
#Here,we are no using 'Parent' and 'Child' cuz its not parent-child 'Is-a' relationship
#It is a 'Has-a' relationship where the child 'Has-a' other classes it uses to get work done
print('\n#Composition example')
class other(object):
    def implicit(self):
        print('implicit other')
    def override(self):
        print('override other')
    def alter(self):
        print('alter other') 

class child(object):
    def __init__(self):
        self.other=other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print('override child')
    def alter(self):
        print('before alter other')
        self.other.alter() 
        print('after alter other')

    son=child()

    son.implicit()
    son.override()
    son.alter()
'''
#WHEN TO USE INHERITANCE OR COMPOSITION
1. Avoid multiple inheritance at all costs, as it’s too complex to be useful reliably.
2. Use composition to package up code into modules that are used in many different unrelated places and situations.
3. Use inheritance only when there are clearly related reusable pieces of code that fit under
a single common concept or if you have to because of something you’re using
'''