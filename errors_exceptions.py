

""" interpreter detect syntax error --->   must be solved before interpretation

    ==> logical error

    ===> runtime error
"""

# # debug ---> write your own test cases ?
# def sumnum(num1,num2):
#     res = num1 * num2
#     print(res)
#
# sumnum(2,2)
# sumnum(10,20)

# ### runtime error --> exceptions

# unexpected event caused the application to stop ....


# print(name)  # exception  NameError
# print(8/0)  # ZeroDivisionError
# num = int(input("please enter value: "))  # ValueError
##################### Handle the exception #####################
# try:
#     ####
#     pass
# except:
#     pass

# try:
#     print(name)
# except:
#     print("====problem happened ")
#
#
# print("-============== After the exception handling ====================")

""""""
# try:
#     num =int(input("please enter number : "))
# except:
#     print("====problem happened ")
#
#
# print("-============== After the exception handling ====================")
""" detect the exception causes"""
# try:
#     num =int(input("please enter number :"))
#     print(num/0)
# except Exception as e :
#     print(f"====problem happened :{e}")
#
#
# print("-============== After the exception handling ====================")

""" handle exception """
# try:
#     num1 =int(input("please enter number :"))
#     num2 = int(input('please enter num2 '))
#     res = num1/num2
# except Exception as e :
#     print(f"====problem happened :{e}")
#     print("---- hint: operation not allowed so the result will be kept to zero")
#     res = 0
#
#
# print("-============== After the exception handling ====================")


""" operation may led to different runtime errors """
# try:
#     num1 = input("please enter number :")
#     num1 =int(num1)
#     num2 = input('please enter num2 ')
#     num2 = int(num2)
#     res = num1/num2
# except ValueError as ve:
#     # print("--------------- ")
#     print(f"{ve}")
#     # num1 = num2 =1
#     if isinstance(num1, str):
#         print("-- Due to incorrect inputs num1 and num2 are set be 1 ")
#         num1= 1
#         num2 = 1
#     if isinstance(num2, str):
#         print("-- Due to incorrect input num2 is set be 1 ")
#         num2= 1
#     res = num1/num2
#     print(res )
#     exit()
# except ZeroDivisionError as ze :
#     print(f"====problem happened :{ze}")
#     print("---- hint: operation not allowed so the result will be kept to zero")
#     res = 0
# except Exception as exption:
#     print(exption)
#     exit()
#
# print("-============== After the exception handling ====================")

# """
#     try{}catch(){
#     }
# """
""""""
# try:
#     num1 = input("please enter number :")
#     num1 =int(num1)
#     num2 = input('please enter num2 ')
#     num2 = int(num2)
#     res = num1/num2
# except ValueError as ve:
#     pass
# except ZeroDivisionError as ze :
#     pass
#
# except Exception as exption:
#     pass
#
# print("-============== After the exception handling ====================")
# print(res)
############################################################################
""" try except else """
# try:
#     num1 = input("please enter number :")
#     num1 =int(num1)
#     num2 = input('please enter num2 ')
#     num2 = int(num2)
#     res = num1/num2
#
# except ValueError as ve:
#     print(f"{ve}")
#     if isinstance(num1, str):
#         print("-- Due to incorrect inputs num1 and num2 are set be 1 ")
#         num1= 1
#         num2 = 1
#     if isinstance(num2, str):
#         print("-- Due to incorrect input num2 is set be 1 ")
#         num2= 1
#     res = num1/num2
#     print(res )
#     # exit()
# except ZeroDivisionError as ze :
#     print(f"====problem happened :{ze}")
#     print("---- hint: operation not allowed so the result will be kept to zero")
# else:
#     """ this is an optional block """
#     print("---- this block will be executed if there are no problems ")
#     print(res)

# print(res)



# """ try except else finally """
# try:
#     num1 = input("please enter number :")
#     num1 =int(num1)
#     num2 = input('please enter num2 ')
#     num2 = int(num2)
#     res = num1/num2
#
# except ValueError as ve:
#     print(f"{ve}")
#     if isinstance(num1, str):
#         print("-- Due to incorrect inputs num1 and num2 are set be 1 ")
#         num1= 1
#         num2 = 1
#     if isinstance(num2, str):
#         print("-- Due to incorrect input num2 is set be 1 ")
#         num2= 1
#     res = num1/num2
#     print(res )
#     # exit()
# except ZeroDivisionError as ze :
#     print(f"====problem happened :{ze}")
#     print("---- hint: operation not allowed so the result will be kept to zero")
# else:
#     """ this is an optional block """
#     print("---- this block will be executed if there are no problems ")
#     print(res)
# finally:
#     """ this is an optional block """
#     print("=== this block will be called always ====")




""" try except else finally """
try:
    num1 = input("please enter number :")
    num1 =int(num1)
    num2 = input('please enter num2 ')
    num2 = int(num2)
    res = num1/num2

except ValueError as ve:
    print(f"{ve}")
    if isinstance(num1, str):
        print("-- Due to incorrect inputs num1 and num2 are set be 1 ")
        num1= 1
        num2 = 1
    if isinstance(num2, str):
        print("-- Due to incorrect input num2 is set be 1 ")
        num2= 1
    res = num1/num2
    print(res )
    # exit()
except ZeroDivisionError as ze :
    print(f"====problem happened :{ze}")
    print("---- hint: operation not allowed so the result will be kept to zero")
finally:
    """ this is an optional block """
    print("=== this block will be called always ====")























