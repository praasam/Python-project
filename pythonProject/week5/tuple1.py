# tuple-read only
# print(help(tuple))
# declare and initialize
# creating tuples
# from array import array
# tup1 = ()
# tup1 = tuple()
# tup1 = tuple([4,5,6,7,8,9])
# tup1 = 4,5,6,7,8,9
# arr1 = array("i",[4,5,6,7,8,9])
# tup1 = tuple(arr1)   #array to tuple

# #indexing   -> extract single value based on index
# tup1 = 2,3,4,5,6
# result = tup1[-1]
# print(result)
# result = tup1[2]
# print(result)

# #slicing  multiple values
# tup1 =3,4,5,6,7
# result = tup1[0:3]
# print(result)

# #count (self,value,/)
# tup1 = 5,4,5,6,7,5,4,3,5,6
# value = 5
# result = tup1.count(value)
# print(result)

# index (self,value,start=0,stop=92...07,/)
tup1 = 2, 3, 4, 1, 5, 6, 5
value = 5
result = tup1.index(value)
print(result)

count = tup1.count(value)
start = -1
for i in range(count):
    start += 1
    print(list1.index(value, start))