

#Unlimited Positional Arguments
def add(*args):
    for n in args:
        print(n)
add(3,5,7,8)

#Unlimited Keyword
def add(**kw):
    x = kw.get("n1")
    y = kw.get("n2")
    print(x + y)
add(n1=5, n2=50)
