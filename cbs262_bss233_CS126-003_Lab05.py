# Lab 05 - Phone Contacts
# Colton Spector and Brandon Salter
# cbs262 and bss223
# 10/27/2017
# Lab Section - 03
'''This program resembles a phone contact list and is capable of updating
each bit of contact information provided as well as checking to see if a
contact exists inside of the dictionary.'''


# Creates the contact
def create_contact(contacts, first, last, email, age, phone):
    fullName = first.lower() + ' ' + last.lower()
    contacts[fullName] = [email, age, phone]


# Updates the contact number
def update_contact_number(contacts, first, last, phone):
    fullName = first.lower() + ' ' + last.lower()
    if fullName in contacts:
        contacts[fullName][2] = phone


# Updates the contact email
def update_contact_email(contacts, first, last, email):
    fullName = first.lower() + ' ' + last.lower()
    if fullName in contacts:
        contacts[fullName][0] = email


# Updates the contacts age
def update_contact_age(contacts, first, last, age):
    newAge = age
    if contains_contact:
        fullName = first.lower() + ' ' + last.lower()
        contacts[fullName][1] = newAge


# Grabs the contacts email and returns it
def get_contact_email(contacts, first, last):
    fullName = first.lower() + ' ' + last.lower()
    if fullName in contacts:
        return contacts[fullName][0]


# Grabs the contacts age and returns it
def get_contact_age(contacts, first, last):
    fullName = first.lower() + ' ' + last.lower()
    if contains_contact:
        return contacts[fullName][1]


# Grabs the contacts number and returns it
def get_contact_number(contacts, first, last):
    fullName = first.lower() + ' ' + last.lower()
    if fullName in contacts:
        return contacts[fullName][2]


# Checks to see if the dictionary contains the contact
def contains_contact(contacts, first, last):
    fullName = first.lower() + ' ' + last.lower()
    if fullName in contacts:
        return True
    else:
        return False


# Displays the key(Full Name) then the contents of the list
def display_function(contacts, first, last):
    fullName = first.lower() + ' ' + last.lower()
    if contains_contact(contacts, first, last):
        print(fullName)
        print(contacts[fullName][0])
        print(contacts[fullName][1])
        print(contacts[fullName][2])


# Main calls to see if our code runs correctly
def main():

    contacts = {}

    create_contact(contacts, "Katie", "Katz", "katie.katz@nau.edu", 25,
                   "857-294-2758")
    create_contact(contacts, "Jim", "Jones", "jim.jones@nau.edu", 19,
                   "525-866-2749")
    create_contact(contacts, "Sarah", "Sanders",
                   "sarah.sanders@nau.edu", 18, "593-026-2532")

    print("Creation of Jim Jones : {}".format(
        "Passed" if contains_contact(contacts, "jim", "Jones")
        else "Failed"))

    print("Creation of Katie Katz: {}".format(
        "Passed" if contains_contact(contacts, "Katie", "KaTz") else
        "Failed"))

    print("Creation of Sarah Sanders: {}".format(
        "Passed" if contains_contact(contacts, "Sarah", "Sanders") else
        "Failed"))

    update_contact_age(contacts, "Sarah", "Sanders", 19)
    print("Updating Sarah Sanders age to 19: {}".format(
        "Passed" if get_contact_age(contacts, "sarah", "sanDers") == 19
        else "Failed"))

    update_contact_email(contacts, "Jim", "Jones",
                         "jim.jones@gmail.com")
    print("Updating Jim Jones email: {}".format(
        "Passed" if get_contact_email(contacts, "jim", "jones") ==
        "jim.jones@gmail.com" else "Failed"))

    update_contact_number(contacts, "Katie", "Katz", "907-536-2946")
    print("Updating Katie Katz's number: {}".format(
        "Passed" if get_contact_number(contacts, "Katie", "Katz") ==
        "907-536-2946" else "Failed"))

    display_function(contacts, 'Katie', 'Katz')
    display_function(contacts, 'George', 'Shaw')

main()
