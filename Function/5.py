def myfunc(age ,salary,job):
    if age<18 or job=="president":
        tax=0
    elif age>18 and salary<10000:
        tax=0
    elif age>18 and 10000<salary>20000:
        tax=salary*0.5
    elif age>18 and salary>20000:
        tax=salary*0.10
    return tax
age=int(input())
salary=int(input())
job=input()
tax=myfunc(age,salary,job)
print(tax)