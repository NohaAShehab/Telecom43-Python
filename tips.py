"enumrate "

l = [23, 56, 57, 345, 56]
#
# count = 0
# for item in l:
#     print(f"{count}:{l[count]}")
#     count +=1

# for i in range(len(l)):
#     print(f"{i},{l[i]}")

# en =enumerate(l)  ## create index for iterable
# print(en)
#
# list_index =list(en)
# print(list_index)

# for index, value in enumerate(l):
#     print(f"{index}:{value}")


""" lambda  ---> anonymous functions """

""" function need in specific context --->  map , filter """

""" function accept another function as a parameter , 
or return function --> higer order function """

"1-"
# def addfour(num):
#     return num+4
#
#
# def sayhello():
#     print('hello world')
#     return addfour(35)
# #
# print(sayhello())

"2- "
# def addfour(num):
#     return num+4
# def sayhello():
#     print('hello world')
#     return addfour
#
# print(sayhello())
# #
# res = sayhello()
# print(res(84))

"3-"
# def sayhello():
#     print('hello world')
#     return lambda x: x+4
#
# # print(sayhello())
#
# res = sayhello()
# print(res(84))
#
# r=sayhello()(100)
# print(r)

# l = lambda : 10
# print(l)
# print(l())
""" 4- map/ filter """

"generate list even numbers between 0 ,20"

# nums = list(range(0, 21, 2))
# print(nums)
# nums = list(range(0, 21, 2))*5
# print(nums)

""" map any given list --> iterable according"""
# nums = list(range(0, 21, 2))
# print(nums)
#
# def mul_by_five(element):
#     return element * 5
# new_nums =[]
# for num in nums:
#     new_nums.append(mul_by_five(num))
# print(new_nums)


""" generate list ---> list comprehension """

l = [x for x in range(0,21) if x%2==0]
# print(l)

# def mul_by_five(element):
#     return element * 5
# mapped_l = map(mul_by_five, l)
# print(list(mapped_l))

# mapped_l = map(lambda x:x*5, l)
# print(list(mapped_l))

# mapped_l = map(lambda x:x*5, l)
# print(mapped_l)
# print(list(mapped_l))
#
# l = list(map(lambda i:i*5, [x for x in range(0,21) if x%2==0]))
# print(l)

""" filter --> filter elements according to condition """

l = [4,63,234,56,76,3,69,323,0]

odd_elements = filter(lambda x:x%2!=0, l)
print(list(odd_elements))


