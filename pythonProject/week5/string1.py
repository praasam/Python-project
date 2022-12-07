#ste
#collection of characters
#character-> symbol of language
#english -> characters -256
#alphabets (aAzZ)  -string
#digits(89)  -numeric type
#symbols(*,?)  -operator
#control (ctrl,shift,alt)
#256
#character  -> numeric value
#chracter value -> ASCII Value
#ASCII Value  -> character
#65        -> A
#66        -> B


#declare and initialize
str1 = "PCPS College"
str2 = 'PCPS College'
str3 = """PCPS College"""  #multi-line string
str4 = '''PCPS College'''  #multi-line string

#explore str class
# print(help(str))

# #capitalize(self,/)
# #return a capitalized version of the
# str1 = "pcps College"
# str2 = str1.capitalize()
# print(str1)
# print(str2)

# #casefold(self,/)
# #return a version of the string suitable
# password1 = 'admin'
# password2 = 'AdmiN'
# result = password1 == password2
# print(result)
# pwd1 = password1.casefold()
# pwd2 = password2.casefold()
# result2 = pwd1 == pwd2
# print(result2)

# #center(self,width,fillchar='',/)
# amount = 123.4567
# # result = str(amount).center(20, '*')
# # result = str(amount).ljust(20, '*')
# result = str(amount).rjust(20, '*')
# print(result)

# #count(sub[,start[,end]])  ->int
# str1 = """qwertyuiopoiuytrewqwertyuiopoiuytrewqqwertyuiop"""
# str2 = "i"
# result = str1.count(str2)
# print(result)

# #reading txt file
# file = open("TheHungerGames.txt")
# # str1 = file.read(100)
# str1 = file.readlines()
# str2 = " ".join(str1)
# result = str2.count('is ')
# print(result)
# # print(type(str2))
# # print(str1)
# # print(str2)


#example
# #list to string
# list1 = ['word1','word2','word3']
# str2 = " ".join(list1)
# print(len(str2))

# #endswith(suffix[,start[,end]])  ->bool
# str1 = "pcps college."
# result = str1.endswith(';')
# print(result)

# #expandtabs (Self,/,tabsize=8)
# str1 = "SN\tNAME\tADDRESS"
# str2 = str1.expandtabs(tabsize=15)
# print(str2)

# #find(sub[,start[,end]])  ->int
# str1 = "pcps college,lalitpur"
# str2 = 'l'
# count = str1.count(str2)
# print(count)
# r1 = str1.find(str2)
# print(r1)
# r2 = str1.find(str2, r1+1)
# print(r2)
# r3 = str1.find(str2, r2+1)
# print(r3)
# r4 = str1.find(str2, r3+1)
# print(r4)

#automated
str1 = "pcps college, lalitpur"
str2 = "l"
count = str1.count(str2)
result = -1
results = []
for i in range (count):
    result = str1.find(str2, result+1)
    results.append(result)
print(results)
print(result)


