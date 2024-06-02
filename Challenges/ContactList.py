# Contact List Application 
"""
Creating a simple contact list applicaton. This application should allow users to add new contacts, search for a contact by name and display all contacts

"""

def main_menu():
    print("MAIN MENU")
    print("----------")
    print("1. Add Contact")
    print("2 Search Contact")
    print("3. Display all contacts")
    main = int(input("Select the options:"))
    
    if(main == 1):
        add_contact()
    elif(main == 2):
        search_contact()
    elif(main == 3):
        display_users()
    else:
        print("Invalid Input Please Select From The Options")

contacts = []
def add_contact():
    user_name = input("Please enter your name: ")
    user_number = int(input("Please enter you number:"))
    user_email = input("please enter your email: ")

    con_dict = {
        "name" : user_name,
        "phone" : user_number,
        "email" : user_email
    }
    
    contacts.append(con_dict)

    print("New contact has been sucessfully added", contacts)
    main_menu()



def search_contact():
    search_user = input("Please enter the user name to search: ")
    for contact in contacts:
        if contact['name'] == search_user:
            print("Result found", search_user)
        elif contact['name'] != search_user:
            print("Not found")
    main_menu()

def display_users():
    print(contacts)
    main_menu()

main_menu()