def pattern():
    for i in range (5):
        for j in range (1+i):
            print("%",end=" ")
        print(" ")

def readInt():
    return int(input("Enter no.of rows: "))

def age():
    age = int(input("How old are you?"))
    print("You will get {} candles on your birthday next year".format(age+1))
