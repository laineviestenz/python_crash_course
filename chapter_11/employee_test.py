import unittest
from employee import Employee

class test_employee(unittest.TestCase):
    def setUp (self):
        """create a test employee called worker with salary = 4320"""
        self.worker = Employee('laine', 'viestenz', 4320)
    
    def test_standard_raise(self):
        """test if a standard raise gives an employee a 5000 raise"""
        Employee.give_raise(self.worker)
        salary = self.worker.salary
        self.assertEqual(salary, 9320)

    def test_custom_raise(self):
        """test that a custom 1000 raise works properly"""
        Employee.give_raise(self.worker, 1000)
        salary = self.worker.salary
        self.assertEqual(salary, 5320)

unittest.main()