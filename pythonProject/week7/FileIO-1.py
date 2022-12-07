# # Create new file
# file=open("data.txt", "w")
# file.write("Hello!\n")
# file.write("How are you?\n")
# file.close()

# #append on file
# file=open("data.txt", "a")
# file.write("Good\n")
# file.close()

#read file
file=open("data.txt", "r")
contents=file.readlines()
print(contents)
