



# rows = int(input("Enter the number of rows: "))  
# # Downward loop for inverse loop  
# for i in range(rows, 0, -1):  
#     n = i   # assign value to n of i after each iteration  
#     for j in range(0, i):  
#         # print reduced value in each new line  
#         print(n, end=' ')  
#     print("\r")  


row=int(input("Enter the number"))
i=6
while i>=row:
    n=i
    j=0
    while j<i:
        print(n,end='')
        j=j+1
    i=i-1
    print()    