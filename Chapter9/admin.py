class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.height = 0
        self.weight = 0
        self.login_attempts = login_attempts
        
    
    def describe_user(self):
        print(f"You are {self.first_name} {self.last_name}.\n")
        print(f"Your weight is {self.weight} lbs. Your height in cm is {self.height}.\n")
        print(f"You've logged in {self.login_attempts} times.\n")
    
    def greet_user(self):
        print(f"Good to have you onboard {self.first_name}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts
    
    def reset_login_attempts(self):
        self. login_attempts = 0
        return self.login_attempts

class Privileges():
    def __init__(self, privileges):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        for x in range(len(self.privileges)):
            print(f"Admin {self.privileges[x]}\n")


class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = Privileges([])
