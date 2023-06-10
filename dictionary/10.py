user={'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
myd={}
keys="keys"
max=-999999999
for k,v in user.items():
    if v>max:
        max=v
        keys=k 
myd[k]=max
print(keys) 
print("The highest selling book genre is","'"+keys+"'","and the number of books sold are ",max)
#we have a little problem here. we cannt print the key of maximum value.(Solved with keys)