

# info = ["Noha", 'iti', 30]  #unlabeled

## datatype- --> represent labeled data

## dictionary ? ---> comma-seperated : key:value pair

#1- define a dict
# d = {}
# myd = dict([])
## dict ---> doesn't allow key duplication
### from 3.7 ---> sorted datatype ### key:value --->
# # according the order you pass it
# d = {"name":"Noha", "work":'iti', 'age':30, "name":'Noha Shehab'}
# print(d)


### dict  --> access data using keys
# print(d["name"])

### dict ---> key with number


# according the order you pass it
# d = {"name":"Noha", "work":'iti', 'age':30, 2:True}
# print(d[2])
#
# d[2] = 'updated'

##################################
# according the order you pass it
d = {"name":"Noha", "work":'iti', 'age':30}
## add key:value pair to the dict
d['track']  ='Telecom'
print(d)
## get dict keys

d_keys = d.keys()
# print(d_keys)
#
# # for k in d_keys:
# #     print(k)
# keys = list(d_keys)
# print(keys)

# d_values = d.values()
# print(d_values)
### loop over the dict
# for item in d:
#     # print(f"item = {item}")
#     print(f"item = {item}, ---> {d[item]}")
### in operator
# print("Noha" in d)
############### keys , values

items = d.items()
print(items) # dict_items  --->can be casted to list
# for i in d.items():
#     print(i)

# for key , value in d.items():
#     print(f"{key}:{value}")

### get len of the dict
print(len(d))

## update dict ---->
# info = {"name":"noha"}
# add_info = {"name":"Noha", "track":"Telecom", "age":20,
#             'courses': {"mongo", 'admin01', 'PHP'}
#             }
#
# info.update(add_info)
#
# print(info)
######### --->

# keys = ["name", 'email']
# myd ={}
# myd=myd.fromkeys(keys, True)
# print(myd)

### zip
# keys =["name", 'email']
# values = ["noha", 'noha@gmail.com']
# #
# res = zip(keys, values)
# print(res)
#
#
# # res = dict(zip(keys, values))
# print(res)


##################### clear
# d.clear()  # remove key:value pairs ---> empty dict

l = ["Salma", "python", 'True']
## pop(index) ---> pop() last element  ----> return with popped element
## remove("element I want to remove" ) ---> None
### del variable name ---> remove variable from the memory
