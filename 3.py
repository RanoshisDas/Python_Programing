a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
c=int(input('Enter 3rd number: '))
if a==b and b==c:
    print('You enter same numbers.')
elif a<c and b<c:
    print(c,'is the largest.')
elif b<a and c<a:
    print(a,'is the largest.')
else:
    print(b,'is the ;argest.')