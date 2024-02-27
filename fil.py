li=[]

#Display functions 
def display():
    if len(li)==0:
        print("\nlist is empty.")
    else:
        print("\nThe list is: ",li,"\nThe leanth of the list is: ",len(li))
        print('The maximum element: ',max(li),'\nThe minimum element: ',min(li),'\nsum of every element: ',sum(li))
#Enter data function        
def enter():
    print("\n1.Add element at specific position\n2.Add element at last\n3.Add element at first")
    d=int(input('Enter choice:'))

    if d==1:
        d=int(input('\nEnter the position(1 for first element):'))
        if d>len(li)+1:
           print("You don't have",d,"th element.\nMaximum element is",len(li))
           return
        li.insert(d-1,int(input("Enter element:")))

    elif d==2:
        d=int(input('\nEnetr the element:'))
        li.append(d)

    elif d==3:
        d=int(input('\nEnter the element:'))
        li.insert(0,d)
        
    else:
        print('\n\t!!!wrong choice!!!\n\t(Returning to main program)')
#Delete data function    
def delete():
    if len(li)==0:
        print("\nlist is empty.")
    else:
        print("\n1.Delete specific element\n2.Delete specific position's element\n3.Delete last element\n4.Delete first element")
        d=int(input('Enter choice:'))

        if d==1:
            d=int(input('\nThe element you want to delete: '))
            li.remove(d)

        elif d==2:
            d=int(input('\nEnter the position:'))
            print('\nThe element',li[d],'is deleted.')
            li.remove(li[d])

        elif d==3:
            print("\nlast element ",li.pop() ,"is deleted.")

        elif d==4:
            print('\nThe element',li[0],'is deleted.')
            li.remove(li[0])

        else:
            print('\n\t!!!wrong choice!!!\n\t(Returning to main program)')
            
#Main Program   
x=0
while x==0:
    print('\n1. Data Enter \n2. Delete an element \n3. Display Data \n4. Exit')
    c=int(input('Enter your choice: '))

    if c==1:
        enter()

    elif c==2:
        delete()
    
    elif c==3:
        display()
    
    elif c==4:
        x=1
    
    else:
        print('\n\t!!!wrong choice!!!\n\t(Returning to main program)')   
        