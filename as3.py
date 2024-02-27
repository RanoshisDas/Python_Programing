#Write a program that prompts the user to input a number and prints its mulitiplication table.
n=int(input('Enter a positive number:'))
m=0
if n>0:
    for i in range(1,11):
        m=n*i
        print(i,'*',n,'=',m)
else:
    print('Enter positive value.')