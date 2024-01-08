# In terms of scripting an "Input Error", here is something (one of many, many ways to do it) that you could try


good_input = False

while good_input == False:
    n = input("Enter a number: ")
    if n.isnumeric():
        n = eval(n)
        good_input = True
    else:
        print("Input Error")
