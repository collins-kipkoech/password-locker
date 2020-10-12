import unittest
from passlock import User
from passlock import Credentials

class TestPasslock(unittest.TestCase):
    def test_init(self):
        self.assertEqual(self.new_user.username,'collins')
        self.assertEqual(self.new_user.password,'12345')


    def test_save_details(self):
        self.assertEqual(self.user)
        """
        method to test if save details method saves the user information
        """

if __name__ == '__main__':
    unittest.main()