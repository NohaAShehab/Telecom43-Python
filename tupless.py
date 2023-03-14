"tuple is immutable datatype "
"tuple is immutable datatype "
# 1- to define a tuple
t = ()
myt = tuple()

pytuple = ('Python', 'iti', 'iti', 'iti', 'iti', True, 324, 234.666, t)

# 2- access elements using index
print(pytuple[1])
#


##9- get index of the element
print(pytuple.index('iti'))
#
# # 10 - get length of the tuple
print(len(pytuple))
#
# # 11- concate tuples ?
t1 = (3, 5, 6)
t2 = ("Aisha", 'Basant', 'Salma', 'Hesham', True, 'interesting')
t3 = t1 + t2
print(t3)
#
# ##
#

# ########### 13- check if item exists or not in the tuple ?
#
names = ('Noha', 'Omar', 'Ali', 'Ahmed')
print('Omar' in names)
#
# ## 14- loop over the tuple
# #
for name in names:  # iterable
    print(name)

#### 17- min , max --> items must be from the same type
t = (3, 5, 6, 2334, 234, 123)
print(max(t))
#
# ##18- empty tuple is falsy value
#
#
#
# ### join tuple elements to one string ---> tuple elements must be string
names = ('ahmed', 'ali', 'noha')
newstring = '__|__'.join(names)
print(newstring)
# newstring = ''.join(names)
# #
# # print(newstring)
# #####################################
# cast list to tuple and viceversa
# l = [3,5,6]
# t = tuple(l)

# t = ("Ahmed", 'Hesham', 'ali')
# myl = list(t)
#
# # tuple of one element
# t = ("Ahmed",)
# print(t, type(t))
