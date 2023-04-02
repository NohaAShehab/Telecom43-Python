" function ---> it's goal -> setting value , get the value of specific property"


class Student:
    def __init__(self, name, grade):
        self.name = name
        # self.__grade = grade
        self.grade = grade
        self.__salary = 10000


    @property
    def salary(self):
        return self.__salary


    # def grade(self):
    #     return self.__grade
    @property
    def grade(self):
        return self.__grade

    # def setgrade(self, grade):
    #     if isinstance(grade, int) or isinstance(grade, float):
    #         if 0<grade<100:
    #             self.__grade  =grade
    #         else:
    #             raise  ValueError("Grade should be between 0 and 100")
    #     else:
    #         raise TypeError(f"Grade should int or float not {type(grade)}")

    @grade.setter
    def grade(self, grade):
        if isinstance(grade, int) or isinstance(grade, float):
            if 0<grade<100:
                self.__grade  =grade
            else:
                raise  ValueError("Grade should be between 0 and 100")
        else:
            raise TypeError(f"Grade should int or float not {type(grade)}")
s = Student('Ahmed', 20)
# print(s.__grade)
# print(s.grade())
# print(s.grade)
# # s.setgrade(82)
# s.grade = 6
print(s.grade)
print(s.salary)