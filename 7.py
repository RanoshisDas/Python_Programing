a=int(input('Marks for 1st subject: '))
b=int(input('Marks for 2nd subject: '))
c=int(input('Marks for 3rd subject: '))
if 0<a<=100 and 0<b<=100 and 0<c<=100:
    av=(a+b+c)/3
    print('Your average is:',av)
    if av>=0 and av<60:
        print('Grade is "F".')
    elif av>=60 and av<69:
        print('Grade is "D".')
    elif av>=70 and av<79:
        print('Grade is "C".')
    elif av>=80 and av<89:
        print('Grade is "B".')
    elif av>=90:
        print('Grade is "A".')
else:
    print('Check your numbers again.')