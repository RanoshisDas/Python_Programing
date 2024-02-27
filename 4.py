y=int(input('Enter the year: '))
if y%4==0 and y%100!=0 or y%400==0:
    print(y,'is leap yaer.')
else:
    print(y,'is not leap year.')