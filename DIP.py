from abc import ABC, abstractmethod

class ILoginService(ABC):
    @abstractmethod
    def validte_user(self, user_name:str, password:str):
        pass
    
class LoginService(ILoginService):
    def validte_user(self, user_name:str, password:str):
        
        return user_name == "admin" and password == "admin"
    
class SecurityService:
    def __init__(self, login_service: ILoginService):
        self.login_service = login_service
        
    def login_user(self, user_name : str, password:str) -> bool:
        return self.login_service.validte_user(user_name, password)

def main():
    security_service = SecurityService(LoginService())
    is_logged_in = security_service.login_user("admin", "admin")
    print(f"Login successful: {is_logged_in}")
    
if __name__ == "__main__":
    main()