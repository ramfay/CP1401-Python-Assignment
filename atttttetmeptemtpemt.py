def get_username_string():
    print("Please enter your first and last name.")
    username = input()
    return username


def menu_option_string():
    print("This is the Tropical Airlines Ticket Ordering System."
          "\nFor more information, press 'I'."
          "\nTo order a ticket, press 'O'."
          "\nTo quit, press 'Q'.")
    menu_input = input()
    return menu_input


"""def get_username_string():
    print("Please enter a first and last name for the person's ticket.")
    ticket_name = input()
    return ticket_name"""


def trip_length_string():
    print("For a one-way trip, please enter 'O."
          "\nFor a return trip, please enter 'R'.")
    trip_input = input()
    return trip_input

def get_destination_one_string():
    print("Please type in the appropriate corresponding code for your destination:"
          "\nCairns - $250 (Code: C1) "
          "\nSydney - $420 (Code: S1)"
          "\nPerth - $510 (Code: P1)")
    destination_one_input = input()
    return destination_one_input

def get_destination_return_string():
    print("Please type in the appropriate corresponding code for your destination:"
          "\nCairns - $400 (Code: C2)"
          "\nSydney - $575 (Code: S2)"
          "\nPerth - $700 (Code: P2)")
    destination_return_input = input()
    return destination_return_input


def fare_type_string_eg():
    f_error = False
    while f_error == False:
        fare_input=str(input("Please select which class you would like for your travels by entering the corresponding code:"
          "\nBusiness - $ (Code: B)"
          "\nEconomy - $ (Code: E)"
          "\nFrugal - $ (Code:F)"))
        if fare_input == "B" or fare_input == "E" or fare_input == "F":
            print("You have selected " + fare_input)
            return fare_input
        elif fare_input != "B" or fare_input != "E" or fare_input != "F":
            print("error")
        else:
            print("idk tbh")


def seat_type_string():
    print("Please select which seat you would like to be seated in by entering the corresponding code:"
          "\nWindow seat - $ (Code: W)"
          "\nAisle seat - $ (Code: A)"
          "\nMiddle seat - $ (Code: M)")
    seat_input = input()
    return seat_input


def ticket_age_int():
    print("Please enter the age for the ticket holder."
          "\n Note: only whole numbers will be accepted")
    age_input = int(input())
    return age_input


def main():
    print("Hello! Welcome to Tropical Airlines Ticketing Ordering System.")
    username = get_username_string()
    print("Welcome " + username + "!")
    menu_choice = menu_option_string()
    if menu_choice != "O" and menu_choice != "I" and menu_choice != "Q" and menu_choice != "o" and menu_choice != "i" and menu_choice != "q":
        print("You have not entered a valid menu option. Please press 'Y' to go back to the menu.")
    elif menu_choice == "I" or menu_choice == "i":
                print("Welcome to Tropical Airlines! Thanks for choosing us for "
                      "\nyour travel needs."
                      "\nIn this ticket ordering system, we'll ask a few quick questions "
                      "\nregarding the type of ticket you would like,"
                      "\nincluding destination information. Please press the corresponding letter key on your "
                      "\nkeyboard when you are prompted - it's as easy as that!"
                      "\nWe are also currently offering 50% discounted fares for children! (Press 'Y' to return to the menu.)")
    elif menu_choice == "Q" or menu_choice == "q":
                print("BYE Felicia")
    elif menu_choice == "O" or menu_choice == "o":
                print("Let's order a ticket! Is this ticket for you, or someone else?")
                ticket_user = str(input("Enter 'M' if this ticket is for you, or 'S' if it is for someone else."))
                if ticket_user == "S" or ticket_user == "s":
                    """ ticket_name = get_username_string()
                    print("Ticket for " + ticket_name + "!")
                elif ticket_user == "M" or ticker_user == "m":
                    ticket_name = username
                    print("Ticket for " + ticket_name + "!")
                else:
                    print("placeholder") """
    else:
        print("Something went horribly wrong, sorry!")

main()
