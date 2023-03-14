######## strings

#### strings  ------> is immutable datatype  ##########
work = "Information Technology Institute"
print(work[2:8])   # char from index 2:7
# print(work[::-1])
# # print(work[100])
# print(len(work))
# print(work.count('i'))
#############################

#### string is immutable 00> return new string
fname = 'Noha'
midname='Abdelhady'
lname = 'Shehab'

# fullname = fname + midname +midname + lname
# print(fullname)

# fullname = fname + midname*2 + lname
# print(fullname)

mystring = 'i love iti o o o '
# print(mystring.capitalize())
# print(mystring.title())
# print(mystring.upper())
print(mystring.replace('o', '@'))
print(mystring.replace('o', '@', 2))

### format string
# temp = 'My name is {0} I lives in {1}'
# print(temp.format('noha', 'cairo'))
# print(temp.format('Salma', 'Cairo'))
#
# temp = 'My name is {username} I lives in {usercity}'
# ### usercity and username  are keywords
# print(temp.format(usercity='october', username='Hesham' ))
#
# ################ f-format string
# myname = 'noha'
# mycity = 'cairo'
# ## myname , mycity are variables
# temp = f'My name is {myname} I lives in {mycity}'
# print(temp)
################################3

name = 'noha'
print(name.isalpha())
print(name.isdigit())

# num ="20"
# print(num.isdigit())

# num ="20.093"
# print(num.isdigit())

num ="20"
# print(num.isnumeric())

# message = '                   '
# print(message.isspace())

# print('noha'.islower())
####################### strip string

message = '           I love Python                       '
# print(len(message))
# print(message)
# # print(message.strip())
# # print(message.lstrip())
# print(message.rstrip())

message = '           I love Python                       '

print(message.strip("n "))

################ Numbers
c = complex(4, 5)

print(round(33445.56))


a = 10
b = 1200
c = -20
print(min(a,b,c))


