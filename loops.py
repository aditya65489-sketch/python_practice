#var= int(input("Enter a multiple of 7"))
#while var%7 !=0:
    #var= int(input("Enter a multiple of 7"))
#else:
    #print("%d is a multiple of 7" % var)

#x = [1,6,"simpliearn"]
#for i in x:
    #print(i)

#x = "simpliearn"
#for i in x:
    #print(i)

#x= [1,2,3,],["a","b","c"]
#for i in x:
    #for j in i:
        #print(j,end=" ")

#x= "hey there. how are you?"
#for i in x:
    #if i == ".":
        #break
    #print(i, end=" ")

"""for i in [1,13,56,4,6]:
    if i>14:
        continue
    print(i)"""
from pygments.lexers import python

#accesing elements of loops
#x= [1,4,2,"python"]
#for i in x:
    #print(i)

"""for i in range(0,21,2):
    print(i)"""

"""sum=0
for i in range(0,21):
    if i%2==0:
        sum=sum+i
print(sum)"""

#using pattern for loop
#1
#12
#123
#1234
#12345

"""n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""

#accesing elements of matrix
"""r=int(input("enter the number of rows"))
c=int(input("enter the number of columns"))
x=[]
val=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j,int(input ("enter the %d * %d elements" %(i,j))))
    x.insert(i,val)
    val=[]
y=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j,int(input ("enter the %d * %d elements" %(i,j))))
    y.insert(i,val)
    val=[]
sum=[]

for i in range(0,r):
    for j in range(0,c):
        val.insert(j, x[i][j] + y[i][j])
    sum.insert(i,val)
    val=[]
print(sum)"""

#demo of while loop
"""i=1
while i<=10 :
    print("python")
    i=i+1""" #also can use i+=1

"""i=10
while i>=1:
    print("python")
    i-=1"""

"""i=1
sum=0
while i<=10:
    sum=sum+i
    i+=1
print(sum)"""


"""i=1
sum=0
while i<=10:
    if i%2==0:
        sum=sum+i
    i+=1
print(sum)"""

#reversing a integer
"""n= int(input("enter the number"))
nr=0
#n=5678
#nr=8765
while n%10!=0:
    c=n%10
    nr=nr*10 +c
    n=n//10
print(nr)"""


"""x= [1,2.3,"python"]
length=0
i=0
try:
    while x[i]:
        length=length+1
        i+=1
except IndexError:
    print(length)"""

#Nested while loop
#1
#22
#333
#4444
#55555

"""n=int(input("enter the number"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    i+=1
    print()"""


import random
nump= random.randint(1000,9999)
n = int(input("enter a 4 digit  number"))

while n!=10:
    num=nump
    cor = 0
    while num %10 :
        numc= num%10
        nc= n%10
        num= num//10
        n=n//10
        if numc==nc:
            cor=cor+1
    if cor==4:
        print("congrats! you guessed it right")
        break
    else:
        print("%d digits were guessed it right"%cor)
        n = int(input("enter a 4 digit  number"))
else:
    print("you quit the game")
