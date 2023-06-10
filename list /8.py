list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 11, 12, -13, -14, -15, -16]
list3=list1+list2
mylist=[]
for i in list3:
    if i%2==0:
        mylist.append(i)
print(mylist)