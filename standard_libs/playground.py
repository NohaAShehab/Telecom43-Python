
""" standard lib to deal with os """

# import os
#
# try:
#     os.mkdir("/home/noha/Telecom43_")
# except Exception as e:
#     print(e)

""" create file """
# import  os
# print(os.path)
#
# os.system('ls -l')
#
# os.system('touch abc.txt')
#
# # os.system('mkdir back')
# print(os.getcwd())
# os.chdir('/home/noha')
# print(os.getcwd())
# print(os.getlogin())

""" math lib """
# import  math
# # print(math.pi)
# print(math.ceil(345.6))
# print(math.floor(2334.3))
# print(math.pow(3,5))
# print(math.sqrt(16))
""" re ---> regular expression , regex """

import  re


## math
pattern  = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

email  = input("please enter your email : ")

## match return with match object if part of the string follows the pattern
# result =  re.match(pattern, email) # valid ---> match object else None
# print(result)
# if result:
#     print("---- email well formatted")
# else:
#     print("---Error with the input email ----")

""" full match ---> make sure that the string parts follows the pattern """
result =  re.fullmatch(pattern, email) # valid ---> match object else None
print(result)
if result:
    print("---- email well formatted")
else:
    print("---Error with the input email ----")

