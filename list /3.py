mylist=[]
for i in range(5):
    user=int(input("Sir Please input a number :"))
    mylist.append(user)
for i in range(len(mylist)-1,-1,-1):
    print(mylist[i])