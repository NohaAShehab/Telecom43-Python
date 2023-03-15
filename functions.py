################ function with known number arguments.
#
# def sayHello():
#     pass
#
# sayHello()
##################3


# def sayHello():
#     pass
#
# res = sayHello()  # return None

# def sayHello():
#     return
#
# res = sayHello()  # return None

#############################33
# def sayHello():
#     print("Hello world")
#
# res = sayHello()  # return None

################333
# def sayHello():
#     print("Hello world")
#     return 'Hello world'
#
# res = sayHello()  # return


# def sayHello():
#     print("Hello world")
#     return []
#
# res = sayHello()  # return Tuple

########################
# def get_fullname(firstname, lastname):
#     fullname = firstname + " "+ lastname
#     return( fullname, firstname ), lastname
#
#
# n = get_fullname("Noha", "Shehab")
# print(n)

#####################################
# def sumnums(num1, num2):
#     print(f"num1 ={num1}, num2 ={num2}")
#     res = num1 + num2
#     print(res)
#     return res
#
# # res1= sumnums(10, 20)
# # res2= sumnums("Ahmed",'Ali')
# res3 = sumnums(3,'Ahmed')

###########################
# def sumnums(num1:int, num2:int) -> int:  # define for you 00> clean code
#     print(f"num1 ={num1}, num2 ={num2}")
#     res = num1 + num2
#     print(res)
#     return res
#
# res1= sumnums(10, 20)
# res2 = sumnums("Ahmed", 'Ali')
###################################################
print(isinstance('noha', int))

# def sumnums(num1:int, num2:int) -> int: # define for you 00> clean code
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1 ={num1}, num2 ={num2}")
#         res = num1 + num2
#         print(res)
#         return res
#
# res1= sumnums(10, 20)
# res2 = sumnums("Ahmed", 'Ali')

###################### python allow default arguments #################################
#
# def sumnums(num1, num2=10) -> int:  # define for you 00> clean code
#     print(f"num1 ={num1}, num2 ={num2}")
#     res = num1 + num2
#     print(res)
#     return res
#
#
# sumnums(2)
# sumnums(344,456)
#
#
#
# print("noha", 'ahmed', 'ali',sep='__||__')
# print("skdfjfklj" ,end='$$$$$$$$$$$$$$$$$')
# print('ksjfksjdkljf')
#
####################### function with variable number of argumeents

# def askfornumbers(*nums):  # *---> function accept zero or more argument
#
#     print(nums,type(nums))
#
# askfornumbers(312,435)

#####################

# def introduce_yourself(**info):  #Keyword arguments
#     print(info, type(info))
#
#
# introduce_yourself(name='noha', work='iti', age=30)
# introduce_yourself()
# introduce_yourself(fname='salma', lname='ali', hoppy='standup comedy')
#


temp = 'My name is {username}, I lives in {usercity}'
print(temp.format(username='noha', usercity='cairo'))
















