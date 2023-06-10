user=input("Sir,Please input something :")
length=len(user)
temp=""
newlist=[]

for i in range(length):
    if user[i]!=" ":
        temp+=user[i]
    elif(user[i]==" "):
        newlist.append(int(temp))
        temp=""
print(newlist)

    
    