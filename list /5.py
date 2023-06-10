mylist=["hey", "there", "", "what's", "", "up", "", "?"]
newlist=[]
for i in mylist:
    if i!="":
        newlist.append(i)
print(newlist)