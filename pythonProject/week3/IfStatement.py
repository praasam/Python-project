# # Basics
# # Variable declare
# # Value assign
# # Operators
# # Assignment, Relational
#
#
#
# num1 = 0
# if(num1 == 0):
#     print("Zero")
#
# if(num1 != 0):
#     print("Not zero")
#
# num1 = 0
# if(num1 == 0):
#     print("Zero")
#
# num2 = 5
# if(num2 !=0):
#     print("not zero")
#
# num1 = input("enter any number")
# num1 = int(num1)
# if(num1 == 0):
#     print("zero")
# else:
#     print("not zero")
#     print("no")

#
# day = input("enter value(1-7):")
# day = int(day)
# if(day == 1):
#     print("SUN")
# if (day == 2):
#     print("MON")
# if(day == 3):
#     print("TUE")
# if(day == 4):
#     print("WED")
# if(day == 5):
#     print("THU")
# if(day == 6):
#     print("FRI")
# if(day == 7):
#     print("SAT")
# if (day <= 0):
#     print("Others")
# if (day >= 7):
#     print("Others")

# Month = input("Enter any number(1-12):")
# Month = int(Month)
# if(Month == 1):
#     print("JAN")
# if(Month == 2):
#     print("FEB")
# if(Month == 3):
#     print("MAR")
# if(Month == 4):
#     print("APR")
# if(Month == 5):
#     print("MAY")
# if(Month == 6):
#     print("JUNE")
# if(Month == 7):
#     print("JULY")
# if(Month == 8):
#     print("AUG")
# if(Month == 9):
#     print("SEPT")
# if(Month == 10):
#     print("OCT")
# if(Month == 11):
#     print("NOV")
# if(Month == 12):
#     print("DEC")
# if(Month <= 0):
#     print("out of range")
# if(Month >= 13):
#     print("out of range")


# #declare
# year = None
# #input
# year = input("Enter your age : ")
# year = int(year)
# if(year >=18):
#     print("You are eligible to vote")
# else:
#     print("You're not eligible to vote")

#nested if
sub1 = 70
sub2 = 80
pm = 40
result = "fail"
if sub1>= pm:
    if sub2>= pm:
        result = "pass"
print(result)


