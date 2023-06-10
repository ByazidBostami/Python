user=input("Please input something")
finallist=[]
mylist=user.split(",")
length=len(mylist)
if length<4:
    print("Not Possible")
else:
    newlist=mylist[2:length-2]
    for i in newlist:
        inti=int(i)
        finallist.append(inti)
print(finallist)