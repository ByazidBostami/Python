user=input("Sir, please input something :")
user1=int(input("Sir,Please enter a reverse number :"))
for i in range(user1,-1,-1):
    print(user[i],end='')
for i in range(user1+1,len(user),1):
    print(user[i],end='')