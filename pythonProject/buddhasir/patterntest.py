from pattern import pattern
from pattern import readInt
from pattern import age
pattern()

num1 = readInt()
print("num1:", num1)
for i in range(num1):
    for j in range(i + 1):
        print("%", end=" ")
    print()

age()
