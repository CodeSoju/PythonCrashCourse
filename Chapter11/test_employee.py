import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test cases for Employee class"""
    def setUp(self):
        """ Create an employee and a set of responses for use in all test methods."""
        self.my_employee = Employee('Joe', 'Huay', 85000)

    def test_give_default_raise(self):
        value = self.my_employee.give_raise()
        self.assertEqual(value, 90000)
    
    def test_give_custom_raise(self):
        custom_value = self.my_employee.give_raise(10000)
        print(custom_value)
        self.assertEqual(custom_value, 95000)

if __name__ == '__main__':
    unittest.main()