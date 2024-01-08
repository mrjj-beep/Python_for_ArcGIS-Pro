import shelve

grades = shelve.open('grades.txt', 'c')
name = input("Please enter student name; Enter -999 to quit: ")

while name != '-999':
    score = eval(input("Please Enter the student's score: "))
    grades [name] = score

    print()
    name = input("Please enter student name; Enter -999 to quit: ")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

search = input("Please enter student's name for score: ")

while search != '-999':
    if search in grades:
        print(search, "\t", grades[search])
    else:
        print(search, "Name not found")

    print()

    search = input("Please enter student's name for score: ")

grades.close()
