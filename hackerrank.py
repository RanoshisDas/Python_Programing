# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
m=int(input())
a=int((n-1)/2)
b=int((m-1)/2)
b1=b
#1st half
for i in range(a):
        
        for j in range(1,b):
            print("-",end="")
        if i==0:
            print(".|.",end="")

        for k in range(i):
            print(".|.",end='')
        if i!=0:
            print(".|.",end='')
            
        for k in range(i):
            print(".|.",end='')

        for j in range(1,b):
            print("-",end="")
        b-=3
        print()
#middle
for i in range(3,b1):
    print("-",end='')
print("WELCOME",end="")
for i in range(3,b1):
    print("-",end='')
print()
#last half
b+=3
m-=6
for i in range(a,0,-1):
    for j in range(1,b):
        print("-",end="")

    for k in range(0,m,3):
            print(".|.",end='')
            
    for j in range(1,b):
            print("-",end="")
    b+=3
    m-=6
    print()