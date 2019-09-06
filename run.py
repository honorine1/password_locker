#!/usr/bin/env python3.6
from user import User
from credential import Credential

#########creating  create_user() 
def create_user(fullname,username,password):
    '''
    Function to create a new user acc
    '''
    new_user = User(fullname,username,password)
    return new_user
#######3creating save_users() that is calling the save_user() from User class

def save_users(contact):
    '''
    Function to save user
    '''
    contact.save_user()

    #########del_user() that is calling the delete_user() from User

def del_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

    #########find_user() that is calling the find_by_username() from User

def find_user(username):
   
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

    #########display_users() that is calling the display_user() from User

def display_userss():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

    ######check existing account#############

def check_existing_users(username):
    '''
    Function that check if a usaer acc exists using username and return a Boolean
    '''
    return User.user_exist(username)
    ##########33verifying username before creating new account######

def verify_user(username,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(fullname,password)
	return checking_user






def main():

    print('Most Welcome to the password_locker application!,What is your name?')
    fullname = input()

    print(f'Hello {fullname} ,what do you want to do?') 
    print('\n')


    while True:
        print('Please enter one of these short code to proceed: \n ex - for exiting \n cua -for creating new user acc if you didnt signup before \n log -to login if you already have an account \n du -display the users acc list \n fu -for finding user account')
    
        short_code = input().lower()
        if short_code == 'ex':
            print('Thanks for coming,Byee!!')
            break
        elif short_code == 'cua':

            print('Create New User')
            print('-'*10)

            print('Full name ....')
            fullname = input()
            
            print('User name ....')
            username = input()

            print('password ....')
            password = input()


            save_users(create_user(fullname,username,password))##create and save new user
            print('\n')
            print(f'log in details for {username} have been saved')
            print('\n')
            
            
            print("Please exit the application to log in to see your credentials")
            print('\n')

        elif short_code == 'du':
            if display_userss():
                
                print('Here is a list of all of your accounts ')
                print('\n')

                for user in display_userss():
                    print(f'{user.fullname} {user.username} ..... {user.password}')
                    print('\n')

            else:
                print('no account saved yet')
                print('\n')

        elif short_code == 'fu':
            print('Enter username you want to search for')

            search_user = input()
            if check_existing_users(search_user):

                search_user = find_user(search_user)
                print(f'{search_user.fullname} {search_user.password}')
                print('-'*20)
                print('\n')

                print(f'fullname.......{search_user.fullname}')
                print(f'username.......{search_user.username}')
                print(f'password........{search_user.password}')
                print('\n')
                print('\n')

            else:

                print('That user account does not exist')
                print('\n')
                print('\n')

        elif short_code =='log':
            print('Please Fill in the required details')
            print('-'*50)
            print('\n')
            # print('Enter your full Name')
            # fullname=input()

            print('To login Enter your user Name')
            username=input()
            print('Enter your password')
            password=str(input())
            user_exists = verify_user(username,password)
            if user_exists == 'username':
                print(' ')
                print(f'Welcome {username} .Please choose an option to continue')
                print(' ')
                while True:
                    print('-'*50)
                    print('choose one short code : \n cc-Create a Credential \n dc-Display Credentials  \ gen -generate password \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)



        else:
            print('User does not exist please create an account first')

    #    print('Please enter one of these short code to proceed: ex - for exiting , cua -for creating new user acc if you didnt signup before, del -deleting user_acc , log -to login if you already have an account , fu -for finding user , du -display the users acc list')
          


if __name__ == '__main__':

    main()
