
n= int(input("enter the number of elements in dictionary: "))#number of elements in dictionary
dictionary = {}#creating empty dictionary
for i in range(n):#loop to input elements
  keyi = input("enter your key: ")#key input
  valuei = int(input("enter your value: "))#value input
  a = {keyi: valuei}#creating dictionary with key and value
  dictionary.update(a)#updating the main dictionary with new key-value pair
print(dictionary)#displaying the final dictionary
for keys in dictionary:#loop to display the keys in dictionary
  print(keys)#displaying the keys in dictionary