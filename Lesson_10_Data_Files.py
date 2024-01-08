# Create .txt file in write mode (destination same as source code:
out_file = open('mydata.txt', 'w')

# To specify the file destination:
out_file2 = open('C:/Users/MrJoh/OneDrive/Documents/TXST/Python/Lesson 10/mydata2.txt', 'w')


# Write to the file:
out_file2.write('Hello ')
out_file2.write('world!')
out_file2.write('\n')
out_file2.write('\nTime interval is a strange and contradictory matter in the mind. \nIt would be reasonable to suppose that a routine time or an eventless time would seem interminable. \nIt should be so, but it is not. It is the dull eventless times that have no duration whatever. \nA time splashed with interest, wounded with tragedy, crevassed with joy - that is the time that seems long in the memory. \nAnd this is right when you think about it. Eventlessness has no posts to drape duration on. From nothing to nothing is no time at all.')
out_file2.flush( )
out_file2.close( )


#
out_file3 = open('C:/Users/MrJoh/OneDrive/Documents/TXST/Python/Lesson 10/mydata3.txt', 'w')
weekends = ['Saturday', 'Sunday']
out_file3.writelines(weekends)
out_file3.writelines(weekends)
out_file3.flush( )
out_file3.close( )


# Open file for reading ('r'):
in_file2 = open('C:/Users/MrJoh/OneDrive/Documents/TXST/Python/Lesson 10/mydata2.txt','r')
print (in_file2.read())
print()


# to append an existing file:
out_file2 = open('C:/Users/MrJoh/OneDrive/Documents/TXST/Python/Lesson 10/mydata2.txt', 'a')
out_file2.write('\n\nby John Steinbeck')
out_file2.flush( )
out_file2.close( )
in_file2 = open('C:/Users/MrJoh/OneDrive/Documents/TXST/Python/Lesson 10/mydata2.txt','r')
print (in_file2.read(), "\n")


#
out_file4 = open('C:/Users/MrJoh/OneDrive/Documents/TXST/Python/Lesson 10/mydata4.txt', 'w')
out_file4.write('First line\n')
out_file4.write('Second line')
out_file4.flush( )
out_file4.close( )


#
in_file4 = open('C:/Users/MrJoh/OneDrive/Documents/TXST/Python/Lesson 10/mydata4.txt', 'r+')
# print (in_file4.read(1))
# print (in_file4.tell())

print (in_file4.readline())
print (in_file4.tell())

in_file4.seek(0)
print (in_file4.readline())

in_file4.seek(0)


# Example
in_file4 = open('C:/Users/MrJoh/OneDrive/Documents/TXST/Python/Lesson 10/mydata4.txt', 'r+')
print (in_file4.readline())

in_file4.seek(0)
in_file4.write('Hi!')
in_file4.seek(0)
print (in_file4.readline())

in_file4.seek(0)
in_file4.write('Fir')
in_file4.seek(0)

print (in_file4.read())
