dis=float(input("Distance="))
tim=float(input("Time="))
sum=(dis/1000)/(tim/3600)
print(sum,"km/h")
if(sum<60):
  print("Too slow. Needs more changes.")
elif(60<=sum>=90):
  print("Velocity is okay. The car is ready!")
elif(sum>90):
  print("Too fast. Only a few changes should suffice")