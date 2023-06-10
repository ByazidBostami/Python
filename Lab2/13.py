#task13
mark=int(input("Input a marks :"))
if (90<=mark<=100):
  print("A")
elif (80<=mark<=89):
   print("B")
elif (70<=mark<=79):
   print("C")
elif (60<=mark<=69):
   print("D")
elif (50<=mark<=59):
   print("E")
elif (0<=mark<=50):
   print("F")
else:
   print("invalid number")