# #to print % % % %
# i = ("%, %, %, %")
# print(i)
# print(i)
# print(i)
# print(i)

# for i in range (3):
#     for j in range (5 ):
#         print("%)", end=" ")
#     print("")

rows = int(input("Enter any number of rows: "))
columns = int(input("Enter any number of columns: "))
for j in range(rows):
    for i in range(columns):
        print("%", end=" ")
    print(" ")