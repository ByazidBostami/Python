mytup= ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
mylist=[]
finaltup=()
for i in mytup:
    mylist.append(i)
for i in range(len(mylist)-1,-1,-1):
    finaltup+=(mylist[i],)
print(finaltup)
