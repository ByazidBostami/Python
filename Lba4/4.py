user=input("Sir,Please input something :")
length=len(user)
if length<4:
  print(user)

if length>3 and user[length-2:length:1]=="er":
  print(user[0:length-3]+"est")
elif length>3 and user[length-2:length:1]=="est":
  print(user)
elif length>3:
  print(user+"er")