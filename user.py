from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_info(self, name, email, phone, user_id):
        self.name = name
        self.email = email 
        self.phone = phone
        self.user_id = user_id
    
    def update_location(self, new_location):
        pass
    