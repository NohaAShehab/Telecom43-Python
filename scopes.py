
# course = 'python'  # global variable -->
# # can be accessed anywhere in the script
#
#
# print(course)
#
# def displaycourse():
#     print(f"From the function course = {course}")
#
# displaycourse()

##########################

# def course_info():
#     course = 'django'  ####  local variable ---> can be accessed
#     ### in the function scope only
#     print(f"course = {course}")
#
# course_info()
# print("----------------------------")

#################### Modify global variable from inside function


# course = 'python'  # global
#
# def modifyCourse():
#     global course
#     course = input("please enter course name: ")
#     print(f"course from inside the function {course}")
#
# modifyCourse()
# print(course)
#
""
###############################function inside onther function ####################
# def outerfun():
#     course = 'Python'
#     def innerfun():
#         course = 'django'  # new local variable for the inner function
#         print(f"inner function course = {course}")
#
#
#     innerfun()
#     print(f"course = {course}")
#
# outerfun()

# def outerfun():
#     course = 'Python'
#     def innerfun():
#         nonlocal course
#         course = 'django'  # new local variable for the inner function
#         print(f"inner function course = {course}")
#
#     innerfun()
#     print(f"course = {course}")
#
# outerfun()









def saHello():
    print("----- Hello Hesham -----")
    def test():
        print("test")
        print("############# inside test #################")

    test()

saHello()











