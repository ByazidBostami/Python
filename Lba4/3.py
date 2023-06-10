user=input("Input something :")
length=len(user)
check=True
for i in user:
    if i!="0" and i!="1":
        check=False
if check==True:
    print("Binary Number")
else:
    print("Not a Binary number")
