# This is a simple program that stores a number and tells you what it is, you can then manipulate it and it'll show you the updated one
import random
print("Input a number: ")

number = input()
print("Would you like to modify the number?")
path = input()

if (path == "Yes"):
   print("What would you like to modify? Clone, Double, Square, Delete or Randomise?")

else:
    print("Ok, this is the number then:", number)

choice = input()
if (choice == "Clone"):
        print(number, " ", number)
elif (choice == "Double"):
        number = int (number) * 2
        print(number)
elif (choice == "Square"): 
        number = int (number) * int (number)
        print(number) 
elif (choice == "Delete"):
      number = 0
      print(f"{number}, Cleared now")
elif (choice == "Randomise"):
      print(random.randint(0,100))

else:
    print("Let's just stick with this:", number)