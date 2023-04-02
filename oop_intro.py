

# man_= {
#     "name":"ahmed",
#     'age': 22
# }
#
# man2 = {
#     "fullname":"Ali",
#     'age':32
# }

""" template definition for object properties and methods
    create new type --> you can use it in this script only

"""
#
# if __name__=='__main__':
#     print('test')

""" classes """
# class Employee:
#     pass
#
# 'take object from class '
# emp = Employee()  # instance from employee
# print(emp)
# emp.name = 'Ahmed'
# emp.track = 'telecom'
# emp.salary = 20000
#
# emp2 =Employee()
# emp2.firstname='Ali'
# emp2.country ='Egypt'
# print(emp2.firstname)


""" control object creation --> constructor ---> initialize object """

# class Employee:
#     def __init__(self):
#         print("object is being created ")
#         print(self) # --> self refer to object address
#         self.name = 'Ahmed'
#         self.address = 'Cairo'
#         self.track = 'telecom'
#
# emp = Employee()
# print(emp)
#
# emp2 = Employee()

""" customize object creation """

# class Employee:
#     def __init__(self, name, address , track):
#         """ name , address , track ---> instance variables """
#         self.name = name
#         self.address = address
#         self.track = track
#
# emp = Employee("ahmed", 'Cairo','telecom')
# print(emp)
# print(emp.name)
# emp.test =True
#
# emp2 = Employee('Ali', 'test', 'telecom')
# print(emp2.name)
# emp2.salary  =100000
#

"""
    employee :  name, salary 
    
    manager : name, salary , email , admin , country , 

"""

""" """
# class Employee:
#     def __init__(self, name, address='' , track='telecom'):
#         """ name , address , track ---> instance variables """
#         self.name = name
#         self.address = address
#         self.track = track
#
# emp = Employee("ahmed", 'Cairo','telecom')
# print(emp)
# print(emp.name)
# emp.test =True
#
# emp2 = Employee('Ali', 'test', 'telecom')
# print(emp2.name)
# emp2.salary  =100000
#
# emp3= Employee('test')
""" instance methods """

# class Employee:
#     def __init__(self, name, address='' , track='telecom'):
#         """ name , address , track ---> instance variables """
#         self.name = name
#         self.address = address
#         self.track = track
#
#     # instance method
#     def speak(self):
#         print(f"My name is {self.name}, Address = {self.address}")
#
# emp = Employee("ahmed", 'Cairo','telecom')
# print(emp)
# print(emp.name)
# emp.test =True
# emp.speak()
#
# emp2 = Employee('Ali', 'test', 'telecom')
# print(emp2.name)
# emp2.salary  =100000
#
# emp3= Employee('test')
# emp3.speak()
#
#


""" self """
# class Employee:
#     def __init__(self, name, address='' , track='telecom'):
#         """ name , address , track ---> instance variables """
#         self.name = name
#         self.address = address
#         self.track = track
#
#     # instance method
#
#     def speak(var):  # represent self --> instance method --> first argument in the method
#         # --> refer to the call instance  ---> self
#         print("--- in speek function", end=' ')
#         print(f"my name is {var.name} ")
#         print(var)
#
#     def saymessage(self, message=''):
#         print(message)
#
# emp = Employee("ahmed", 'Cairo','telecom')
#
# emp.speak()
# emp.saymessage()
# emp.saymessage('python is easy ')
# emp2 = Employee('Ali', 'test', 'telecom')
#
#
# emp3= Employee('test')
# emp3.speak()



""" count number of objects created from this class """

""" class variable class property ---> property shared between all instances from the class """

# class Employee:
#     no_of_employees = 0  # class Variable
#     def __init__(self, name, address='' , track='telecom'):
#         self.name = name
#         self.address = address
#         self.track = track
#         Employee.no_of_employees +=1
#
#
#     def speak(var):
#         print("--- in speek function", end=' ')
#         print(f"my name is {var.name} ")
#         print(var)
#
# print(Employee.no_of_employees)
# emp = Employee("ahmed", 'Cairo','telecom')
# emp2 = Employee('Ali', 'test', 'telecom')
# emp3= Employee('test')
# print(Employee.no_of_employees)
# emp.no_of_employees = False # create new instance variable for emp.
## del emp.no_of_employees --> valid operatio

# del emp2.no_of_employees  # runtime exception ---> no_of_employees --> class variable



"""note """



# class Employee:
#     no_of_employees = 0  # class Variable
#     def __init__(self, name, address='' , track='telecom'):
#         self.name = name
#         self.address = address
#         self.track = track
#         Employee.no_of_employees +=1
#
#     def speak(var):
#         print("--- in speek function", end=' ')
#         print(f"my name is {var.name} ")
#         print(var)
#
#     def __del__(self):
#         print(f"----{self.name} the object is being deleted now ")
#         Employee.no_of_employees -=1
#
# emp = Employee("ahmed", 'Cairo','telecom')
# emp2 = Employee('Ali', 'test', 'telecom')
# emp3= Employee('test')
# del emp3
# print(Employee.no_of_employees)
# print("------- Application ended ----------------------------")
#
#
#
#
#
#
#

""" ------------------------ class method --------------------------------"""

# class Employee:
#     no_of_employees = 0  # class Variable
#     def __init__(self, name, address , track):
#         self.name = name
#         self.address = address
#         self.track = track
#         Employee.no_of_employees +=1
#
#     def speak(var):
#         print("--- in speek function", end=' ')
#         print(f"my name is {var.name} ")
#         print(var)
#
#     def __del__(self):
#         print(f"----{self.name} the object is being deleted now ")
#         Employee.no_of_employees -=1
#
#     """ function represent behaviour related to the class --> decorator -->
#     @classmethod --> first parameter in the method ---> represent class the instance
#     """
#     # method  --> represent class behaviour not the instance
#     @classmethod  ##
#     def get_no_of_employee(cls):  # cls  --->>
#         print(cls)
#         # return Employee.no_of_employees
#         return cls.no_of_employees
#
#     @classmethod
#     def create_default_object(cls):
#         return  cls('', '','')


# Employee.get_no_of_employee()  # didn't send any parameter

# print(Employee)
#
# print(Employee.get_no_of_employee())
#
# print(Employee.no_of_employees)
#
# emp = Employee("Ahmed", 'ert', 34235)
# # emp2 = Employee()
#
# emp4 = Employee.create_default_object()

""" static method """


class Employee:
    no_of_employees = 0  # class Variable
    def __init__(self, name, address , salary):
        self.name = name
        self.address = address
        self.salary = salary
        Employee.no_of_employees +=1

    def speak(self):
        print("--- in speek function", end=' ')
        print(f"my name is {self.name} ")
        print(self)

    def __del__(self):
        print(f"----{self.name} the object is being deleted now ")
        Employee.no_of_employees -=1

    """ helper function """
    @staticmethod
    def cal_net_salary(salary):
        return salary * .8



emp1 =Employee('Salma', 'Cairo',40000)
emp2 = Employee('Samir', 'Cairo', 30000)
emp3 = Employee('Israa', 'Cairo', 60000)
print(Employee.cal_net_salary(emp1.salary))
print(Employee.cal_net_salary(8923789))
# def cal_net_salary(salary):
#     return salary*.8
#
# print(cal_net_salary(emp3.salary))
# print(cal_net_salary(290839758927))