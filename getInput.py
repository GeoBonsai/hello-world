##getInput.py
##Simple Python script that demonstrates 
##elementary command-line commands
import sys
import os 
os.system('CLS')

str = "Demo of elementary Python commands"
message = "\nYou typed "
##print("Enter text: ", end='')
print("Please type something (press Enter when done): ", end='')
input_line = sys.stdin.readline().rstrip()
##input_line = input_line.rstrip()
print(message + '\"' + input_line + '\"')
print("\n" + str + "\n")


