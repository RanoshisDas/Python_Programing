#Write a program that asks the user for a positive integer value. 
#The program should calculate the sum of all the integers from 1 up to the number entered. 
#For example, if the user enters 20, the loop will find the sum of 1, 2, 3, 4, ... 20
n=int(input('Enter a positive number:'))
s=0
if n>0:
    for i in range(n+1):
        s=s+i
    print('The total sum is= ',s)
else:
    print('Enter positive value.')