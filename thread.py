'''from threading import *
def show () :
    print("this is a child thread")
t=  Thread(target = show())
t.start()
print("this is parent thread")'''
import threading

'''from threading import *
class MyThread(Thread) :
    def run(self):
        for i in range(5) :
            print("\nthis is a child thread")
t = MyThread()
t.start()
for i in range(5) :
    print("\nThis is the main thread")'''

from threading import *
class Demo:
    def show(self) :
        for i in range(5) :
            print("This is a child thread")
obj = Demo()
t =Thread(target=obj.show)
t.start()
for i in range(5) :
    print("This is parent thread")


