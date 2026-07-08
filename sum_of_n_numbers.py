#sum of n numbers 
n = int(input("enter your number: ")) #by using type casting input string is considered as integer
total = 0 #initially, the  total is zero 
for i in range(1,n+1):#loop from 1 to n
     total = total + i #add each number to the total 
print("total: ", total) # display output
    
