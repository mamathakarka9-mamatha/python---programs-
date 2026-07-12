#checking if required key exists in the required dictionary
n= int(input("enter the number of elements in dictionary: "))#number of elements in dictionary
dictionary = {}#creating empty dictionary
for i in range(n):#loop to input elements
  keyi = input("enter your key: ")#key input
  valuei = int(input("enter your value: "))#value input
  a = {keyi: valuei}#creating dictionary with key and value
  dictionary.update(a)#updating the main dictionary with new key-value pair
print(dictionary)#displaying the final dictionary
key = input("enter the key to search: ")
if key in dictionary:#checking if required key is present in the dictionary
  print("required key present in the dictionary")#display if required is present in the dictionary
else:
  print("required key is not present in the dictionary")#display if required key is not present in the dictionary