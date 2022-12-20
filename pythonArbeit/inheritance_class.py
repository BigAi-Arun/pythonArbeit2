#Inheritence in python

class person:

    def __init__(self,name):
        self.name=name

    def displayName(self):
        print(self.name)

    def isEmployed(self):
        print(self.name,"is un-emplyed !!")        


#dreived class aka child class
class Employee(person):

    def __init__(self,emp_name,id_num,salary,designation):
        self.idnumber=id_num
        self.emp_salary=salary
        self.emp_designation=designation
        #calling construtor of base class
        # person.__init(self,emp_name)
        super().__init__(emp_name)

    def isEmployed(self):
        print(self.name,"is Employed!!")

    def employeeDeatails(self):
        print("Employee ID is ",self.idnumber,
        "Employee slary",self.emp_salary,
        'Employee Dessignation',self.emp_designation )

# emp = person('shashank')
# emp.displayName()
# emp.isEmployed()
# emp.emp_name
# emp.employeeDetails()

# # emp = person('shashank')
# emp.displayName()
# emp.isEmployed()

# emp = person('shashank')
# emp.displayName()
# emp.isEmployed()
# emp.emp_salary

emp1 = Employee('Kunal',12, 1000,'Data engineeer')
emp1.displayName()
print(emp1.name)
emp1.employeeDeatails()