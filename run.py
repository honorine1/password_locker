#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random

#########creating  create_user() 
def create_user(fullname,username,password):
    '''
    Function to create a new user acc
    '''
    new_user = User(fullname,username,password)
    return new_user
#######3creating save_users() that is calling the save_user() from User class

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

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
  
def create_credential(acc_name,acc_username,acc_password):
    '''
    Function to create a new user acc
    '''
    new_credential= Credential(acc_name,acc_username,acc_password)
    return new_credential

   

def save_credentials(credential):
    '''
    Function to save user
    '''
    credential.save_credential()
        #########find_credential() that is calling the find_by_name() from Credential

def find_credential(acc_name):
   
    '''
    Function that finds a user by username and returns the user
    '''
    return Credential.find_by_name(acc_name)

        #########display_users() that is calling the display_user() from User

def display_credentialss():
    '''
    Function that returns all the saved users
    '''
    return Credential.display_credentials()

    ##########delete credential########

   

def del_credential(credential):
    '''
    Function to save contact
    '''
    credential.delete_credential()
    ######check existing account#############

def check_existing_credentials(acc_name):
    '''
    Function that check if a usaer acc exists using username and return a Boolean
    '''
    return Credential.credential_exist(acc_name)

    ##########33verifying username before creating new account######

# def verify_user(username,password):
# 	'''
# 	Function that verifies the existance of the user before creating credentials
# 	'''
# 	checking_user = Credential.auth_users(username,password)
# 	return checking_user






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


        elif short_code =='log':
            print('Please Fill in the required details')
            print('-'*50)
            print('\n')
            # print('Enter your full Name')
            # fullname=input()

            print('To login Enter your user Name')
            username1=input()
            if username1 != username:
                continue
            else:

                password1=str(input('Enter your password:'))
                if password1 != password:
                    continue
                else:
            
                        while True:
                            print('-'*50)
                            print('To continue,choose one short code : \n cc-Create a Credential \n dc-Display Credentials \n delete Credential \n ex-Exit')
                            # short_code = input('Enter a choice: ').lower()
                            short_code = input().lower()
                            # print('-'*50)
                            if short_code == 'ex':
                                print('\n')
                                print(f'Good bye {username}')
                                break

                            
                            elif short_code == 'cc':

                                print('Enter your site name')
                                acc_name = input()
                                print('-'*10)

                                print('Your site User name ....')
                                acc_username = input()



                                print('choose  gn -to generate password or ty -to type your own')
                                shortCode = input().lower()
                                if shortCode =='gn':
                                    passwordlen = 8
                                    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?0123456789"
                                    pasword ="".join (random.sample(s,passwordlen))
                                   
                                    print(f'your password:{pasword}')
                                
                                else :
                                    print('enter your password.....')
                                    pasword = input()
                                
                                    

                                save_credentials(create_credential( acc_name , acc_username , pasword ))##create and save new user acc
                                print('\n')
                                print(f'details for {acc_name} have been saved')
                                print('\n')

                            elif short_code == 'dc':
                                if display_credentialss():
                                    
                                    print('Here is a list of all of your site ')
                                    print('\n')

                                    for credential in display_credentialss():
                                        print(f'{credential.acc_name} {credential.acc_username} ..... {credential.acc_password}')
                                        print('\n')

                            elif short_code == 'del':

                   
                                 print('enter the account name  you want to delete')

                                 search_acc_name = input()
                                 if check_existing_credentials(search_acc_name):
                                    search_credential = find_credential(search_acc_name)
                                    print(f'{search_credential.acc_name} {search_credential.acc_username}')
                                    print('-'*20)
                                    search_credential.delete_credential()
                                    print(f'{search_credential.acc_name} successfully deleted')

                                 else:
                                    print('That credential does not exist')

                            else:
                                print('no credential saved yet')
                                print('\n')

        elif short_code == 'du':
            if display_userss():
                
                print('Here is a list of all of your users ')
                print('\n')

                for user in display_userss():
                    print(f'{user.fullname} {user.username} ..... {user.password}')
                    print('\n')

            else:
                print('no user not saved yet')
                print('\n')

        elif short_code == 'fu':
            print('Enter user name you want to search for')

            search_user = input()
            if check_existing_users(search_user):

                search_user = find_user(search_user)
                print(f'{search_user.username} {search_user.password}')
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

        


        else:
            print('User does not exist please create an account first')

if __name__ == '__main__':

    main()
