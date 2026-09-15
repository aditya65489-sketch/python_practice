'''from threading import *
def show () :
    print("this is a child thread")
t=  Thread(target = show())
t.start()
print("this is parent thread")'''

'''from threading import *
class MyThread(Thread) :
    def run(self):
        for i in range(5) :
            print("\nthis is a child thread")
t = MyThread()
t.start()
for i in range(5) :
    print("\nThis is the main thread")'''

'''from threading import *
class Demo:
    def show(self) :
        for i in range(5) :
            print("This is a child thread")
obj = Demo()
t =Thread(target=obj.show)
t.start()
for i in range(5) :
    print("This is parent thread")'''

from threading import *
import time
class Demo:
    def num(self) :
        for i in range(1,6) :
            print("The number is", i)
            time.sleep(1)
    def double(self) :
        for i in range(1,6) :
            print("The double of the number is", 2*i)
            time.sleep(1)

    def square(self) :
        for i in range(1,6) :
            print("The square of the number is", i*i)
            time.sleep(1)
obj = Demo()
t1= Thread(target=obj.num)
t2= Thread(target=obj.double)
t3= Thread(target=obj.square)


t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()
time.sleep(0.2)

t1.join()
t2.join()
t3.join()

print("This is the main thread")
