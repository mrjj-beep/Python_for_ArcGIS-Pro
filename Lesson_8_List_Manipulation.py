My_List = []
My_List.append (10)
My_List.append ('ten')
print (My_List)
print ("\n")

# Function for adding multiple inputs to a list:
My_List.extend ([20, 'twenty'])
print (My_List)
print ("\n")

# Another way to adding inputs to a list:
My_List = My_List + [30, 'thirty']
print (My_List)
print ("\n")

# To insert an item at a specific index in a list:
My_List.insert (0, "Hi there!")
print (My_List)
print ("\n")

# To insert a specific item from a list:
My_List.remove ("Hi there!")
print (My_List)
print ("\n")

# Numeric lists:
my_numbers = [16, 8, 15, 42, 23, 4]
print (max(my_numbers))
print (min(my_numbers))
print ("\n")

my_numbers.sort( )
print (my_numbers)
print ("\n")

my_numbers.reverse( )
print (my_numbers)
print ("\n")
