import unittest
from main import Game 

class TestGame(unittest.TestCase):
    def test_grid(self):
        g = Game(3,3)
        self.assertEqual(g.get_grid(), [['_', '_', '_'],
                                          ['_', '_', '_'],
                                          ['_', '_', '_']])
        g.declare_move(0, 0)
        self.assertEqual(g.get_grid(), [['X', '_', '_'],
                                          ['_', '_', '_'],
                                          ['_', '_', '_']])
        
    def test_diagonal_check(self):
        g = Game(3, 3)

        self.assertTrue(g.check())
        g.declare_move(0, 0)
        g.declare_move(0, 1)
        g.declare_move(1, 1)
        g.declare_move(0,2)
        g.declare_move(2, 2)
        self.assertFalse(g.check())

unittest.main()