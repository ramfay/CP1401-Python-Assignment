# constants

C1 = 250
C2 = 400
S1 = 420
S2 = 575
P1 = 510
P2 = 700
BUSINESS = 275
ECONOMY = 25
FRUGAL = 0
WINDOW = 75
AISLE = 50
MIDDLE = -25


def get_username():
    username = input("Welcome! Please enter your first and last name:")
    return username


def get_menu():
    m_error = False
    while m_error == False:
        menu_choice = input("Please make a selection:"
                            "\n(I)nformation"
                            "\n(O)rder a ticket"
                            "\n(Q)uit")
        menu_choice = menu_choice.upper()
        if menu_choice == "I":
            print("Welcome to Tropical Airlines! Thanks for choosing us for "
                      "\nyour travel needs."
                      "\nIn this ticket ordering system, we'll ask a few quick questions "
                      "\nregarding the type of ticket you would like,"
                      "\nincluding destination information. Please press the corresponding letter key on your "
                      "\nkeyboard when you are prompted - it's as easy as that!"
                      "\nWe are also currently offering 50% discounted fares for children!"
                  "\nYou will be directed back to the menu now.")
        elif menu_choice == "Q":
            m_error = True
            print("Thanks for visiting, bye!")
        elif menu_choice == "O":
            return menu_choice
        elif menu_choice != "I" or menu_choice != "O" or menu_choice != "Q":
            print("Sorry, it seems like you've put in an invalid option. Let's try that again!")
        else:
            return menu_choice


def main():
    username = get_username()
    print("Pleased to see you, " + username + "! Welcome to Tropical Airlines Ticket Ordering System.")
    menu_choice = get_menu()
    final = []
    if menu_choice == "O":
        print("Let's order a ticket!")
        n_error = False
        while n_error == False:
            who_dis = input("For whom is this ticket?"
                   "\n(M)yself"
                   "\n(S)omeone else")
            who_dis = who_dis.upper()
            if who_dis == "M":
                n_error = True
                ticket_name = username
                print(ticket_name)
            elif who_dis =="S":
                n_error = True
                ticket_name = input("Please enter the first and last name of the ticket holder:")
                print(ticket_name)
            else:
                print("Oh no, you've entered an unavailable option. Take 2, let's do that again!")

    print (final)

main()
