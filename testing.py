options = {"quit":0, "open account": 1, "view account":2, "open committee": 3,
           "calculate contributions": 4, "view credit scores": 5,
           }
selection = input("Write selection: ")
return options[selection]

if selection.lower() ==

while True:
    selection = input("Please input one of the following options: ")
    if selection.lower() not in options:
        print("Sorry, that's not a valid option, please try again")
        continue
    else:
        break
if selection.lower() == 'open account':
    return 1
elif selection.lower() == 'view account':
    return 2
elif selection.lower() == options[2]:
    return 3
elif selection.lower() == options[3]:
    return 4
elif selection.lower() == options[4]:
    return 5
elif selection.lower() == options[-1]:
    print("Thank you for using the Kamiti Money Manager")
    sys.exit()