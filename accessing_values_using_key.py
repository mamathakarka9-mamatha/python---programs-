#accessing values using key in dictionary
n= int(input("enter the number of elements in dictionary: "))#number of elements in dictionary
dictionary = {}#creating empty dictionary
for i in range(n):#loop to input elements
  keyi = input("enter your keyi: ")#key input
  valuei = int(input("enter your valuei: "))#value input
  a = {keyi: valuei}#creating dictionary with key and value
  dictionary.update(a)#updating the main dictionary with new key-value pair
b = input("enter the required key to access the value: ")#key to access the value
print(dictionary.get(b))#displaying the value of the required key