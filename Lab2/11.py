s=int(input("Sir,Please enter your desire number :"))
if s<100:
    l=300-125*s*s
    print(l)
elif s>=100:
    l=(12000/(4+s*s/14900))
    print(l)