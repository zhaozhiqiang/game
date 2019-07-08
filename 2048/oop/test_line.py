import unittest
from line import Line

MAX_LINE_INDEX = 3

class TestLine(unittest.TestCase):
    def test_line_to_string(self):
        line_1 = Line([0, 0, 0, 0])
        line_1_string = '·    ·    ·    ·    '
        self.assertEqual(line_1_string, line_1.line_to_string())

        line_2 = Line([4, 0, 0, 4])
        line_2_string = '4    ·    ·    4    '
        self.assertEqual(line_2_string, line_2.line_to_string())

        line_3 = Line([8, 16, 0, 128])
        line_3_string = '8    16   ·    128  '
        self.assertEqual(line_3_string, line_3.line_to_string())

        line_4 = Line([2048, 16, 0, 2048])
        line_4_string = '2048 16   ·    2048 '
        self.assertEqual(line_4_string, line_4.line_to_string())

    def test_next_not_zero(self):
        line_1 = Line([0, 2, 0, 2])
        self.assertEqual(1, line_1.next_not_zero(0))
        self.assertEqual(3, line_1.next_not_zero(1))
        self.assertEqual(-1, line_1.next_not_zero(3))

        line_2 = Line([0, 0, 0, 2])
        self.assertEqual(3, line_2.next_not_zero(0))
        self.assertEqual(3, line_2.next_not_zero(1))
        self.assertEqual(3, line_2.next_not_zero(2))
        self.assertEqual(-1, line_2.next_not_zero(3))

        line_3 = Line([4, 0, 0, 0])
        self.assertEqual(-1, line_3.next_not_zero(0))
        self.assertEqual(-1, line_3.next_not_zero(1))
        self.assertEqual(-1, line_3.next_not_zero(2))
        self.assertEqual(-1, line_3.next_not_zero(3))

    def test_plus(self):
        line_1 = Line([0, 2, 0, 2])
        self.assertEqual([0, 4, 0, 0], line_1.plus())

        line_2 = Line([0, 2, 2, 2])
        self.assertEqual([0, 4, 0, 2], line_2.plus())

        line_3 = Line([2, 2, 2, 2])
        self.assertEqual([4, 0, 4, 0], line_3.plus())

        line_4 = Line([2, 2, 64, 128])
        self.assertEqual([4, 0, 64, 128], line_4.plus())

    def test_move(self):
        line_1 = Line([0, 2, 0, 2])
        self.assertEqual([2, 2, 0, 0], line_1.move())

        line_2 = Line([0, 2, 2, 2])
        self.assertEqual([2, 2, 2, 0], line_2.move())

        line_3 = Line([2, 2, 2, 2])
        self.assertEqual([2, 2, 2, 2], line_3.move())

        line_4 = Line([0, 0, 0, 0])
        self.assertEqual([0, 0, 0, 0], line_4.move())

        line_5 = Line([2, 0, 0, 0])
        self.assertEqual([2, 0, 0, 0], line_5.move())

    def test_full(self):
        line_1 = Line([2, 2, 0, 2])
        self.assertEqual(False, line_1.full())

        line_2 = Line([2, 2, 2, 2])
        self.assertEqual(True, line_2.full())

    def test_find_equal(self):
        line_1 = Line([2, 2, 4, 8])
        self.assertEqual(True, line_1.find_equal())

        line_2 = Line([4, 2, 2, 8])
        self.assertEqual(True, line_2.find_equal())

        line_3 = Line([4, 8, 2, 2])
        self.assertEqual(True, line_3.find_equal())

        line_4 = Line([2, 4, 8, 2])
        self.assertEqual(False, line_4.find_equal())



if __name__ == '__main__':
    unittest.main()
