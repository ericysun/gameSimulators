import time

def wopr():
  #defineFunction=input()
  #defineFunction=defineFunction.lower()
  #if defineFunction=="help games":
  #  print("GAMES REFERS TO MODELS SIMULATIONS AND GAMES WHICH HAVE TACTICAL AND STRATEGIC APPLICATIONS")

  input1 = input("GREETING, PROFESSOR FALKEN.\n")
  if isinstance(input1, str):
    input2 = input("\nHOW ARE YOU FEELING TODAY?\n")
  if isinstance(input2, str):
    input2 = input("\nEXCELLENT. IT'S BEEN A LONG TIME, CAN YOU EXPLAIN THE REMOVAL OF YOUR USER ACCOUNT ON 6/23/73?\n")
  
  input3 = input("\nYES THEY DO. SHALL WE PLAY A GAME?\n")
  input3=input3.lower()
  if input3!='chess':
    input4= input("\nWOULDN'T YOU PREFER A NICE GAME OF CHESS?\n")
  inputList=(str(input4))
  inputList=inputList.split()
  warCounter=0
  for item in inputList:
    item=item.lower()
    if item in ["global","thermonuclear","war"]:
      warCounter+=1
  if warCounter>2:
    print("\nFine.\n")

  print("\nUNITED STATES         SOVIET UNION\n\nWHICH SIDE DO YOU WANT?\n1. UNITED STATES\n2. SOVIET UNION")
  strikeTarget=None
  
  while True:
    input5=input("PLEASE CHOOSE ONE.\n")
    if input5=="1":
      strikeTarget="SOVIET UNION"
      break
    elif input5=="2":
      strikeTarget="UNITED STATES"
      break
    else:
      print("Enter 1 or 2.")
  print("\u0332".join("\nAWAITING FIRST STRIKE COMMAND "))
  print("PLEASE LIST PRIMARY TARGETS BY CITY AND/OR COUNTY NAME\n")
wopr()
