#This program aims to sort an array of numbers in ascending or descending order, as inputted by the user
Array = []
Numbers = input ("Please enter some numbers, separate by spaces \n")
Array.entend(map(int, Numbers.split())) # Uses the extend > append method since it's adding multiple elements to the list, need to split them manually otherwise treats them as one element
Array.sort() # sorts the numbers
print(Array)