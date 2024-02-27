c=""
c=input('Enter One character:')
if len(c)==1:
    if c=='a'or c=='e' or c=='i'or c=='o'or c=='u':
     print('This  character is vowel.')
    elif c=='A'or c=='E' or c=='I'or c=='O'or c=='U':
        print('This  character is vowel.')
    else:
        print('This  character is consonant.')
else:
   print('you entered more then one charactor.')