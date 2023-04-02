
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         # self.__grade = grade
#         self.grade = grade
#         self.__salary = 10000
#
#
#
# s = Student("Ahmed", 2094)
# s.country = 'Egypt'
# s._country = 'Egypt'
# s.__country = 'Egypt'
# print(s.__country)
# s._Student__country = 'Egypt'
# print(s._Student__country)





# print(s.__dict__)


# class Student:
#     __slots__ = ['name', 'grade', '__salary']
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#         self.__salary = 10000
#
#
#
# s = Student("Ahmed", 2094)
# s.country = 'Egypt'

# class Student:
#     __slots__ = ['name', 'grade', '__salary']
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#         self.__salary = 10000
#
#
#     def __dict__(self):
#         # return "test"
#         d = {}
#         d['name']= self.name
#         d['grade'] = self.grade
#         return d
#
#
#
# s = Student("Ahmed", 2094)
# # s.country = 'Egypt'
#
# print(s.__dict__())

################## "special methods "

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.__salary = 10000

    def __str__(self):
        """ function must return with string """
        return self.name

    def __repr__(self):
        """ function must return with string """
        return f"Student(name={self.name}, grade ={self.grade}, salary= {self.__salary})"

    def __len__(self):
        "function must return with number "
        return len(self.__dict__)

    def __add__(self, other):
        self.name = f"{self.name} {other.name}"
        self.__salary = self.__salary + other.__salary

s = Student("Ahmed",90)
# print(s) # address --->
# s.country ='er'
print(s.__repr__())
# print(len(s))
#
s2 = Student("Ali",45)

s + s2

print(s.__repr__())






#
# l = [434]
# l.append('sdf')
# print(l)
# print(len(l))




