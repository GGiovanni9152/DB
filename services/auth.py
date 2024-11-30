import repositories.users

users = repositories.users.get_users_with_password()


class Authotize():

    def __init__ (self):
        self.users = self.get_users()
    
    def get_users(self):
        users = repositories.users.get_users_with_password()
        return {user["email"]: user["password"] for user in users}

    def auth(self, email, password):
        #print(self.users)
        passw = None

        if email in self.users:
            passw = self.users[email]
        
        if (passw == None):
            return False
        if (passw == password):
            return True



    
            