#Python code for a python class 'calculator' to perform arithmetic operations
#EXAMPLE-1
'''
print('\n#Arithmetic operations code')
class calculator():
    def add(self, a, b):
        return a+b
    def subtract(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def divide(self, a, b):
        if b==0:
          raise ValueError('cannot divide by 0')
        return a/b
       
print('\n#Running unit testing on codes')
import unittest

class Testcalculator(unittest.TestCase): #creating a class that inherits from unittest.TestCase
    def setUp(self): #setup function creates an instance of the 'calculator'class to be used for testing 
        self.calc=calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-2,3),1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(2,5),-3)

    def test_muliply(self):
        self.assertEqual(self.calc.multiply(2,3),6)
        self.assertEqual(self.calc.multiply(-2, 3),-6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6,3),2)
        self.assertEqual(self.calc.divide(-6,3),-2)

        with self.assertRaises(ValueError):
            self.calc.divide(6,0)

if __name__=='__main__':
    unittest.main()                      
'''
#EXAMPLE-2
'''
-The below code creates a class "Room" with 3 methods(functions) i.e __init__,go and add_path
-The __init__ function of the class creates the name,description and paths attributes of the Room
-The 'go' function takes a direction parameter and return the values of the corresponding directions in "paths" of the Room and if the direction is not in the "paths" attribute,it returns None
-The "add_paths" function takes the paths parameter and updates the "paths" attribute of the Room with the given paths
'''
print('\n#Automated code Testing')
class Room():
    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.paths={}

    def go(self,direction):
        return self.paths.get(direction,None) 
     
    def add_paths(self,paths):
        return self.paths.update(paths)

print('\n#UnitTesting')
import unittest 

class TestRoom(unittest.TestCase): #creating a class that inherits from unittest.TestCase with 2 functions(methods)
    def setUp(self): #setUp function creates an instance of the 'Room'class to be used for testing
        self.room=Room('test room', 'a room for testing')

    def test_go(self):  #'test_go' function tests the 'go' method of the Room class
        self.assertIsNone(self.room.go('north'))
        self.assertIsNone(self.room.go('south'))
        self.assertIsNone(self.room.go('east'))
        self.assertIsNone(self.room.go('west'))

        self.room.add_paths({'north':'test room north', 'south':'test room south'})
        self.assertEqual(self.room.go('north'), 'test room north')
        self.assertEqual(self.room.go('south'), 'test room south')
        self.assertIsNone(self.room.go('east'))
        self.assertIsNone(self.room.go('west'))
    
    def test_add_paths(self):
        self.assertEqual(len(self.room.paths),0)
        self.room.add_paths({'north':'test room north', 'south':'test room south'})
        self.assertEqual(len(self.room.paths),2)
        self.assertIn('north', self.room.paths)
        self.assertIn('south', self.room.paths)
        self.assertEqual(self.room.paths['north'], 'test room north')
        self.assertEqual(self.room.paths['south'], 'test room south')

if __name__=='__main__':
    unittest.main()        