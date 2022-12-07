# # print(help(set))
#
#
# #declare and initialize
# from array import array
# set1 = {}
# set1 = set([1,2,3,4,5])  #list to set
# set1 = set(1,2,3,4,5)    #tuple to set
# set1 = set(array("i",[3,4,5,6,7]))  #array to set

# #Add(...)
# set1 = {1,2,3}
# set1.add(6)
# set1.add(1)
# print(set1)

# #Clear (....)
# set1 = {5,6,7,8,9,1,1,2}
# print(set1)
# set1.clear()
# print(set1)

#Copy(....)
# set1 = {3,2,1,3,2,1,4}
# set2 = set1  #copy by reference
# print(id(set1))
# print(id(set2))
# set3 = set1.copy()  #copy by value
# print(id(set3))

# #Difference(...)
# set1 = {1,2,3,4,6,5}
# set2 = {4,5,6,7,8}
# set3 = set1.difference(set2)
# print(set3)
# set3 = set2.difference(set1)
# print(set3)

# #intersection(...)
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# set3 = set1.intersection(set2)
# print(set3)

# #union
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# set3 = set1.union(set2)
# print(set3)

# #pop(...)
# set1 = {1,2,3,4,5,6,7}
# print(set1)
# set1.pop()  #remove from -1 index
# print(set1)

# #remove(...)
# set1 = {1,2,3,4,5,6,7}
# print(set1)
# set1.remove(3)  #remove specific value
# print(set1)


