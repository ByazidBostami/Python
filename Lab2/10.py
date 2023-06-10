user=int(input("Please input working hour :"))
if 0<user<=40: 
    print("Salary",user*200)
elif 168>user>40:
    print("Salary",8000+(user-40)*300)
if(user<0):
  print("Hour cannot be negative")
if(user>168):
  print("Impossible to work more than 168 hours weekly")
