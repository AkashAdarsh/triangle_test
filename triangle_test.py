import unittest
import triangle
if __name__ == "__main__":
    unittest.main()
class CalcTest(unittest.TestCase):
    #scalene
    def test_triangle_type_scalene(self):
        self.assertEqual(triangle.triangle_type(2,3,4), "its scalene")
    #isosceles
    def test_triangle_type_isosceles(self):
        self.assertEqual(triangle.triangle_type(3,3,2), "its isosceles")
    #equilateral
    def test_triangle_type_equilateral(self):
        self.assertEqual(triangle.triangle_type(3,3,3), "its equilateral")
    #error for negative sides
    def test_triangle_type_negative_sides(self):
        self.assertEqual(triangle.triangle_type(-3,7,2), "its an error")
        self.assertEqual(triangle.triangle_type(9,-5,4), "its an error")
        self.assertEqual(triangle.triangle_type(8,6,-3), "its an error")
    #error for mismatching the condition for building triangle
    def test_triangle_type_wrong_condiion(self):
        self.assertEqual(triangle.triangle_type(15,4,1), "its an error")
        self.assertEqual(triangle.triangle_type(2,13,3), "its an error")
        self.assertEqual(triangle.triangle_type(3,8,19), "its an error")
