import functions
import json

welcome = "Welcome to Kamiti Money Manager."

options = {"quit": 0, "open account": 1, "view account": 2, "open committee": 3,
           "calculate contributions": 4, "view credit scores": 5,
           }


print(welcome)
print("Do you already have an account?")
has_account = input("Please enter Yes or No: ")

if has_account.lower() == 'yes': ## if they have an account, they will need to log in
    while True:
        print("Please log into our systems.")
        access_granted = functions.login()
        if access_granted == True:
            break
else:
    print("Please sign up for an account to continue.")
    functions.create_user()



while True:
    print("Please select one of the following options:")
    for option in options.keys():
        print("\t" + option.title())


    selected = functions.get_option()
    functions.director(selected)

## need to rewrite the above code into a function which converts the entry into a
## number and then send us the right way



