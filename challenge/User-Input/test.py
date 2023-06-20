import unittest
from lexicon import lexicon

class Testlexicon(unittest.TestCase):
    def setUp(self):
        lexicon.scan=lexicon
        
    def test_direction(self):
        self.assertEqual(lexicon.scan('north'),[('direction','north')])
        result=lexicon.scan('north south east')
        self.assertEqual(result,[('direction','north'),('direction','south'),('direction','east')])

if __name__=='__main__':
    unittest.main()
