from start_main import *

ext1_string = "This is a string in external file 1"
ext1_int = main_int + 100
print(ext1_string)

def ext_function():
    print("This is an ext_function in external_FILE1 file")

class ext_employee:
   'Common base class for all employees in external file1'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary * 5
      ext_employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % ext_employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)