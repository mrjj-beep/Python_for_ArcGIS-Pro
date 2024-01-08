def print_names(value):
    """This function prints the value passed in"""
    print("The Guetlist is: ", value)

def change_value(value):
    """This function changes the value passed in to 1"""
    print ("Inside, value is:", value)
    value = 1
    print ("Inside, value is changed to:", value)

def change_number():
    """This function changes the value passed in to 1 (global)"""
    global number
    number = 1

number = 5
print ("Outside, number is:", number)
change_number()
print ("Outside, number is now:", number)

