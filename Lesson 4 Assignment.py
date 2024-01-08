# Write a program that reads in a list of numbers from the users and displays
# the sum and average of this list. Your program should allow the users to
# enter as many numbers as they wish. When the users are finished entering
# numbers, they'll enter the value -1. Be sure not to include the -1 in your
# calculations for the sum and average.

count = 0
sum = 0.0
value = eval(input("Please enter a number (-1 quits): "))

while (value != -1):
    sum = sum + value
    count = count + 1

    value = eval(input("Please enter a number (-1 quits): "))

# This is necessary, in case the user doesn't enter any values
if (count != 0):
    average = sum / count

print ("The sum of these numbers is", sum)
print ("The average of these numbers is", average)
