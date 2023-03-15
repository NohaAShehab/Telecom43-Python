"""
    sets
"""
# 1- define a set
# myset = set()





### set contain different data from datatypes
# myset = {"Noha", "Adham", "Ahmed", "Ahmed", "Aisha",
#          "Aya", True, 444, 32.35}

## unsorted datatype , no index, remove duplication

# print(myset)  ### hashing



# myset = {"Noha", ("Adham", "Ahmed"), "Ahmed", "Aisha",
#          "Aya", True, 444, 32.35}


# myset = {"Noha", ["Adham", "Ahmed"], "Ahmed", "Aisha",
#          "Aya", True, 444, 32.35}

# myset = {"Noha", {"Adham", "Ahmed"}, "Ahmed", "Aisha",
#          "Aya", True, 444, 32.35}


#### operations
myset = {"Ahmed", 'iti', True, 345, 423.345}  # iterable
print(set)
for s in myset:
    print(s)

### mutable datatype ---> add element to the set in the runtime
myset.add("added element")

## remove element

## remove random element
popped_element = myset.pop()
## in operator
# myset.remove("Ahmed")
# print(myset)

if 'Ahmed' in myset:
    print("found")
# popped_element = myset.pop()
#
# popped_element = myset.pop()
#
# popped_element = myset.pop()
#
# popped_element = myset.pop()


s1 = {"django", 'python', 'postgres','flask'}

s2 = {'spring','java', 'GSM', 'python'}

s1.update(s2)
print(s1)

