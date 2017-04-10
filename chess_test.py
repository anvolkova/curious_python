import unittest
import chess


class TestChess(unittest.TestCase):

    def test_rank(self):
        expected = "same rank"
        self.assertEqual(chess.check_queen_and_king("a1", "c1"), expected)
        self.assertEqual(chess.check_queen_and_king("h3", "b3"), expected)

    def test_file(self):
        expected = "same file"
        self.assertEqual(chess.check_queen_and_king("a1", "a2"), expected)
        self.assertEqual(chess.check_queen_and_king("h3", "h8"), expected)

    def test_diagonal(self):
        expected = "same diagonal"
        self.assertEqual(chess.check_queen_and_king("a1", "c3"), expected)
        self.assertEqual(chess.check_queen_and_king("h3", "f1"), expected)

    def test_safe(self):
        expected = "king is safe"
        self.assertEqual(chess.check_queen_and_king("a1", "c4"), expected)
        self.assertEqual(chess.check_queen_and_king("h3", "f2"), expected)

if __name__ == '__main__':
    unittest.main()