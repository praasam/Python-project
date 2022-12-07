# #declare and initialize
# address = {
#     'houseno.':1,
#     'street':'street-1',
#     'tole':'tole1',
#     'wardno.':2,
#     'vdc/mpc':'abc',
#     'district':'abc',
#     'zone':'bagmati',
#     'state':'bagmati'
#
# }
# student = {
#     'sid':1,
#     'name':'Prasamsha Maharjan',
#     'email':'maharjanprasamsha102@gmail.com',
# }
# address = {
#     'houseno.':1,
#     'street':'street-1',
#     'tole':'tole1',
#     'wardno.':2,
#     'vdc/mpc':'abc',
#     'district':'abc',
#     'zone':'bagmati',
#     'state':'bagmati'
# }
# print(type(address))
# print(address)
# print(student)

# #clear method
# student = {
#     'sid':1,
#     'name':'Prasamsha Maharjan',
#     'email':'maharjanprasamsha102@gmail.com',
# }
# print(student)
# student.clear()
# print(student)

# #copy method
# student = {
#     'sid':1,
#     'name':'Prasamsha Maharjan',
#     'email':'maharjanprasamsha102@gmail.com',
# }
# s1 = student.copy()  #copy by value
# print(id(student))
# print(id(s1))
# s2 = student #copy by reference
# print(id(s2))

# #get(self,key,default=None,/)
# student = {
#     'sid':1,
#     'name':'Prasamsha Maharjan',
#     'email':'maharjanprasamsha102@gmail.com',
# }
# print(student.get('sid'))
# print(student['sid'])
# print(student.get('name'))
# print(student['name'])
# print(student['email'])
# print(student.get('email'))

# #items(...)
# student = {
#     'sid':1,
#     'name':'Prasamsha Maharjan',
#     'email':'maharjanprasamsha102@gmail.com',
# }
# print(student.items())

#keys(...)
student = {
    'sid':1,
    'name':'Prasamsha Maharjan',
    'email':'maharjanprasamsha102@gmail.com',
}
# print(student.keys())

#values(...)
# print(student.values())

#pop(...)
#popitem(self,/)

#keys and for loop
keys = student.keys()
for key in keys:
    print(key,"=",student[key])
