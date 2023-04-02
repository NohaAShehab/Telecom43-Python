


# class Human:
#     pass
#
# class Employee(Human):  # inheritance
#     pass
#
#
# """ inheritence support is - a relation """
# emp = Employee()
# print(isinstance(emp, Human))


""" """
""" inherit properties , methods"""
# class Human:
#     pass
#     def speak(self):
#         print("I am human")
#
# class Employee(Human):  # inheritance
#     pass
#
#
# """ inheritence support is - a relation """
# emp = Employee()
# print(isinstance(emp, Human))
# emp.speak()

# class Human:
#     def __init__(self,name):
#         self.name = name
#
#
#     def speak(self):
#         print("I am human")
#
# class Employee(Human):  # inheritance
#     pass
#
#
# """ inheritence support is - a relation """
# emp = Employee('Ahmed')
# print(isinstance(emp, Human))
# emp.speak()
""" ==="""
#
#
# class Human:
#     def __init__(self,name):
#         self.name = name
#
#
#     def speak(self):
#         print("I am human")
#
# class Employee(Human):  # inheritance
#     def __init__(self,name, salary):
#         super().__init__(name)
#         self.salary  =salary
#
#
# """ inheritence support is - a relation """
# emp = Employee('Ahmed',9482)
# print(isinstance(emp, Human))
# emp.speak()



""" mutiple inheritence """

#
#
#
# class Alive:
#     pass
#     def __init__(self, state):
#         self.alive = state
#
# class Human:
#     def __init__(self,name):
#         self.name = name
#
#
#     def speak(self):
#         print("I am human")
#
# class Employee(Alive, Human):  # inheritance
#     def __init__(self,name, salary):
#         # super().__init__(True)
#         super(Employee, self).__init__(True)
#         Human.__init__(self, name)
#         self.salary  =salary
#
#
# """ inheritence support is - a relation """
# emp = Employee('Ahmed',9482)
# print(isinstance(emp, Human))
# emp.speak()
#


""" ---->  __init_ function <--- """

#
# class Teacher:
#     pass
#
# class Engineer:
#     pass
#
# class Instructor(Teacher, Engineer):
#     pass
#
#
# inn = Instructor()
"""--------------------"""



# class Teacher:
#     pass
#
# class Engineer:
#     def __init__(self,dept):
#         self.dept =dept
#
# class Instructor(Teacher, Engineer):
#     pass
#
#
# inn = Instructor("telecom")

""" """
# class Teacher:
#     pass
#
# class Engineer:
#     def __init__(self,dept):
#         self.dept =dept
#
# class Instructor(Teacher, Engineer):
#     def __init__(self, dept, intake):
#         super(Instructor, self).__init__(dept)  # super() will call the first parent that has __init__
#         self.intake =intake
#
#
# inn = Instructor("telecom", 43)

' teacher has __init__'

# class Teacher:
#     def __init__(self, course):
#         self.course =course
#
# class Engineer:
#     def __init__(self,dept):
#         self.dept =dept
#
# class Instructor(Teacher, Engineer):
#     def __init__(self, dept, intake, course):
#         super(Instructor, self).__init__(course)  # super() will call the first parent that has __init__
#         Engineer.__init__(self, dept)
#         self.intake =intake
#
#
# inn = Instructor("telecom", 43, 'python')


""" inheritance """

# class Parent:
#     pass
#
# class A(Parent):
#     pass
#
# class Test(A,Parent):
#     pass
#
#
# t = Test()



# class Parent:
#     def __init__(self):
#         self.parent= True
#
# class A(Parent):
#     def __init__(self):
#         self.a= True
#
# class Test(A,Parent):
#     def __init__(self):
#         self.test = 'abc'
#         super(Test, self).__init__()
#         Parent.__init__(self)
#
# t = Test()

""" """


class Parent:
    def __init__(self):
        self.name= 'test'


class A(Parent):
    pass


class B(Parent):
    pass


class Child(A, B):
    def __init__(self):
        super(Child, self).__init__()



c= Child()


