#char count without the space
s=input("Enter your String: ")
c=0
for i in s:
  if i==" ":
      pass
  else:
      c+=1
      
print("Total char without space: ",c)
print("Total Space: ",len(s)-c)
