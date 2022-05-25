import unittest
from isbn import is_valid_isbn

class TestIsbn(unittest.TestCase):
    def test_value(self):
        self.assertTrue(is_valid_isbn("9780316066525"))
        self.assertFalse(is_valid_isbn("0330301824"))
        self.assertTrue(is_valid_isbn("0316066524"))

if __name__ =="__main__":
    unittest.main()