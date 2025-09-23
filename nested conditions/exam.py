medicalcause=str(input("did you have a medical cause"))
attendance=int(input("enter the attendance of the student"))
if medicalcause=="yes":
 print("you are allowed")
else:
 if attendance>=75:
  print("you are allowed")
 else:
  print("you are not allowed")