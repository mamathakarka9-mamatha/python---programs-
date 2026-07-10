#finding second largest number in a list
def secondlargest(name):#defining function
 result=[]#creating empty list to store the second largest number
 if len(name) <= 1:#checking if the length of the list is less than or equal to 1
  return "no second largest number"#displaying message if the length of the list is less than or equal to 1
 name.sort(reverse=True)#sorting the list in descending order
 for i in range(len(name)-1):#iterating through the list
      if name[i] != name[i+1]: #checking if the current element is not equal to the next element
       return name[i+1]#returning the second largest number
 return "no second largest number"#displaying message if there is no second largest number
name= list(map(int, input("enter the list elements: ").split()))#taking input from the user and converting it into a list of integers
print(secondlargest(name))#displaying the second largest number in the list