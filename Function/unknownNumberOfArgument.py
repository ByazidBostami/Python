def myfunc(*nums):
    print(nums)
myfunc(1)
myfunc(1,2,3,4)
myfunc("Byazid","Bostami",110,[121])
# for print as a tuple 
def myfunc(*nums):
    for i in nums:
        print(i,end=",")
myfunc(1)
myfunc(1,2,3,4)
myfunc("Byazid","Bostami",110,[121])