a=float(input('1st sem:'))
b=float(input('2nd sem: '))
c=7*a
d=(850*b)/100
if (c*10)%10<5:
    c=(c//1)
else:
    c=(c//1)+1

if (d*10)%10<5:
    d=(d//1)
else:
    d=(d//1)+1
r=d+c
print('you got',r,'out of 1550')