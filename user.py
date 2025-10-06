class User:
    def __init__(self, name, email, phone, user_id, current_location):
        self.name = name
        self.email = email
        self.phone = phone
        self.user_id = user_id
        self.current_location = current_location
    
    def update_location(self, new_location):
        self.current_location = new_location