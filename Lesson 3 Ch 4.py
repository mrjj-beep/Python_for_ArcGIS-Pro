# Logic Operators

age = eval(input("How old are you? "))
registered = input("Are you registered? (y/n) ")

# if age >= 18:
#    if registered == "y":
#        print ("You are ready to vote.")
#    else:
#        print ("You are NOT ready to vote.")

# Above is a NoGo.

if age >= 18 and registered == "y" or "Y":
        print ("\nYou are ready to vote.\n")
else:
        print ("\nYou are NOT ready to vote.\n")


# Pay Calculation:

rate = eval(input("Enter rate of pay: "))
hours = eval(input("Enter number of hours worked: "))

if hours <= 40:
    pay = rate * hours
else:
    pay = rate * hours
    OvertimeHours = hours - 40
    OvertimePay = OvertimeHours * (rate * 0.5)
    pay = pay + OvertimePay

print ("Your weekly pay is: ", pay)
    
