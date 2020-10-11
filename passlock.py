import pyperclip
class User:
    """
    class to create new user
    """
    user_details = []

    def __init__(self,username,password):
        self.username = username
        self.password = password
        """
        defined an init method to initialize the user attributes
        """

new_user = User('collins','12345')
# print(new_user.username)

    def save_details(self):
        User.user_details.append(self)
        """
        method to save user details in the list
        """

    def delete_details(self):
        '''
        method to delete user details
        '''
        User.user_list.remove(self)

    