def myfunc(user):
    for h in range(1,user+1):
        print(" ")
    for i in range(1,h+1):
        print(i,end=" ")
    for k in range(h-1,0,-1):
        print(k,end=" ")
user=int(input())
myfunc(user)