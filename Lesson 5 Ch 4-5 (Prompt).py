def prompt_user(prompt, num_tries = 6):
    """This function prompts the user a certain number of times"""
    answer = input(prompt)

    while (answer != "yes" and answer != "no" and num_tries > 1):
       num_tries = num_tries - 1
       print ("Try again")
       answer = input(prompt)

prompt_user("Enter yes or no: ", 6)
