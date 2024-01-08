# The break Statement

for number in range(1, 11):
         if number == 4:
                   break
         print (number)
print ("Thanks!")
print("\n")

for x in range (1,11):
    if x%2==0:
        print(x)
print("\n")


# The continue Statement

for number in range(1, 11):
         if number == 4:
                   continue
         print (number)
print ("Thanks again!")
print("\n")
# from line 4, note the resultes here omit the number "4".


# The else Clause

for number in range (1,11):
    if number == 4:
        continue
    print (number)
else:
    print ("Exited normally.")
print ("\n")


for number in range (1,11):
    if number == 4:
        break
    print (number)
else:
    print ("Exited normally.")
print ("\n")


# Example using break:

phrase = input("Enter a phrase: ")
letter = input("Enter a letter:")
length = len(phrase)

for index in range (0,length):
    if phrase [index] == letter:
        break
else:
    print("Your letter wasn't found.")
