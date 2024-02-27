#A palindromic number is a number that remains the same when its digits are reversed. For example, 16461. Write a program that prompts the user to input a number and determine whether the number is palindrome or not.
n=int(input('Enter a number:'))
m=0
p=n
while p>0:
    a=p%10
    p=p//10
    m=(m*10)+a
if n==m:
    print("The number is palindrome")
else:
    print("The number is not palindrome")