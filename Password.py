import random
Length = int(input("Enter number of characters for password \n"))
Password = []

for i in range (Length):
   Char = chr(random.randint(33, 126))
   Password.append(Char)

Password_string = ''.join(Password) 
print(Password_string)