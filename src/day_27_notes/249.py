#unlimited Arguments

def add(n1, n2):
    return n1 + n2

add(n1=5, n2=3)

#unlimited Arguments
def add(*args):
    for n in args:
        print(n)

add(3, 5, 7, 8)
