#Two numbers are entered through the keyboard. 
#Write a program to find the value of one number raised to the power of another.
n=int(input('Enter a number:'))
p=int(input('Enter the power:'))
m=1
for i in range(p):
    m=m*n
print(m)