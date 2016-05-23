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
LUCKY_WORD = "fluff"
import random


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


def get_trip_length():
    t_error = False
    while t_error == False:
        o_r = input("Is this trip:"
                "\n(O)ne way or"
                "\n(R)eturn?")
        o_r = o_r.upper()
        if (o_r == "O") or (o_r == "R"):
            t_error = True
        else:
            t_error = False
            print("You have not specified a proper response! One more time.")
    return o_r


def get_dest_one():
    do_error = False
    while do_error == False:
        dest_one = input("Please pick a destination:"
                         "\n(C)airns $250"
                         "\n(S)ydney $420"
                         "\n(P)erth $510")
        dest_one = dest_one.upper()
        if dest_one == "C" or dest_one == "S" or dest_one == "P":
            do_error = True
        else:
            print("Uh oh, please try again! Make sure you put in the correct letter!")
    return dest_one


def get_dest_return():
    dr_error = False
    while dr_error == False:
        dest_return = input("Please pick a destination:"
                            "\n(C)airns $400"
                            "\n(S)ydney $575"
                            "\n(P)erth $700")
        dest_return = dest_return.upper()
        if dest_return == "C" or dest_return == "S" or dest_return == "P":
            dr_error = True
        else:
            print("Uh oh, please try again! Make sure you put in the correct letter!")
    return dest_return


def get_fare_type():
    f_error = False
    while f_error == False:
        fare_type = input("Please select a class:"
                          "\n(B)usiness $275"
                          "\n(E)conomy $25"
                          "\n(F)rugal $0 (FREE!)")
        fare_type = fare_type.upper()
        if fare_type == "B" or fare_type == "E" or fare_type == "F":
            f_error = True
        else:
            print("Did you make a typo? Let's try that again.")
    return fare_type


def get_seat_type():
    s_error = False
    while s_error == False:
        seat_type = input("Please select a seat type:"
                          "\n(W)indow $25"
                          "\n(A)isle $50"
                          "\n(M)iddle $-25 off your total!")
        seat_type = seat_type.upper()
        if seat_type == "W" or seat_type == "A" or seat_type == "M":
            s_error = True
        else:
            print("Are you sure you entered the correct letter? Here, try again.")


def get_age():
    a_error = False
    while a_error == False:
        age = int(input("What is the age of the passenger?"))
        if 0 >= age <= 116:
            a_error = True
        elif 0 <= age >= 116:
            print("It seems like it's not physically possible to be that age! Please try again.")
        else:
            return age


def calculate_total_fare(trip_destination,  direction, seat, fare, age):
    if trip_destination == "C" and direction == "O":
        total_fare = C1
    else:
        total_fare = P2
    return total_fare



def main():
    # This gets the username for the person. This is also the name on the ticket if
    # it is being ordered for themselves.
    username = get_username()
    # Welcome user to the system.
    print("Pleased to see you, " + username + "! Welcome to Tropical Airlines Ticket Ordering System.")
    # Calling the menu function. Only info and quit are handled in that function, order ticket
    # is in main.
    menu_choice = get_menu()
    # Define a new list. This is what will be displayed to the user at the end.
    final = []
    # Order ticket begins.
    if menu_choice == "O":
        print("Let's order a ticket!")
        # Error checking for whoever the ticket holder will be, using while loop / switch.
        n_error = False
        while not n_error:
            who_dis = input("For whom is this ticket?"
                   "\n(M)yself"
                   "\n(S)omeone else")
            # Convert response from lower to upper case.
            # This is used throughout the program.
            who_dis = who_dis.upper()
            if who_dis == "M":
                n_error = True
                ticket_name = username
                # Adding name to the list.
                print("Ticket for: " + ticket_name + ".")
            elif who_dis == "S":
                n_error = True
                ticket_name = input("Please enter the first and last name of the ticket holder:")
                print("Ticket for: " + ticket_name + ".")
            else:
                print("Oh no, you've entered an unavailable option. Take 2, let's do that again!")
        direction = get_trip_length()
        if direction == "O":
            trip_destination = get_dest_one()
            # TODO - separate fn for get_destination()
            if trip_destination == "C":
                print("You have selected Cairns.")
            elif trip_destination == "S":
                print("You have selected Sydney.")
            else:
                print("You have selected Perth.")
        elif direction == "R":
            trip_destination = get_dest_return()
            if trip_destination == "C":
                print("You have selected Cairns.")
            elif trip_destination == "S":
                print("You have selected Sydney.")
            else:
                print("You have selected Perth.")
        else:
            print("How did you get here, honestly.")
        fare = get_fare_type()
        if fare == "B":
            print("You have selected business class. Fancy.")
        elif fare == "E":
            print("You have selected economy class. Economical!")
        else:
            print("You have selected frugal. It's free!")
        seat = get_seat_type()
        if seat == "W":
            print("You have chosen the window seat. Enjoy the view!")
        elif seat == "A":
            print("You have chosen the aisle seat. Quicker route to the bathroom, good choice!")
        else:
            print("You have chosen the middle seat. Hope you like making new friends!")
        age = get_age()
        if age <= 16:
            print("You are eligible for a 50% discount! Yay!")
        else:
            print("Sorry, you do not qualify for the children's discount.")

        # TODO
        total_fare = calculate_total_fare(trip_destination, direction, seat, fare, age)
        print(total_fare)
        # some fun because I feel bad for handing this in late.
        # words = ['hammer', 'fluff', 'bongos', 'dog ', 'pupper', 'shepherd']
        # discount = (random.choice(words))
        # if discount == LUCKY_WORD:
        #     print("Congratulations! You have received a random discount."
        #           "\nYou now get 30% off your total cost.")
        # else:
        #     print("Gadzooks! You have missed out on our random discount."
        #           "\nOrder another ticket, and see if you get it next time.")
    print (final)

main()
