i=0
k=0
row=int(input("Enter the number"))
while i<=row:
    j=1
    while j<=row-i:
        print(" ",end='')
        j=j+1
    j=0
    while j<=k:
        print("*",end='')
        j=j+1
    k=k+2
    print()  
    i=i+1    
    a=0
    while a<=i+1        :
        print("*",end='')
    a=a+1
    print("")    




row=int(input("Enter the number;"))
z=0
i=0
while i<=row:
    j=1
    while j<=row-i:
        print(" ",end='')
        j=j+1
    j=0
    while j<=z:
        print(i,end='')
        j=j+1
    z=z+2
    print()
    i=i+1         
  