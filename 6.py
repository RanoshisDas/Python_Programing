a=int(input('Enter the value of a: '))
b=int(input('Enter the value of b: '))
c=int(input('Enter the value of c: '))
x=((b*b)-4*a*c)
if x==0:
    print('The equation has two equal roots.')
elif x>0:
    print('The equation has two real roots.')
elif x<0:
    print('The equation has two complex roots.')
else:
    print('Something went wrong.')