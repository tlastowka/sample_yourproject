from api.tokens import Token
from pushservices.apns import delete_function

class SomeClass(object):
    
    def delete(self,token):
        
        
        delete_function(token)
        
        
if __name__ == '__main__':
    
    token = Token('some token')
    sc = SomeClass()
    
    sc.delete(token)
    