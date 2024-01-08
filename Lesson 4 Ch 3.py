# Ch 3

for x in range (1,36):
    print (x)
print ("\n")

for number in range(6):
    print (number)
print ("\n")


# Placing a third digit in the range yields an increment

for y in range(25,100,6):
    print (y)
print ("\n")

# Using a negative number reverses the string direction.

for z in range(100,24,-5):
    print (z)
print ("\n")

# Average selected numbers

x = eval(input("Enter the number of values you wish to average: "))
sum = 0.0

for count in range (x):
    value = eval(input("Enter a value "))
    sum = sum + value

average = sum / x
print ("The averge is: ", average)
print ("\n")


# Note the actual range is irrelevant because the user is selecting the numbers.

x = eval(input("Enter the number of values you wish to average: "))
sum = 0.0

for count in range (x, 0, -1):
    value = eval(input("Enter a value "))
    sum = sum + value

average = sum / x
print ("The averge is: ", average)
