#Write a program that prompts the user to input a positive integer. It should then output a message indicating whether the number is a prime number. A prime number is a number that is evenly divisible only by itself and 1. 
#For example, the number 5 is prime because it can be evenly divided only by 1 and 5. The number 6, however, is not prime because it can be divided evenly by 1, 2, 3, and 6
n=int(input('Enter a positive number:'))
p=0
for i in range(2,n//2):
    if n%i==0:
        p=1
#checking the number is negative or zero.
if n<=0:
   print('you entered zero or negative number.')
#checking flag 'p' if it changes then number is not a prime number.
elif p==1:
  print('The number not prime number.')
else:
   print('The number is prime number.')