list1=[1,4,7,5]
list2=[6,1,3,9]
list1[len(list1)-1]=list2[0]

for i in range(1,len(list2)):
    list1.append(list2[i])
print(list1)
