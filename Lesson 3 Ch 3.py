age = eval(input("Input your age: "))
             
if age >= 18:
    print ("Congratulations!", end = " ")
    print ("You are old enough to vote.", '\n')
else:
    print ("Sorry!", end = " ")
    print ("You are not old enough to vote.", '\n')

    
year = eval(input("Enter year of High School (1 thru 4): "))

if year == 1:
    print ("Freshman\n")
if year == 2:
    print ("Sophomore\n")
if year == 3:
    print ("Junior\n")
if year == 4:
    print ("Senior\n")


# Nested Statements

year = eval(input("Enter year of High School (1 thru 4): "))

if year == 1:
    print ("Freshman\n")
else:
    if year == 2:
        print ("Sophomore\n")
    else:
        if year == 3:
            print ("Junior\n")
        else:
            if year == 4:
                print ("Senior\n")
            else:
                print ("Invalid input, Dumb Ass!\n")


# The elif Statement

year = eval(input("Enter year of High School (1 thru 4): "))

if year == 1:
    print ("Freshman\n")
elif year == 2:
    print ("Sophomore\n")
elif year == 3:
    print ("Junior\n")
elif year == 4:
    print ("Senior\n")
else:
    print ("Invalid input, Numb Nuts!\n")
