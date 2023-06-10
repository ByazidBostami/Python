#This is how we can input dictionary from user 
user=int(input("Please enter how many element on your dictionary"))
myd={}
for i in range(user):
    keys=input("Please input keys-")
    value=input("Please input values-")
    myd[keys]=int(value)
print(myd)