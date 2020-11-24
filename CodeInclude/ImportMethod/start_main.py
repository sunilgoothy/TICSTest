"""This is the main entry file"""
print("Starting of script......")
from external_file1 import *
print("External file1 import completed")
main_string = "This is main file"
main_int = 100


def main_function():
    print("This is a main_function in main file")

class main_employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      main_employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % main_employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)




if __name__ == "__main__":
    print("__main__ function starting......")
    print("-" * 80)

    emp1 = main_employee("Tim", 2000)
    emp2 = main_employee("Tom", 5000)

    emp1.displayEmployee()
    emp2.displayEmployee()

    print("Total Employee %d" % main_employee.empCount)
    print("main INT: ", ext1_int)
    print("-" * 80)

    emp3 = ext_employee("Pim", 2000)
    emp4 = ext_employee("Pom", 5000)

    emp3.displayEmployee()
    emp4.displayEmployee()

    print("Total Employee %d" % ext_employee.empCount)
    print("External File1 INT: ", ext1_int)
    print("-" * 80)