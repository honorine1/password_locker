import unittest
from user import User 

class TestUser(unittest.TestCase):
     '''
     Test class that defines test cases for the user class behaviors.
     Args:
        unittest.TestCase: TestCase class that helps in creating test cases
     '''
     def setUp(self):
         '''
         Set up method to run before each test cases.
         '''
         self.new_user = User ('keza joy','kjoy','kezajoymami2020') #create user object


     def tearDown(self):
         '''
         tearDown method that does clean up after each test case has run.
         '''
         User.users_list = []
###############test initialization##############

     def test_init(self):

         '''
         test_init test case to test if the object is initialized properly
         '''

         self.assertEqual(self.new_user.fullname,'keza joy')
         self.assertEqual(self.new_user.username,'kjoy')
         self.assertEqual(self.new_user.password,'kezajoymami2020')

         ##########test saving the new users########3

     def test_save_user(self):

        '''
        test case to test if the user object is saved into users_list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.users_list),1)

        ######test saving of multiple users#####

     def test_save_multiple_users(self):
         '''
         to test if we can save multiple object in our users_list
         '''

         self.new_user.save_user()
         test_user = User ('kami joyce','kajoc','kamijoyce2000')
         test_user.save_user()
         self.assertEqual(len(User.users_list),2)

         #####test deleting user######33

     def test_delete_user(self):
         '''
         to test if  we can remove a user from users_list
         '''
         self.new_user.save_user()
         test_user = User ('kami joyce','kajoc','kamijoyce2000') 
         test_user.save_user()

         self.new_user.delete_user()
         self.assertEqual(len(User.users_list),1)

     

###############find user by username##########


     def test_find_user_by_uname(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        
        test_user = User('kami joyce','kajoc','kamijoyce2000')
        test_user.save_user()

        found_user = User.find_by_username('kajoc')
        self.assertEqual(found_user.fullname , test_user.fullname)


        ####testing the existance of the user in user_list######

     def test_user_exists(self):

        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User('kami joyce','kajoc','kamijoyce2000') 
        test_user.save_user()

        user_exists = User.user_exist('kajoc')
        self.assertTrue(user_exists)

############testing the displayed users###############

     def test_display_all_users(self):
        '''
        method that returns a list of all contacts saved
        '''
        self.assertEqual(User.display_users(),User.users_list)
      



if __name__ == '__main__':
      unittest.main()

     