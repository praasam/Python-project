num1 = None
num2 = None

# #to check whether the number is even or odd number
# num1 = int(input("Enter any number:"))
# if num1%2 == 0:
#     print("even")
# else:
#     print("odd")
#
# #to check whether the number is positive, negative or zero
# num1 = int(input("Enter any number:"))
# if num1>0:
#     print("positive")
# elif num1<0:
#     print("negative")
# else:
#     print("zero")
#
# #to display last digit of number
# n1 = int(input("Enter any number:"))
# n2 = (n1 % 10)
# print(n2)

# #to check whether the last digit of number is divisible by 7 or not
# num1=int(input("Enter any number: "))
# num2=num1%10
# if (num2%7==0):
#     print("divisible by 7")
# else:
#     print("not divisible by 7")

# #to check whether an year is leap year or not
# num1=int(input("Enter any year: "))
# if(num1%4==0):
#     print("leap year")
# else:
#     print("not a leap year")

#to display the name of day like 1 for sunday...
day = int(input("Enter any number(1-7): "))
if day==1:
    print("Sunday")
if day==2:
    print("Monday")
if day==3:
    print("Tuesday")
if day==4:
    print("Wednesday")
if day==5:
    print("Thursday")
if day==6:
    print("Friday")
if day==7:
    print("Saturday")
if day<=0:
    print("Other")
if day>=8:
    print("Other")