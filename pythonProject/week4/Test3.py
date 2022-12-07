#import library
from MyFunctions3 import readInt, calcSum, printMessage

# #call function
# n1 = readInt() #read value for n1
# #read value for n2
# n2 = readInt()
# n3 = calcSum(n1, n2)
# print(n3)

n1 = 7
n2 = 8
n3 = 9
n4 = calcSum(calcSum(n1, n2), n3)
print(n4)

printMessage("Num1", n1)
printMessage("Num2", n2)
printMessage("Nun3", n3)
printMessage("Num4", n4)

