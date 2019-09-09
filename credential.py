import random
from user import User
class Credential:
    '''
    a class that generates new credential instance
    '''
    cred_list = [] 
    ##################initialization test###########
    def __init__(self,acc_name,acc_username,acc_password):
        '''
        this is a method is showing the properties of the above method
        '''
        self.acc_name = acc_name
        self.acc_username = acc_username
        self.acc_password = acc_password

        #######3to save the credential####
    def save_credential(self):

        '''
        save_contact method saves credential objects into cred_list
        '''

        Credential.cred_list.append(self)

        ##########3to display the saved credentials#######
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the cred_list
        '''
        return cls.cred_list

        #########to find a given credential using acc_name#######

    @classmethod
    def find_by_name(cls,acc_name):
        '''
        Method that takes in a site name and returns a credential that matches that site name.

        '''

        for credential in cls.cred_list:
            if credential.acc_name == acc_name:
                return credential

   

        ##########method to generate password#######

    @classmethod
    def generate_password(cls):
        '''
        A method to generate a credential generate_password
        '''

        passwordlen = 8
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?0123456789"
        gen_password ="".join (random.sample(s,passwordlen))
        return gen_password

