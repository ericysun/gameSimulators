def rot13(inputChar):
  
  number = ord(inputChar)
  if number >=65 and number <=90:
    offset=65
  elif number >=97 and number <=122:
    offset=97
  else:
    return inputChar
  
  number=number-offset
  number = (number+13)%26
  number = number+offset
  return chr(number)
  

a = str(input("What phrase would you like to put through the rot13 cipher?\n"))
b = ""
for i in range(len(a)):
  b = b + str(rot13(a[i]))
print("Rot13 Encrypted Phrase: "+b)
