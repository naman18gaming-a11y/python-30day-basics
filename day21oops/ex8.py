#Exercise 8: User Class with Password Validation
class user:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def username(self):
        if self.username == "":
            return "Username cannot be empty"
        return self.username
    def check_password(self, input_password):
        return self.password == input_password

u1 = user("namanlendi","oye123")   
print(u1.username('namanlendi'))  
print(u1.check_password("oye123"))
