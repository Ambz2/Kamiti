database = {'ameen':'dave2','mariya':'parantha61', 'ajeel': 'paranthawala64',
            }

def login():
    """Logins in the user, and returns true once password matches"""
    username = input('Enter username: ')
    if username in database.keys(): ## check if username is in database
        while True:
            password = input('Enter password: ')
            if password in database[username]: #checks if password matches
                print("Welcome " + str(username) + ".")
                return True
            else:
                print('Invalid code. Please try again.')
                continue
    else:
        print("Username does not exist. Please create a user.")

