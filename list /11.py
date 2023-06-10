list1=[1,4,3,2,6]
list2=[5,6,9,8,7]
flag=False
for i in list1:
    for j in list2:
        if i==j:
            flag=True
if flag==True:
    print("True")
else:
    print("False")