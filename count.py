print('########Counting by 2s#######')
myName = input('What is your name? ').capitalize()

while (myName == "" or len(myName) >20 or len(myName) <3):
	print("Name must be filled or name must not be greater than 20 or less than 3")
	myName = input('What is your name? ').capitalize()

import string
invalidChars = set(string.punctuation.replace("_",""))
while any(char in invalidChars for char in myName):
	print("Invalid! Please enter letters only")
	myName = input('What is your name? ').capitalize()

while myName.isalpha() == False:
	print("That is definitely not your name")
	myName = input('What is your name? ').capitalize()

print("Hello " + myName)
		
endNum = input('Enter a number:')

while endNum=="" or endNum.isnumeric()== False or int(endNum) > 100 or int(endNum) < 3:
	if endNum == "":
		endNum = input("Please don't leave it blank and type a number:")
	elif endNum.isnumeric() == False:
		endNum = input("Please! Do not type anything except numbers")
	elif int(endNum) < 3 or int(endNum) > 100:
		endNum = input("You should enter a number greater than 3 or less than 100")
		endNum = int(endNum)

input('Counting to ' +str(endNum) + '-press Enter to start: ')
endNum = int(endNum)
if endNum % 2 == 0: #even
		z=0
else: #odd
		z=1
for x in range(z, endNum + 1, 2):
    
     print (x)

print('Done!')



