number_list = []
sum = 0.0

user_number = eval(input("Please enter a number (-999 quits): "))

while (user_number != -999):
    number_list.append(user_number)
    sum = sum + user_number
    user_number = eval(input("Please enter a number (-999 quits): "))

if (len(number_list) != 0):
    average = sum / len(number_list)

    print ("Using the numbers:")

    for i in range(len(number_list)):
        print (number_list[i], end = " ")

    print ("\nThe average is:", average)
else:
    print ("No values were entered")
