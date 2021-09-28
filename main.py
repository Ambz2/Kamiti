import functions
import sys

welcome = "Welcome to Kamiti Money Manager."

options = ["open account", "view account", "open committee",
           "calculate contributions", "view credit scores", "quit"
            ]
database = {'ameen':'dave2','mariya':'parantha61', 'ajeel': 'paranthawala64',
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




print("Please select one of the following options:")
for option in options:
    print("\t" + option.title())

while True:
    selection = input("Please input one of the following options: ")
    if selection.lower() not in options:
        print("Sorry, that's not a valid option, please try again")
        continue
    else:
        break
if selection.lower() == options[0]:
    print("Okay, let's open an account.")
elif selection.lower() == options[1]:
    print("Opening your account now.")
elif selection.lower() == options[2]:
    print("Opening committee management suite now.")
elif selection.lower() == options[3]:
    print("Taking you to the calculator now.")
elif selection.lower() == options[4]:
    print("Opening credit score management suite now.")
elif selection.lower() == options[-1]:
    print("Thank you for using the Kamiti Money Manager")
    sys.exit()

## need to rewrite the above code into a function which converts the entry into a
## number and then send us the right way



