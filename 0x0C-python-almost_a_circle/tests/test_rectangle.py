import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    def test_width_integer_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_width_value_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 2)

    def test_height_integer_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_height_value_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_integer_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "x", 0)

    def test_x_value_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -5, 0)

    def test_y_integer_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "y")

    def test_y_value_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -5)

    def test_str_method(self):
        rectangle = Rectangle(10, 5, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 10/5"
        actual_output = str(rectangle)
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
