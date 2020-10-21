import unittest
from passlock import User
from passlock import Credentials

class TestPasslock(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("collins", "12345")


    def test_init(self):
        self.assertEqual(self.new_user.username,'collins')
        self.assertEqual(self.new_user.password,'12345')


    def test_save_details(self):
        
        """
        method to test if save details method saves the user information
        """
        self.new_user.save_user_details() 
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
    
        '''
        test to check if it saves many users
        '''
        
        self.new_user.save_user_details()
        test_user = User("John","00000")
        test_user.save_user_details()

        self.assertEqual(len(User.user_list),2)

class TestAccount(unittest.TestCase):
    def setUp(self):

        self.new_account = Credentials("facebook", "collins", "12345")

    def test_init(self):
        self.assertEqual(self.new_account.account,"facebook")
        self.assertEqual(self.new_account.username,"collins")
        self.assertEqual(self.new_account.password,"12345")

    def test_save_account(self):

        """
        test to check if it saves account
        """
        self.new_account.save_credentials() 
        self.assertEqual(len(Credentials.credentials_list),1)

        

if __name__ == '__main__':
    unittest.main()