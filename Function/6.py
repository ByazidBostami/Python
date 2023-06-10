def myfunc(user):
    if user > 0:
        year = user // 365
        remdays = user % 365
        months = remdays // 30
        remdays1 = remdays % 30
        print("year:", year, "months:", months, "Days :", remdays1)

user = int(input("Please input days to calculate: "))
myfunc(user)