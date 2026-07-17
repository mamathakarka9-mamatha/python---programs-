#creating a set from user input and checking whether that set contains any elements or not and printing all elements from set 
s = set(input("Enter the elements of the set: ").split())#taking input from user  
if len(s)==0:#checking the length of the set
    print("given set is a empty: ", s)#displays this message if length of the list is zero
elif len(s)!=0:#checking the length of the set
    print("given set contains: ", s)#displays this message if length of the list is not equal to zero