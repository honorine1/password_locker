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
         self.new_credential = Credential ('keza joy','kjoy','kezajoymami2020') #create user object


     def tearDown(self):
         '''
         tearDown method that does clean up after each test case has run.
         '''
         User.users_list = []