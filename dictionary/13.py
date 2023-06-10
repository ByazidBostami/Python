list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
myd={}
for k,v in list_1:
    if k not in myd:
        myd[k]=[v]
    else:
        myd[k].append(v)
print(myd)