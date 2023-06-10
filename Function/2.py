user=int(input())
def myfunc(num):
    a=0
    b=1
    print(a,end=" ")
    if num>=2:
     print(b,end=" ")
    for i in range(2,num):
      sum=a+b
      print(sum,end=" ")
      a=b
      b=sum
myfunc(user)