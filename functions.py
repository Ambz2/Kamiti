import sys
import json
from datetime import datetime
import random


database = {}
options = {"quit": 0, "open account": 1, "view account": 2, "open committee": 3,
           "calculate contributions": 4, "view credit scores": 5,
           }

def login():  ##NEEDS TO BE REFORMULATED
    """Logs the user in, and returns true once password matches"""
    login_name = input('Enter username: ')
    ## Open's JSON dictionary and loads it into python.
    data = open_database()
    if login_name in data.keys(): ## check if username is in database
        while True:
            password = input('Enter password: ')
            if password in data[login_name]['password']: #checks if password matches
                print("Welcome " + str(login_name) + ".")
                return True
            else:
                print('Invalid password. Please try again.')
                continue
    else:
        print("Username does not exist. Please create a user.")

def create_user():
    """Add's a user to the database."""
    data = open_database()
    username = username_chooser(data)
    password = input("Please input a password: ")
    first_name = input("Please input your first name: ")
    last_name = input("Please input your last name: ")
    dob = input("Please input your date of birth: ")
    write_to_database(username, password, first_name, last_name, dob, data)

    print("Account created.")

def username_chooser(data):
    while True:
        username = input("Please input a username: ")
        if username in data.keys():
            print("Sorry, that is already in use. \nPlease choose another.")
            continue
        else:
            break
    return username

def open_database():
    """Opens up the database"""
    with open("database.json","r") as file:
        data = json.load(file)
    return data

def write_to_database(username, password, first_name, last_name, dob, data):
    """Writes the username to the database"""
    data = open_database()
    database[username] = {}
    database[username]["password"] = password
    database[username]["first_name"] = first_name
    database[username]["last_name"] = last_name
    database[username]["DOB"] = dob
    database[username]["Account_Creation_Date"] = get_creation_date()
    database[username]["ID_Number"] = id_generator(data)
    with open("database.json", "r+") as file:
        data = json.load(file)
        data.update(database)
        file.seek(0)
        json.dump(data, file, indent=4, sort_keys = True, default=str)

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

def get_creation_date():
    """Returns the date when the account was created."""
    current_datetime = datetime.now().date()
    return current_datetime

def id_generator(data):
    """Generates an id number for each user using a random int
    which is then compared to other users"""
    print(data)
    while True:
        id_number = random.randint(1, 4)
        for dictionary in data:
            if str(id_number) not in dictionary:
                return id_number
                break
            else:
                continue
def view_account(data, login_name):
    """Allows the user to view their own account once they have logged in."""
    print(data[login_name])


#def open_committee():


#def calculate_contributions():


#def view_scores():









