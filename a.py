# a=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# z=a[0]
# while i<len(a):
#     if a[i]>z:
#         z=a[i]
#     i=i+1
# a.remove(z)
# j=0
# k=a[0]
# while j<len(a):
#     if a[j]>k:
#         k=a[j]
#     j=j+1
# print(k)


# import json
# user=input("singup or login:")
# name=input("enter your name:")
# if user=="singup":
#     password=input("enter the password:")
#     re_password=input("enter the password:")
#     dob=input("enter DOB :")
#     gender=input("your gender:")
#     print("your ac has been created")
#     deta={"user":user,"name":name,"password":password,"password2":re_password,"dob":dob,"gender":gender} 
#     with open (name+".json","w")as f:
#         b=json.dump(deta,f,indent=2) 
# else:
#     print("login") 
#     a=open(name+".json","r")
#     b=a.read()
#     c=json.loads(b)
#     if name==c["name"]:
#         password=input("enter your paasword")
#         if password==c["password"]:
#             print("login successfull")
#         else:
#             print("password is  wrong")
#     else:
#         print("your name is wrong")




# a=int(input("enter num:"))
# if a<=9999 and a>999:
#     print("yes")
# else:
#     print("no")    

num=int(input("enter number:"))
# i=0
# a=[]
# while i<num:
#     i=+1
#     name=input("enter name:")
#     a.append(name)
#     print(a)
    # i=+1
i=0
while i<num:
    j=0
    while j<=i:
        print(i,end="")
        j=+1
    i=+1
            
    