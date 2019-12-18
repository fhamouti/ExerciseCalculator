import unittest
import app


class TestApp(unittest.TestCase):

    #Test add function
    def test_add(self):
        self.assertEqual(app.add(10, 5), 15)
        self.assertEqual(app.add(-4, -2), -6)
        self.assertEqual(app.add(-1, 1), 0)

    #Test subtract function
    def test_subtract(self):
        self.assertEqual(app.subtract(20, 4), 16)
        self.assertEqual(app.subtract(-1, 1), -2)
        self.assertEqual(app.subtract(-1, 0), -1)

    #Test multiply function
    def test_multiply(self):
        self.assertEqual(app.multiply(10, 10), 100)
        self.assertEqual(app.multiply(-4, 3), -12)
        self.assertEqual(app.multiply(0, 20), 0)

    #Test divide function
    def test_divide(self):
        self.assertEqual(app.divide(4, 2), 2)
        self.assertEqual(app.divide(1, 2), 0.5)
        self.assertEqual(app.divide(-2, -2), 1)

        with self.assertRaises(ValueError):
            app.divide(2, 0)


if __name__ == '__main__':
    unittest.main()