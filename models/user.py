
class User:
    def __init__(self, id=None, email:str = None, name:str = None, password:str = None) -> None:
        self.id:int | None = id
        self._email:str = email
        self._name:str  = name
        self._password:str = password
        
    def getDados(self) -> dict:  
        return {
            
            "id":self.id, 
            "email":self._email, 
            "name":self._name, 
            "password":self._password
        }
    
        