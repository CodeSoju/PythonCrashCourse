class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_value=''):

        if raise_value:
            return self.annual_salary + int(raise_value)
        else:
            self.annual_salary += 5000
            return self.annual_salary