# Introduction to Python Programming
# Lesson 11 Assignment
# Sample Solution

try:
    counter = 1
    while (counter >= 1):
        # This code simply prints the number and
        #   is for debugging purposes
        print (counter)

        # A second set of code
        # This code will raise 2^counter
        result = 2.0 ** counter

        # I used the following line for debugging
        #   purposes for the second case
        print ("2 ^", counter, "=\t", result)

        counter = counter + .001
except OverflowError:
    print ("\n\nOverflowError: You stopped the program with counter =", counter)

except KeyboardInterrupt:
    print ("\n\nKeyboardInterrupt: You stopped the program with counter =", counter)

    # This is the output I used for the 2^number code
    #print ("\n\nKeyboardInterrupt: You stopped the program with result =", result)
