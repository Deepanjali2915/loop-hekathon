# current_Number = 1  
# stop = 2  
# rows = 3  # Number of rows to print numbers  
  
# for i in range(rows):  
#     for j in range(1, stop):  
#         print(current_Number, end=' ')  
#         current_Number += 1  
#     print("")  
#     stop += 2  

# i=1
# # a=1
# stop=2
# row=3
# while i<=row:
#     j=1
#     while j>=stop:
#        print(i,end='')
#        j=j+1
#     # i=i+1
#     stop+=2
#     print("")
#     # stop+=2
#     i+=1   



k=1
row=int(input("Enter the number"))
i=1
while i<=row:
   j=1
   while j<=i:
      print(k,end='')
      j+=1
      k+=1
   i+=1
   print()   
