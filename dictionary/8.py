num=int(input("Sir how maney element you want to print :"))
myd={}
sum=0
count=0
for i in range(num):
    keys=input("Please input keys :")
    value=input("Please input values :")
    myd[keys]=int(value)
for k,v in myd.items():
    sum=sum+v
    count=count+1
print(myd)
print("Average is ",sum/count)
