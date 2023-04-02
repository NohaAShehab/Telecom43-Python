""" all classes in python ---> implicitly inherits from class object """
""" 
    overloading 
    
    overriding

"""
l = ['er', 'wer','wr']
l.append('kfjklj')

#
# class Employee:
#     no_of_employees = 0
#     def __init__(self,name):
#         self.name = name
#         self.track = 'telecom'
#         self.test = 'abc'
#         Employee.no_of_employees +=1
#
#     def speak(self):
#         print("I am an employee")
#
# emp = Employee("Ahmed")
# print(emp.__dict__)
#
#
# class Teacher(Employee):
#     pass
#
#     def speak(self):
#         super().speak()
#         print("--- I am a teacher --------------")
#
#
# t=  Teacher("test")
# t.speak()

""" overload """



class Overloading:
    # def sayhello(self):
    #     print('Hello')

    def sayhello(self,message=''):
        print(f'Hello {message}')



o  =Overloading()
o.sayhello()
o.sayhello('poiropi')

" no explicit overloading in python "

""" you can implement overloading via installing package dispatch """