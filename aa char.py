# print("The character pattern ")  
# asciiValue = 65     #ASCII value of A  
# for i in range(0, 5):  
#     for j in range(0, i + 1):  
#         # It will convert the ASCII value to the character  
#         alphabate = chr(asciiValue)  
#         print(alphabate, end=' ')  
#         asciiValue += 1  
#     print() 





a=65
i=0
row=int(input("Enter the number"))
while i<=row:
    j=0
    alpha=chr(a)
    while j<=i:
        print(alpha,end='')
        j+=1
    a+=1
    i+=1
    print()    
            