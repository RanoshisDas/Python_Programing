#Write a program that prompts the user to input a decimal integer and display its binary equivalent.
n=int(input('Enter a number:'))
b=0
print('The binary of',n,'is=',end='')
while n>0:
    i=0
    for i in range(64):
        p=2**i
        if p>n:
            n=n-(p/2)
            b=b+(10**(i-1))
            break
print(b)