
""" class, object  ---> wrapping data , functionality into one component """

""" encapsulation ==> limit accessibility to the properties , methods """

"""
    access modifiers 
    public  ---> access variable anywhere in the script --> self (in class) ,,, object ==> outside the class
    private  ---> access variable anywhere in the class --> self, outside the class no
    protected  --> access variable in the class or the derived class 
    
    --------------------------- No explicit Access Modifiers ----------------------------------
    -- access modifiers 00>  naming ---> variable , function 
    [a-z] ====> public property
    _ ===> protected property
    __ ===> private property

"""

class Employee:
    def __init__(self,name, age, salary):
        self.name = name  # public
        self._age = age # protected
        self.__salary = salary  # private


    def display_info(self):
        print(f"{self.name}, {self._age}, {self.__salary}")


emp=  Employee('Ahmed', 25, 823768)
# emp.display_info()
# print(emp.name)
# print(emp._age)  # it-works  # ethically please don't this
# print(emp.__salary)  # private --> cannot be accessed, Attribute error

print(emp.__dict__)
print(emp._Employee__salary) # it-works  # ethically please don't this

