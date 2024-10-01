import unittest
import logging
from main import Game 

class TestGame(unittest.TestCase):

    def test_display_grid(self):
        g = Game(3,3)
        g.display_grid
        with self.assertLogs('foo', level="DEBUG") as cm:
            g.display_grid()
        
        self.assertEqual(cm.output, ['C 0 1 2',
                                     '0 _ _ _',
                                     '1 _ _ _',
                                     '2 _ _ _'])


unittest.main()