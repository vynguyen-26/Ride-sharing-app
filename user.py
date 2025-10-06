from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def __init__(self, name, email, phone, user_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.user_id = user_id
    