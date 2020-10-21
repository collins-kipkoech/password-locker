
class User:
    """
    class to create new user
    """
    user_list = []

    def __init__(self,username,password):
        self.username = username
        self.password = password
        """
        defined an init method to initialize the user attributes
        """



    def save_user_details(self):

        """
        method to save user details in the list
        """

        User.user_list.append(self)
        

    def delete_user_details(self):
        '''
        method to delete user details
        '''
        User.user_list.remove(self)

    @classmethod
    def display_user_details(cls):
        return cls.user_list

    @classmethod
    def find_user_username(cls,username):
        """
        method to take in a username and return a matching username
        """
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def find_user_password(cls,password):
        """
        method to take in password and return a matching password
        """

        for user in cls.user_list:
            if user.password == password:
                return user




class Credentials:
    """
    created credentials class
    """

    credentials_list = []

    def __init__(self,account,username,password):
        """
        method to initialize user credential details
        """

        self.account = account
        self.username = username
        self.password = password
       

    def save_credentials(self):
        """
        method to save user credentials to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        method to delete credentials from the credentials list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def show_credentials(cls):
        """
        method to display user credentials in the list
        """
        return cls.credentials_list

    @classmethod
    def find_credential(cls, account):
        """
        Method to find the user account credential
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def display_credentials(cls):
        """
        method to display credentials in the credentials list
        """
        return cls.credentials_list

    @classmethod
    def credential_exist(cls, account):
        """
        Method to check if credential exist
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    # @classmethod
    # def verify_user(cls,username, password):
    #     """
    #     method to verify whether the user exist
    #     """
    #     a_user = ""
    #     for user in User.user_list:
    #         if(user.username == username and user.password == password):
    #                 a_user == user.username
    #     return a_user


    

    

    