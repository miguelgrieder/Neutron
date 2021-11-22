
import unittest

from coordinates import Point
  
class PointTest(unittest.TestCase):
  
    def test_init(self):        

        p = Point(10, 20)

        self.assertEqual(p.x, 10)
        self.assertEqual(p.y, 20)

    def test_directions(self):
        original = Point(100, 50)

        offset = 10

        to_up = original.to_up(offset)
        to_down = original.to_down(offset)
        to_left = original.to_left(offset)
        to_right = original.to_right(offset)

        self.assertEqual(original.x, 100)
        self.assertEqual(original.y, 50)

        self.assertEqual(to_up.x, original.x)
        self.assertEqual(to_up.y, original.y - offset)

        self.assertEqual(to_down.x, original.x)
        self.assertEqual(to_down.y, original.y + offset)

        self.assertEqual(to_left.x, original.x - offset)
        self.assertEqual(to_left.y, original.y)

        self.assertEqual(to_right.x, original.x + offset)
        self.assertEqual(to_right.y, original.y)


    

  
if __name__ == '__main__':
    unittest.main()