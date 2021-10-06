import sys
import json
from datetime import datetime
import random

options = {"quit": 0, "view account": 1, "open committee": 2,
           "calculate contributions": 3, "view credit scores": 4
           }

def login():
    notlogin = True
    while notlogin:
        login_name = input("Please enter your username: ")
        password = input("Please enter your password: ")
        data = open_database()
        if login_name in data.keys():
            if data[login_name]["password"] == password:
                notlogin = False
                print("Log in successful. Welcome back " + login_name + ".")
                return [True, login_name]


            else:
                print("Username or password incorrect. Please try again.")
        else:
            print("Username or password incorrect. Please try again.")

def open_database():
    """Opens up the database"""
    with open("database.json","r") as file:
        data = json.load(file)
    return data


def create_user():
    """Add's a user to the database."""
    data = open_database()
    username = username_checker(data)
    password = input("Please input a password: ")
    first_name = input("Please input your first name: ")
    last_name = input("Please input your last name: ")
    dob = input("Please input your date of birth: ")
    write_to_database(username, password, first_name, last_name, dob, data)

    print("Account created.")

def create_new_user():
    """Add's a user to the database."""
    data = open_database()
    username = username_checker(data)
    password = input("Please input a password: ")
    first_name = input("Please input your first name: ")
    last_name = input("Please input your last name: ")
    dob = input("Please input your date of birth: ")
    write_to_database(username, password, first_name, last_name, dob, data)

    print("Account created.")


def write_to_database(username, password, first_name, last_name, dob, data):
    """Writes the username to the database"""

    data[username] = {}
    data[username]["password"] = password
    data[username]["first_name"] = first_name
    data[username]["last_name"] = last_name
    data[username]["DOB"] = dob
    data[username]["Account_Creation_Date"] = get_creation_date()
    with open("database.json", "r+") as file:
        database = json.load(file)
        data.update(database)
        file.seek(0)
        json.dump(data, file, indent=4, sort_keys = True, default=str)

def get_creation_date():
    """Returns the date when the account was created."""
    current_datetime = datetime.now().date()
    return current_datetime

def username_checker(data):
    exists = True
    while exists:
        username = input("Please input your desired username: ")
        exists = username in data
        if exists:
            print("Sorry, that username is already taken.")
    return username

def get_option():
    selection = input("Please input one of the options: ")
    while selection.lower() not in options:
        print("Sorry, that option doesn't look correct."
              "Please try again")
    return options[selection.lower()]


def director(selected):
    """Directs the program to the correct function."""
    if selected == 0:
        sys.exit()
    elif selected == 1:
        view_account() #need to complete
    elif selected == 2:
        open_committee() #need to complete
    elif selected == 3:
        calculate_contributions() #need to complete
    elif selected == 4:
        view_scores() #need to complete

def view_account(data, login_name):
    """Allows the user to view their own account once they have logged in."""
    print(data[login_name])