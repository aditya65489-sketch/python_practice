'''class Person :

    def __init__(self) :
        self.name = "Sam"
        self.gender = "Male"
        self.age = 22

    def talk(self) :
        print("Hi I'm", self.name)

    def vote(self) :
        if self.age< 18 :
            print("i am not eligible to vote")
        else :
            print("I am eligible to vote")

obj= Person()
Person.talk(obj)
Person.vote(obj)'''

'''class Person :
    def __init__(self,n,g,a) :
        self.name = n
        self.gender = g
        self.age = a

    def talk(self) :
        print("Hi I'm", self.name)

    def vote(self) :
        if self.age< 18 :
            print("i am not eligible to vote")
        else:
            print("i am eligible to vote")


obj1 = Person("Sam","Male",18)
obj2 = Person("Jesse", "Female", 16)
obj1.talk()
obj1.vote()

obj2.talk()
obj2.vote()'''


'''class car :
    def __init__(self, year, speed) :
        self.year = year
        self.speed = speed
    def getSpeed(self) :
        print("maximum speed is:", self.speed)
    def setSpeed(self, speed) :
        self.speed = speed

BMW = car(2018, 155)
FORD = car(2016, 140)

BMW.getSpeed()
BMW.setSpeed(143)

BMW.getSpeed()
FORD.getSpeed()'''


'''class car :
    def __init__(self, year, speed) :
        self.year = year
        self.speed = speed
    def getSpeed(self) :
        print("maximum speed is:", self.speed)
    def setSpeed(self, speed) :
        self.speed = speed
        #print(self.speed)

BMW = car(2018, 155)
FORD = car(2016, 140)
#inheritence
class Sedan(car) :   #child class
    def accelerate(self) :
        print('137')
    def openTrunk(self) :
        print("trunk has been opened")

class SUV(car): #child class
    def accelerate(self) :
        print('127')
Honda = Sedan(2018, 150)
BMW.getSpeed()
Honda.getSpeed()
Honda.openTrunk()
Honda.accelerate()'''

#polymorphism
class car :     #parent class
    def __init__(self, name) :
        self.name = name

class Sedan(car) :   #child class
    def accelerate(self) :
        print('137')

class SUV(car): #child class
    def accelerate(self) :
        print('127')

objL = [Sedan("camry"), SUV("scorpio")]

for obj in objL :
    print (obj.name+" : ", end="")
    obj.accelerate()