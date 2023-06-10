
time=int(input("Give an hour="))

if(4<=time<=6):
  print("Breakfast")
if(12<=time<=13):
  print("Lunch")
if(16<=time<=17):
  print("Snacks")
if(19<=time<=20):
  print("Dinner")
elif(0<=time<=23):
  print("Patience is a virtue")

else:
  print("Wrong time")
