#1.create a blank list
list1 = []
print(list)

#2. append 100 random numbers in list (int)
import random
MAX = 100
for i in range(MAX):
    tmp = random.randint(16,24)
    list1.append(tmp)
print(list1)

# #3. export all values to data.txt file  #save files
# file1 = open("data.txt","w")
# for i in range(len(list1)):
#     file1.writelines(str(list1[i]))
# file1.close()

# #print max number of list
# max = max(list1)
# min = min(list1)
# print(max)
# print(min)

#search user given number in list
tmp = int(input("Enter any number to search: "))
result = list1.count(tmp)
if (result==0):
    print("Not Found")
else:
    print("Found {} times".format(result))

#calculate average age
#sorting ages in ASC order
#sorting ages in DES order
