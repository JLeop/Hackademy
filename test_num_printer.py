import unittest
import production

class Test_nasty_code(unittest.TestCase):
    def test_print_square(self):
        input = list(range(0,10))
        output = [0,1,4,9,16,25,36,49,64,81,100]
        self.assertListEqual(output,nasty_code1.print_square(input))

if __name__ == "__main__":
    unittest.main()
