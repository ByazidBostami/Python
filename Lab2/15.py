user=float(input("Please enter your cgpa :"))
user_cr=int(input("How maney credit did you cover :"))
if 3.89>=user>=3.80 and user_cr>=30:
    print("The student is eligible for a waiver of 25 percent.")
if 3.94>=user>=3.90 and user_cr>=30:
    print("The student is eligible for a waiver of 50 percent.")
if 3.95>=user>=3.99 and user_cr>=30:
    print("The student is eligible for a waiver of 75 percent.")
if user==4.00 and user_cr>=30:
    print("The student is eligible for a waiver of 100 percent.")
else:
    print("The student is not eligible for a waiver")