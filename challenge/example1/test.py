#Challenge: write a function called "add" that makes 2 arguments and returns their sum.
#*we start by writting a failing test of the "add" function
print('\n#Testing the add function')
import unittest
from code import Add

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.add=Add()

    def test_add(self):
        self.assertEqual(self.add.add(2,2), 4)

if __name__=='__main__':
    unittest.main()  

'''      
#Challenge: write a function called "add" that makes 2 arguments and returns their sum.
#Creating code to make the test in test.py work
class Add():
    def add(self, a, b): #"a n b" are the arguments
        return a+b
'''        