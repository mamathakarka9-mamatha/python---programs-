#finding average of the list elements 
lst = list(map(int, input("enter your list elements: ").split()))#creating list from user input
sum = 0#initializing sum variable
i = 0#index variable
while i < (len(lst)):#looping through the list to find sum of elements
    sum = sum + lst[i]#sum of elements
    i += 1 #incrementing index variable
average = sum / len(lst)#calculating average
print(average)#displaying average of the list elements