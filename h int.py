row=int(input("Enter the number;"))
z=0
i=1
while i<=row:
    j=1
    while j<=row-i:
        print(" ",end='')
        j=j+1
    j=1
    while j<=z:
        print(j,end='')  
        j=j+1
    z=z+1
    print()
    i=i+1         


