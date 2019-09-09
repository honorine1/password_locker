class User:
    '''
    a class that generates new user instance
    '''
    users_list =[] 
    def __init__(self,fullname,username,password):
        '''
        this is a method is showing the properties of the above method
        '''
        self.fullname = fullname
        self.username = username
        self.password = password

        

    ############defining the save_user method to pass the test#########

    def save_user(self):
        '''
        method that save the user object into users_list
        '''

        User.users_list.append(self)

############defining the delete_user method to pass the test#########

    def delete_user(self):
        '''
        method that delete user object from users_list
        '''
        User.users_list.remove(self)

        ############## defining the find_user method to pass the test############
    @classmethod
    def find_by_username(cls,username):
        '''
        method that takes username and return the users_list item containing that username
        '''
        
        for user in cls.users_list:
            if user.username == username:
                return user

                ########### defining the user_exists() to pass the test########

    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the users list.
        Args:
            username: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.users_list:
            if user.username == username:
                    return True

        return False


        #########3defining display_user()######

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.users_list

        #######for checking the existance of users#########3

    @classmethod
    def auth_users(cls, username, password):
        '''
        method that check if username and password are correct
        '''

        # user = ''
        for  User in cls.users_list:
            if(User.username == username and User.password == password):
                User = User.username
                return User
        return 0
       