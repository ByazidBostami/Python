user=int(input("Sir,please enter a number for calculate :"))
hour=user//3600
remsec=user%3600
minutes=remsec//60
againremsec=remsec%60
print("Hours:",hour,"Minutes:",minutes,"Second:",againremsec)