user=int(input("Please give a number :"))
if user%2==0 and user%5==0:
    print("Multiple of 2 and 5 both")
elif user%2==0 or user%5==0 :
    print(user)
else:
    print("Not a multiple we want")