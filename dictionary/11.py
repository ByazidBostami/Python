user=input()
user=user.lower()
myd={}
for i in range(len(user)):
    key=user[i]
    if key in myd.keys():
        myd[key]=myd[key]+1
    else:
        myd[key]=1
print(myd)