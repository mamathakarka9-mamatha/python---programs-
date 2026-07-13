#finding the element in the list and returning the index of that element
lst = list(map(int, input("enter your list elements: ").split()))#creating list from user input
element = int(input("enter the required list element to search: "))#enter the element for searching
for i in range(len(lst)):#loop for the length of list
    if element == lst[i]:#checking if the element is present in the list or not 
        print("element is found in the list")#if present displays this message
        break
else:
    print("element is not found in the list")#if not present displays this message 
print("index of the element:", lst.index(element))#displaying the index of the required element