
### loop ---> while
# num = 1
# l = []
# while num < 11:
#     l.append(num)
#     num+=1  # num += 1
#
# print(l)

#### range ? ---> datatype can generate ranges of numeric values


# r = range(10)  # range object --> iterable
# print(r)
# # for num in r:
# #     print(num)
#
# myl = list(r)
# print(myl)
#


# r = range(1,10, 2)  # range object --> iterable
# print(r)
#
# myl = list(r)
# print(myl)


# r = range(1,10, -2)  # range object --> iterable
# print(r)
#
# myl = list(r)
# print(myl)

# r = range(10,1, -2)  # range object --> iterable
# print(r)
#
# myl = list(r)
# print(myl)

######################### ask the user to enter info

mynum = input("please enter number ")  # return with string
print(mynum, type(mynum))
if mynum.isdigit():
    mynum = int(mynum)

print(mynum, type(mynum))




