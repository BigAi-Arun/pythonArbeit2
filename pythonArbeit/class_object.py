# class Employee:
#     # Constructor of class
#     # it is mainly used for assignment of instance variables
#     def __init__(self, name, salary ):
#         # instance variable or instance attributes
#         self.emp_name = name
#         self.emp_salary = salary
#     # method of a class
#     def displayEmployeeInfo(self):
#         print("Employee name : ",self.emp_name, " , Employee Salary : ",self.emp_salary)

# emp1 = Employee('Arun', 1000)
# emp2 = Employee('Rahul', 2000)

# emp1.displayEmployeeInfo()
# emp2.displayEmployeeInfo()

# print(emp1.emp_name)
# print(emp2.emp_name)



class Employee:

    empcount=0
    #Constructor of class
    # it is mainly used for assignment of instance variables
    def __init__(self, name, salary ):
        # instance variable or instance attributes
        self.emp_name = name
        self.emp_salary = salary
        Employee.empcount +=1
    # method of a class
    def displayEmployeeInfo(self):
        print("Employee name : ",self.emp_name, " , Employee Salary : ",self.emp_salary)
    def displayEmployeeCount(self):
        print("Employee count : ", Employee.empcount )    

emp1 = Employee('Shashank', 1000)
emp1.displayEmployeeInfo()
emp1.displayEmployeeCount()
emp2 = Employee('Rahul', 2000)
emp2.displayEmployeeInfo()
emp2.displayEmployeeCount()


print(emp1.emp_name)
print(emp1.emp_salary)

print(emp2.emp_name)
print(emp2.emp_salary)

emp1.empcount = 10
emp2.empcount= 20
print(emp1.empcount)
