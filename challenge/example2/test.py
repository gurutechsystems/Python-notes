#step1=import the modules needed for the test to work
'''
class lexicon():
    def __init__(self, name, description):
        self.name=name
        self.description=description
        self.path={}

    def go(self, direction):
        return self.path.get(direction,None)

    def add_paths(self,paths):
        return self.paths.update(paths)
'''
import unittest
from code import lexicon

class Testlexicon(unittest.TestCase): #creating a class with 3 functions and that inherits from unittest.TestCase
    def setUp(self): #setUp function creates an instance of the 'lexicon'class before each each test method is run for testing
        self.lexicon=lexicon('Test Room', 'testing words')

#step2=create an empty version of the first test case and run it
    def test_init(self):
        self.assertEqual(self.lexicon.name, 'Test Room')
        self.assertEqual(self.lexicon.description, 'testing words')
        self.assertEqual(self.lexicon.paths, {})

    def test_go(self):
        self.assertIsNone(self.lexicon.go('north')) 

        paths={'north':'north room', 'south':'south room'}
        self.lexicon.add_paths(paths)

        self.assertEqual(self.lexicon.go('north'), 'north room')
        self.assertEqual(self.lexicon.go('south'), 'south room')

    def test_add_paths(self):
        self.assertEqual(self.lexicon.paths,{})

        paths={'east':'east room', 'west':'west room'}
        self.lexicon.add_paths(paths)

        self.assertEqual(self.lexicon.paths, paths)       


if __name__=="__main__":
    unittest.main()    