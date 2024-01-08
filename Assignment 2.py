# Introduction to Python Programming
# Lesson 02 Assignment
# Sample Solution

# Quote: Time interval is a strange and contradictory matter in the mind. It would be reasonable to suppose that a routine time or an eventless time would seem interminable. It should be so, but it is not. It is the dull eventless times that have no duration whatever. A time splashed with interest, wounded with tragedy, crevassed with joy - that's the time that seems long in the memory. And this is right when you think about it. Eventlessness has no posts to drape duration on. From nothing to nothing is no time at all.

import math

# Get quote from user
Quote = input('What is your favorite quote? ')

# Now get starting and ending positions
startNum = eval(input("Please enter the starting position: "))
endNum = eval(input("Please enter the ending position: "))

# Finally print out the slice
print (Quote[startNum:endNum+1])

# NOTE: Some may want to show the character at the last position
# to the user.  In that case, the above print statement would be:
print (Quote[len(Quote)-1:len(Quote)])

print (Quote, '\n')
print (len(Quote),'\n')
print (Quote[:64])


# Determine where to divide the phrase in half (rounded down)
Quote_length = len(Quote)
mid_point = math.floor(Quote_length/2)

# Obtain two numbers from an upper and lower range from user
nmb1 = eval(input("Enter a number between 0 and " + str(mid_point) +  " >>> "))
nmb2 = eval(input("Enter a number between " + str(mid_point) + " and " + str(Quote_length) + " >>> "))

# Print sliced phrase based upon the provided numbers
print (Quote[nmb1:nmb2])
