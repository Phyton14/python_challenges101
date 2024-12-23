#   program that checks whether a pH level is basic, acidic, or neutral.

#create a ph variable and ask the user for a value between 0 and 14.

ph = int(input('Enter the value(0 to 14): '))

#statement that:
#If ph is greater than 7, output "Basic".

if(ph > 7):
  print("Basic.")
#If ph is less than 7, output "Acidic".

elif(ph < 7):
  print("Acidic.")

#Else, output "Neutral".

else:
  print("Neutral")

print(ph)
