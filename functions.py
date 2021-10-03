import sys
database = {'ameen':'dave2','mariya':'parantha61', 'ajeel': 'paranthawala64',
            }
options = {"quit": 0, "open account": 1, "view account": 2, "open committee": 3,
           "calculate contributions": 4, "view credit scores": 5,
           }

def login():
    """Logs the user in, and returns true once password matches"""
    username = input('Enter username: ')
    if username in database.keys(): ## check if username is in database
        while True:
            password = input('Enter password: ')
            if password in database[username]: #checks if password matches
                print("Welcome " + str(username) + ".")
                return True
            else:
                print('Invalid password. Please try again.')
                continue
    else:
        print("Username does not exist. Please create a user.")

def create_user():
    """Add's a user to the database."""
    while True:
        username = input("Please input a username: ")
        if username in database.keys():
            print("Sorry that username is already taken. "
                  "\nPlease choose another one")
            continue
        else:
            break
    password = input("Please input your password: ")
    database.update({username:password})
    print("Account created.")

def get_option():

    while True:
        selection = input("Please input one of the options: ")
        if selection not in options.keys():
            print("Sorry, that option doesn't look correct. Please try again")
            continue
        else:
            return options[selection]

def director(selected):
    """Directs the program to the correct function."""
    if selected == 0:
        sys.exit()
    elif selected == 1:
        create_user()
    elif selected == 2:
        view_account() #need to complete
    elif selected == 3:
        open_committee() #need to complete
    elif selected == 4:
        calculate_contributions() #need to complete
    elif selected == 5:
        view_scores() #need to complete











