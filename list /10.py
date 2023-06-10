user=input()
mylist=user.split(",")
newlist=[]
finallist=[]
for i in mylist:
    newlist.append(int(i))
print("Input list :",newlist)
for i in range(len(newlist)):
    if newlist[i] not in finallist:
        finallist.append(newlist[i])
print("Modified list :",finallist)
