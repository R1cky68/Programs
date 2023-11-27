# This program is a simple word counter that counts words given in a file, it's for a rtf file so it has bonus code here
import re
from striprtf.striprtf import rtf_to_text

# Opening file
filename = input("Enter file name: ")
file = open(filename, "r")

# Read the contents of file
rtf = file.read()
text = rtf_to_text(rtf)

# Counts word number
pattern = re.compile(r'\w+')
matches = pattern.findall(text)
words = len(matches)

print("The file contains", words, "words in it")
print("Matches:", matches)

file.close()