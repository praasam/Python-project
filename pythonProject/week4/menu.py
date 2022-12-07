import sys
list1 = []  #black lists
while(True):
    print("-----Main Menu-----")
    print("1. ADD")
    print("2. Display All")
    print("0. Exit")
    print("-------------------")
    choice=int(input("Enter your choice:"))
    print("--------------------")
    print("Your choice is:{}".format(choice))
    if(choice>=0 and choice<=2):
        match choice:
            case 1:
                tmp = int(input("Enter any number: ")) #add
                list1.append(tmp)
            case 2:
                print(list1) #display all
            case 0:
                print("Bye!!")
                sys.exit()
