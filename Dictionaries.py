# Dictionaries: use curly brackets, key word is first, colon, then stored value.

days_in_month = {'Jan':31}
print (days_in_month ['Jan'] )

days_in_month = {'Jan':31,
                 'Feb':28,
                 'Mar':31}
print (days_in_month)

# Remember, the dictionary is an unordered list. So input inoformationmay not be output in the same order.

print (days_in_month.keys())
print (days_in_month.values())
print (days_in_month.items())

# To add to a ictionary, is list the dictionary name with the key inside square brackets,
# an equal sign, and the value you want stored:

days_in_month ['Apr'] = 20
print (days_in_month.items())

# To make correction, use same syntax:
days_in_month ['Apr'] = 30
print (days_in_month.items())

# To add one dictionary to another:
days_in_month2 = {'May':31, 'Jun':30, 'Jul':31}
days_in_month.update(days_in_month2)
print (days_in_month.keys())

print (days_in_month2.keys())

# To delete items from a dictionary:
del days_in_month ['Apr']
print (days_in_month.items())

# To remove all of the items in your dictionary:
odds = {1:'one', 3:'three', 5:'five'}
evens = {2:'two', 4:'four', 6:'six'}
odds.clear()
print (odds)

# To delete your dictionary:
# del evens
print (evens)

# If key is not found in dictionary, get() command will return 'None',
# as opposed to an KeyError message crashing your program: 
print (days_in_month.get('January'))

# Or change message from 'None' to desired message:
print (days_in_month.get('January', 'January not present'))

# Example:

words = {}
value = input('Please enter a word (or -999 to quit): ')
while (value != '-999'):
    if value in words:
        words [value] = words [value] + 1
    else:
        words [value] = 1

    value = input("Please enter a word (or -999 to quit): ")

print('\n')

for current_key in words.keys():
    print(current_key, '\t', words [current_key])

print('\n')

# To ensure output is in alphabetical order:
my_keys = list(words.keys())
my_keys.sort()
for current_key in my_keys:
    print(current_key, '\t', words [current_key])

print('\n')

# 

temp_list = []
# Select a key in the dictionary
for current_key in words.keys():
   # determine the number of words in the sorted list
   list_length = len(temp_list)

   # start looking at position 0
   placeholder = 0

   # As long as there are still items in the list
   while placeholder < list_length:

       # Get the word in the sorted list
       list_key = temp_list [placeholder]

       # Determine if this word has been entered
       # more times than the current word
       if words [list_key] > words [current_key] :
           break

       # It wasn't, so let's look at the next word
       # in the sorted list
       placeholder = placeholder + 1

   # We found the location in the sorted list for
   # this word, insert it
   temp_list.insert(placeholder, current_key)

for current_key in temp_list:
   print (current_key, '\t', words [current_key] )
