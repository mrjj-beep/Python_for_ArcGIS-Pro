# Write a Python program that will print a table of Celsius
# temperatures and their Fahrenheit equivalents between 0 and 100
# Celsius in increments of 10 degrees. Your program should include
# a function named, convert_to_fahrenheit that takes a Celsius
# temperature and returns the corresponding Fahrenheit temperature.

# Fahrenheit = 9.0/5.0 * Celsius + 32

def C_to_F (celcius):
    """This function converts a C temp to a F temp"""
    F = celcius *(9.0/5.0) + 32
    return F

for C in range(0,101,10):
    print (C, " deg Celcius = \t", C_to_F(C), " deg Fahrenheit")
