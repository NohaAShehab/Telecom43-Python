# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name  # public
#         self._age = age  # protected
#         self.__salary = salary  # private ==> you need to apply logic on the property
#
#     def display_info(self):
#         print(f"{self.name}, {self._age}, {self.__salary}")
#
#     def getSalary(self):
#         return self.__salary * .8
#
#     def setSalary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise TypeError(f"Salary should be number not  {type(salary)}")
#
#
# emp = Employee("Test", 83, 82376)
# print(emp.getSalary())
# emp.setSalary("19999")
#
# emp.name = 'updated'
# print(emp.name)


""" ---->"""

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name  # public
#         self._age = age  # protected
#         # self.__salary = salary  # private ==> you need to apply logic on the property
#         self.setSalary(salary)
#
#     def display_info(self):
#         print(f"{self.name}, {self._age}, {self.__salary}")
#
#     def getSalary(self):
#         return self.__salary * .8
#
#     def setSalary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise TypeError(f"Salary should be number not  {type(salary)}")
#
#
# emp = Employee("Test", 83, 8798)
# # print(emp.getSalary())
#


""" """
class Employee:
    def __init__(self, name, age, salary):
        self.name = name  # public
        self._age = age  # protected
        # self.__salary = salary  # private ==> you need to apply logic on the property
        # self.setSalary(salary)
        self.salary = salary  #


    def display_info(self):
        print(f"{self.name}, {self._age}, {self.__salary}")

    @property
    def salary(self):
        return self.__salary * .8

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int) or isinstance(salary, float):
            self.__salary = salary
        else:
            raise TypeError(f"Salary should be number not  {type(salary)}")

    @property
    def breif_name(self):
        return self.name[-1]

emp = Employee("Test", 83, 10000)
print(emp.salary)  # calculated
print(emp.name)
emp.salary = 894923
print(emp.__dict__)
print(emp.breif_name)
# emp.breif_name = 'eio'





