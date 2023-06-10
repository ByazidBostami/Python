#Task-6
user=input("Please input something separated by comma :")
mylist=user.split(",")
newlist=[]
maxi=0
index=0
for i in mylist:
  inlist=int(i)
  newlist.append(inlist)
for i in range(len(newlist)):
  if newlist[i]>maxi:
    maxi=newlist[i]
    index+=i

print("Largest number in the list is ",maxi,"Which was found at index",index)