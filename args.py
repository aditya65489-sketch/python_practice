'''def func1 (*args):
    for i in args:
        print(i)


func1 (1,10.2,30,25,"Aditya" )'''
from IPython.utils.PyColorize import C2

'''def func1 (*args, **kwargs):
    for i in kwargs.items ():
        print(i)


func1 ( a= 10, b= 20, c= 30,  )'''


'''def func1 ():
    x= 10
    def func2 (x):
        return x+1
    return func2 (x)


result= func1()
print(result)'''

'''def func1 (called_func):
    print("This is the first function")
    def nested_func1 (called_func):
        print("This is the nested function")
        called_func()
    return nested_func1 (called_func)

def outer_func ():
    print("This is the outer function")


obj= func1(outer_func)'''

#factory
B=type("BaseClass", (object,), { })
C1=type("C1", (B,), {'val' :5})
C2=type("C2", (B,), {'val' :10})



def ClassCreator(bool):
    if bool:
        return C1()
    else:
        return C2()



print(ClassCreator(True).val)
print(ClassCreator(False).val)