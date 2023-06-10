user=int(input("foo_moo:"))
def myfunc(num):
    if num%2==0:
        return "Foo"
    if num%3==0:
        return "Moo"
    if num%2==0 and num%3==0:
        return "FooMoo"
    else:
        return "Boo"
myfunc(user)
print(myfunc(user))