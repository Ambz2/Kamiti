import json
from operations import *
welcome = "Welcome to Kamiti Money Manager."

options = {"quit": 0, "open account": 1, "view account": 2, "open committee": 3,
           "calculate contributions": 4, "view credit scores": 5,
           }


print(welcome)
print("Do you already have an account?")
has_account = input("Please enter Yes or No: ")
logged_in = [False, ""]
if has_account.lower() == 'yes': ## if they have an account, they will need to log in
    print("Please log into our systems.")
    logged_in = login()
else:
    print("Please sign up for an account to continue.")
    create_user()


while True:
    if logged_in[0]:
        print("Please select one of the following options:")
        for option in options.keys():
            print("\t" + option.title())


        selected = get_option()
        director(selected)
    else:
        logged_in = login()
## need to rewrite the above code into a function which converts the entry into a
## number and then send us the right way



