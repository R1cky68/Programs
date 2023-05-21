import os
import re
from striprtf.striprtf import rtf_to_text

filename = input("Enter name of writing: ")

if os.path.exists(filename):
    print("File already exists, writing to existing one..")
    with open(filename,'w') as file:
        text = input("Enter desired text into file: ")
        file.write(text)

else:
    print("File does not exist, creating new one: ")
    with open(filename,'w') as file:
        text = input("Enter desired text into file: ")
        file.write(text)

print("Text is written successfully!")