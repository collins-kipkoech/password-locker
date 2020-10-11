import unittest
from passlock import User

class TestPasslock(unittest.TestCase):
    def test_init(self):
        self.assertEqual(self.new_user.username,'collins')
        self.assertEqual(self.new_user.password,'12345')


    def test_save_details(self):
        self.assertEqual(self.user)

if __name__ == '__main__':
    unittest.main()