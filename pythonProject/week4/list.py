# #declare and initialize
# from array import array
# list1=[5,6,7,1,2]  #style1
# list1=list(5,6,7,8,9)  #style2
# arr1=array("i",[7,8,9,1,3])  #array declare and initialize
# list=list(arr1) #array to list   #style3

# # indexing and slicing
# list1=list([5,6,7,8,9])
#
#
# print(list1[0])
# print(list1[10])   #type error
# print(list1[1])
# print(list1[4])
# print(list[-10])  #type error

# print(list1[-1])

# #slicing
# list1=list([5,6,7,8,9,1,2,3,4,0,7,8])
# result=list1[1:100]
# print(result)

# #append(self,object,/)
# list1=list([5,6,7,8,9,1,2,3,4,0,7,8])
# list1.append(True)
# list1.append(False)
# list1.append("Hello")
# print(list1)
#
# #clear(self,/)
# list1.clear()
# print(list1)

#clear(self,/)
# list1=[2,4,5]
# list2=list1
# list2.clear()  #clear list2
# print(list1)  #print list1
# print(list2)  #printlist2
# print(id(list1))
# print(id(list2))

# #copy(self,/)
# list1=[4,5,6]
# list2=list1   #copy by reference
# list3=list1.copy()  #copy by value
# print(id(list1))
# print(id(list2))
# print(id(list3))

# #count(self,value,/)
# list1=[1,2,3,4,5,6,7,7,7,8,9]
# num1=7
# result=list1.count(num1)
# print(result)

# #extend(self,iterate,/)
# list1=[6,7]
# list2=[3,4,5]
# list1.extend(list2)
# print(list1)
#
# from array import array
# arr1=array("i",[4,6,7,8,8])
# list1.extend(arr1)
# print(list1)

# #index(self,value,start=0,stop=922....,/)
# try:
#     list1=[4,6,7,8,8]
#     value=int(input("Enter any number: "))
#     result=list1.index(value)
#     print(result)
# except:
#     print("Not Found")

# list1=[2,7,2,9]
# value=2
# count=list1.count(value)
# start=-1
# for i in range(count):
#     start+=1
#     print(list1.index(value,start))

# #insert(Self,index,object,/)     #to add value in specific place
# #append(self,object,/)    #to add value in last position
# list1=[]
# list2=[5,2]
# list1.append(5)
# list1.append(6)
# list2.insert(0,8)
# list2.insert(2,7)
# print(list1)
# print(list2)

# #pop(self,index=-1,/)   #removing based on index -1
# list1=[1,2,3,4,5,6]
# print(list1)
# list1.pop()
# print(list1)

# #remove(self,value,/)  #remove value
# list1=[5,6,7,8,5]
# print(list1)
# list1.remove(5)   #value 5
# print(list1)

# list1=[5,6,7,8,5]
# print(list1)
# count=list1.count(5)
# for i in range(count):
#     list1.remove(5)
# print(list1)

# #reverse(self,/)
# list1=[1,2,3,4,5]
# print(list1)
# list1.reverse()
# print(list1)

#sort(self,/,*,key=None,reverse=False)
list1=[9,8,2,1,5]
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)  #descending
print(list1)
list1.sort(reverse=False) #ascending
print(list1)