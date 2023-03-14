
""" lists 000> mutable datatype
access its elements using index
"""
#1- to define a list
l = []
myl = list()

pylist = ['Python','iti', 'iti', 'iti', 'iti', True, 324, 234.666, l]

#2- access elements using index
print(pylist[1])

#3- mutable---> modify existing values
print(pylist)
pylist[2]='updated'
print(pylist)

# pylist[10] = 'addedd'  # list assignment index out of range
#4- append element to the end of the  list.
pylist.append('Appended element. ')
print(pylist)
## 5- insert element at certain index /
pylist.insert(3, 'inserted element')
print(pylist)
pylist.insert(100, 'added extra element ? ') # add element at the end of the list
print(pylist)
## 6- pop element from the list
popped_element = pylist.pop()  #pop will retrun with popped element
print(pylist, popped_element)

##7- pop element at certain index
#
# popped_element = pylist.pop(3)  #pop will retrun with popped element
# print(pylist, popped_element)


##8- remove element
pylist.remove('iti')  # remove first ocurrence of the element
print(pylist)

##9- get index of the element
print(pylist.index('iti'))

# 10 - get length of the list
print(len(pylist))

# 11- concate lists ?
l1 = [3,5,6]
l2 = ["Aisha", 'Basant', 'Salma', 'Hesham', True, 'interesting']
l3 = l1+ l2
print(l3)

##

# names = ['Ahmed', 'Ali']
# course = ['python', names, 36]
#
# course[1].append("new element ")
# print(names)
#
# print(course[1][1])

###12- extend a list
# courses = ['python', 'js', 'spring']
# extended_course = ['django', 'java database']
#
# courses.extend(extended_course)
# print(courses)

########### 13- check if item exists or not in the list ?

names =['Noha', 'Omar', 'Ali', 'Ahmed']
print('Omar' in names)

## 14- loop over the list
#
# for name in names:  #iterable
#     print(name)
#
#
# for c in 'noha':
#     print(c)

## 15- sort the list ? ----> make sure that all the list elements
### from the same type
# ll =[3, 5,True,'Ahmed']
# ll.sort()
names =['Noha', 'Omar', 'Ali', 'Ahmed']
# names.sort()  ## return with None  --> sort acesending
# print(names)
# names.sort(reverse=True)
# print(names)

## 16- reverse a list ?
l = ['Ahmed', True, 324.5, 323]
l.reverse()
print(l)

#### 17- min , max --> items must be from the same type
l = [3,5,6,2334,234,123]
print(max(l))

##18- empty list is falsy value


#19 --- split string to a list

myinfo = "My name is noha, I works at ITI"

print(myinfo.split(' '))


### join list elements to one string ---> list elements must be string
# names = ['ahmed', 'ali', 'noha']
# # newstring = '__|__'.join(names)
# newstring = ''.join(names)
#
# print(newstring)
#####################################

# l1 = [1,2,3]
# l2 = [1,2,3]
# print(l1==l2)

# l1 = [1,2,3, 4]
# l2 = [1,2,3, True]
# print(l1==l2)

# l = [[2,4,5], [2,45], ['Ahmed']]
l = [[2,4,5], [2,-45], [-19]]
l.sort()
print(l)





