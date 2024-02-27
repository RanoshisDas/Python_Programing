c=int(input('Enter total call '))
b=float(200)
if c<=100:
    print('your bill is: ',b)
elif c>100 and c<=150:
    a=float(c-100)
    b=b+(a*0.60)
    print('your bill is: ',b)
elif c>150 and c<=200:
    a=float(c-150)
    b=b+(50*0.6)+(a*0.5)
    print('your bill is: ',b)
elif c>200:
    a=float(c-200)
    b=b+(50*0.6)+(50*0.5)+(a*0.4)
    print('your bill is: ',b)