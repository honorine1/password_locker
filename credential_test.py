import unittest
from credential import Credential 


class TestCredential(unittest.TestCase):
     '''
     Test class that defines test cases for the credential class behaviors.
     Args:
        unittest.TestCase: TestCase class that helps in creating test cases
     '''
     def setUp(self):
         '''
         Set up method to run before each test cases.
         '''
         self.new_credential = Credential ('facebook','mimy','111') #create user object


     def tearDown(self):
         '''
         tearDown method that does clean up after each test case has run.
         '''
         Credential.cred_list = []

         ################################3

     def test_init(self):
         '''
         test_init test case to test if the object is initialized properly
         '''

         self.assertEqual(self.new_credential.acc_name,"facebook")
         self.assertEqual(self.new_credential.acc_username,"mimy")
         self.assertEqual(self.new_credential.acc_password,"111")

         #########################to save credentials###########
     def test_save_credential(self):
         '''
         test_save_contact test case to test if the credential object is saved into
         the cred_list
         '''
         self.new_credential.save_credential()
         self.assertEqual(len(Credential.cred_list),1)

         #########3save multiple credentials######


     def test_save_multiple_credential(self):
         '''
         test_save_multiple_credential to check if we can save multiple credentials
         objects to our cred_list
         '''
         self.new_credential.save_credential()
         test_credential = Credential("facebook","mimy","111") 
         test_credential.save_credential()
         self.assertEqual(len(Credential.cred_list),2)

         #####to display the alredy saved credential#####

     def test_display_all_credentials(self):
         '''
         test to chech if all credential can be displayed
         '''
         self.assertEqual(Credential.display_credentials(),Credential.cred_list)

         ######find by acc_name#######

     def test_find_contact_by_name(self):
         '''
         test to check if we can find a credential by account_name and display information
         '''

         self.new_credential.save_credential()
         test_credential = Credential("facebook","mimy","111") 
         test_credential.save_credential()
         
         get_credential = Credential.find_by_name("facebook")
         self.assertEqual(get_credential.acc_username,test_credential.acc_username)

       ##########generating password test##############

       
     def test_generate_password(self):
        '''
        test_generate_password test case to test if a given account has its own password
        '''
        self.new_credential.generate_password()
        self.assertEqual(Credential.display_credentials(),Credential.cred_list)


if __name__ == '__main__':
      unittest.main()