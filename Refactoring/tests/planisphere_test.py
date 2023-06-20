import unittest 
from Refactoring.planishere import Room
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