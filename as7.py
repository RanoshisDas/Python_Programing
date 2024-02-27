#Write a program that asks the user to input a positive integer. Your program should find and display the sum of digits of number. For example, sum of digits of number 32518 is 3+2+5+1+8 = 19
n=int(input('Enter a number:'))
sum=0
while n>0:
    a=n%10
    n=n//10
    sum=sum+a
print('sum Total of the digits is= ',sum)