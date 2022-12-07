import sys

def customerManager():
    while (True):
        print("------Customer Management------")
        print("1. New")
        print("2. Display All")
        print("3. Search")
        print("4. Edit")
        print("5. Delete")
        print("0. Exit")
        print("--------------------------------")
        choice2 = int(input("Enter your choice: "))
        if choice2 == 1:
            print("Add new customer")
        elif choice2 == 2:
            print("All customer")
        elif choice2 == 3:
            print("Search customer")
        elif choice2 == 4:
            print("Edit customer")
        elif choice2 == 5:
            print("Delete customer")
        elif choice2 == 0:
            break
        else:
            print("Out of range")

while(True):
    print("--------Main Menu--------")
    print("1. Customer")
    print("2. Driver")
    print("3. Trip")
    print("0. Exit")
    print("-------------------------")


    choice1 = int(input("Enter your choice: "))
    if choice1 == 1:
        customerManager()
    elif choice1 == 2:
        print("Driver Manager")
    elif choice1 == 3:
        print("Trip Manager")
    elif choice1 == 0:
        print("bye!!!")
        sys.exit() #program exit
    else:
        print("Out of Range")

