import math
# '\t' = tab
# '\n' = new line
print ('1\t2\n3\n')

print ('The value of Pi is ', math.pi,'\n')

print(10**6)
print (math.pow(10,6), '\n')

print ('New ' + 'York')
print ('and over ' * 3,'\n')

word = 'My words are important!'
print (word)
print (len(word),'\n')

# There are also functions that let you search a string for a particular
# substring (find), break strings into substrings (split), remove white
# space from the ends of your string (strip), tell if the letters are
# uppercase (isupper), or convert all letters to lowercase (lower).

# indexing and slicing
phrase = "Python rocks"
# phrase = "P,y,t,h,o,n, ,r,o,c,k,s"
# phrase = "0,1,2,3,4,5,6,7,8,9,10,11"
# Note the last digit in the slice is not included in the string.
print (phrase [0])
print (phrase [7])
print (phrase [1:3])
# print "rock"
print (phrase [7:11])
print (phrase [:6])
print (phrase [7:])

phrase = 'p' + phrase [1:]
print (phrase)

value1 = 1
value2 = 2
print(value1, end=" ")
print(value2)
# Gives you 1 2 on the same line.


