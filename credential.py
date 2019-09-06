class Credential:
    '''
    a class that generates new credential instance
    '''
    credential_list = [] 
    def __init__(self,cred_acc,username,password):
        '''
        this is a method is showing the properties of the above method
        '''
        self.cred_acc = cred_acc
        self.username = username
        self.password = password