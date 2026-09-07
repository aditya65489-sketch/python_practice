def welcome():
    print("Welcome to My Friend")

welcome()

def add(b,a):
    total = a+b
    print("a:%d,b:%d"%(a,b))
    print("The sum is",total)

add(a=10,b=20)
x=2
y=3
add(x,y)


def add(a=0,b=0):
    total = a+b
    print("a:%d,b:%d"%(a,b))
    print("The sum is",total)

add(10)

def add(*a):
    total=0
    for i in a:
        total=total+i
    print("The sum is",total)

add(10,20,30,40,50)
add(2)


def add(a,b):
    print(id(a),id(b))
    a=2
    b=3
    print(id(a),id(b))
    total=a+b
    print("The sum is",total)

x=10
y=20
print(id(x), id(y))
add(x,y)
print("The sum is",x+y)


def add(lst):
    lst[2]=0

lst=[0,1,2]
print(lst)
add(lst)
print(lst)

def add(a,b):
    total=a+b
    return total

result=add(10,20)
print("The sum is",result)