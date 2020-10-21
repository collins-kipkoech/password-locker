# !/usr/bin/env python3.6
from passlock import User, Credentials

def create_user(username,password):
    '''
    function to create new user
    '''
    new_user = User(username,password)
    return new_user

def save_user_details(user):
    '''
    Function to save new user
    '''
    user.save_user_details()

def display_user_details():
    """
    Function to show existing user details
    """
    return User.display_user_details()

def create_new_credential(account,username,password):
    """
    function to create new user credentials
    """
    new_credential = Credentials(account,username,password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()

def find_user(username):
    return User.find_user_username(username)

def find_password(password):
    return User.find_user_password(password)

def passlocker():
    print("Welcome to passlock app")

    while True:
        print("please select option: su - SignUp  or  lg - Login")
        user_choice = input().lower()

        if user_choice == "su":
            print("Create an account")
          

            print("Enter Username:")
            username = input()

            print("Enter password")
            password = input()

            
            save_user_details(create_user(username,password)) 
            print('\n')
            print("Your account has been created. Please proceed to login")
            


        elif user_choice == "lg":
            print("Enter your Username:")
            username = input()

            print("Enter your password:")
            password = input()

            if find_user(username) and find_password(password):
                print('\n')
                print("please choose any of the options below:")
                print("nw - Add New Account, da - Display credentials, vw -View credentials, dlt - Delete credentials")

                account_choice = input().lower()

                if account_choice == "nw":
                    print("Enter Account Name:")
                    account = input()

                    print("Enter Account Username:")
                    username = input()

                    print("Enter Account Password:") 
                    password = input()

                    save_credentials(create_new_credential(account,username,password)) 
                    print(f"Account Name:{account}, Username:{username}, Account Password:{password}")


        #         elif account_choice == "da":
        #             if display_account_credentials():
        #                 print("Here is a list of all your accounts: ")
        #                 print('\n')

        #                 for account in display_account_credentials():
        #                     print(f"Account Name:{account.account_name}")

        #             else:
        #                 print("invalid choice")


        #         elif account_choice == "vw":
        #             print("Enter an Account Name:")
        #             account_choiceName = input()

        #             if display_account_credentials():
        #                 account_choiceName = find_account_credentials(account_choiceName)
        #                 print(f"Account Username:{account_choiceName.account_userName}   Password:{account_choiceName.account_password}")

        #             else:
        #                 print(f"{account_choiceName} does not exist")



        #         elif account_choice == "dlt":
        #             print("Enter Account Name:")
        #             delete_acc = input()

        #             if delete_account(delete_acc):
        #                 return delete_account(delete_acc)

        #             else:
        #                 print(f"{delete_acc} does not exist")


        #     else:
        #         print("Incorrect username or password.Please try again.")
        #         print('\n')


        # else:
        #     print("Incorrect Option.Please choose from the ones listed")
        #     print('\n')



if __name__ == '__main__':
    passlocker()