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


def get_username_string():
    username = str(input("Please enter your first and last name."))
    return username


def menu_option_string():
    menu_error = False
    while menu_error == False:
        menu_input = str(input("This is the Tropical Airlines Ticket Ordering System."
                               "\nFor more information, press 'I'."
                               "\nTo order a ticket, press 'O'."
                               "\nTo quit, press 'Q'."))
    if menu_input == "I" or "i" or "O" or "o" or "Q" or "q":
        menu_error = True
    else:
        print("It seems you have not entered a valid option! That's okay, try again.")
    return menu_input


"""def get_username_string():
    print("Please enter a first and last name for the person's ticket.")
    ticket_name = input()
    return ticket_name"""


def trip_length_string():
    trip_error = False
    while trip_error == False:
        trip_input = str(input("For a one-way trip, please enter 'O."
                               "\nFor a return trip, please enter 'R'."))
    if trip_input == "O" or "o" or "R" or "r":
        trip_error = True
    else:
        print("You have not specified a proper response! One more time.")
    return trip_input


def get_destination_one_string():
    destination_one_error = False
    while destination_one_error == False:
        destination_one_input = str(input("Please type in the appropriate corresponding code for your destination:"
                                          "\nCairns - $250 (Code: C1) "
                                          "\nSydney - $420 (Code: S1)"
                                          "\nPerth - $510 (Code: P1)"))
        if destination_one_input == "C1" or "c1" or "S1" or "s1" or "P1" or "p1":
            destination_one_error = True
        else:
            print("Uh oh, please try again! Make sure you put in the correct code!")
    return destination_one_input


def get_destination_return_string():
    destination_error = False
    while destination_error == False:
        destination_return_input = str(input("Please type in the appropriate corresponding code for your destination:"
                                             "\nCairns - $400 (Code: C2)"
                                             "\nSydney - $575 (Code: S2)"
                                             "\nPerth - $700 (Code: P2)"))
        if destination_return_input == "C2" or "c1" or "S2" or "s2" or "P2" or "p2":
            destination_error = True
        else:
            print("Oh dear, it appears you have made a mistake! Take 2, action.")
    return destination_return_input


def fare_type_string():
    fare_error = False
    while fare_error == False:
        fare_input = str(
            input("Please select which class you would like for your travels by entering the corresponding code:"
                  "\nBusiness - $ (Code: B)"
                  "\nEconomy - $ (Code: E)"
                  "\nFrugal - $ (Code:F)"))
        if fare_input == "B" or "b" or "E" or "e" or "F" or "f":
            fare_error = True
        else:
            print("")
        return fare_input


def seat_type_string():
    seat_error = False
    while seat_error == False:
        seat_input = str(input("Please select which seat you would like to be "
                               "\nseated in by entering the corresponding code:"
                               "\nWindow seat - $ (Code: W)"
                               "\nAisle seat - $ (Code: A)"
                               "\nMiddle seat - $ (Code: M)"))
        if seat_input == "W" or "w" or "A" or "a" or "M" or "m":
            seat_error = True
        else:
            print("Are you sure you entered the correct letter? Here, try again.")

        return seat_input


def ticket_age_int():
    age_error = False
    while age_error == False:
        age_input = int(input("What is the age of the passenger?"))
        if 0 >= age_input <= 116:
            age_error = True
        elif 0 <= age_input >= 116:
            print("It seems like it's not physically possible to be that age! Please try again.")
        else:
            return age_input


def fare_type_string_eg():
    fare_input = str(
        input("Please select which class you would like for your travels by entering the corresponding code:"
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


def fare_type_string_egggg():
    f_error = False
    while f_error == False:
        fare_input = str(
            input("Please select which class you would like for your travels by entering the corresponding code:"
                  "\nBusiness - $ (Code: B)"
                  "\nEconomy - $ (Code: E)"
                  "\nFrugal - $ (Code:F)"))
        if fare_input == "B":
            fare_input = "Business"
            return fare_input
        elif fare_input != "B" or fare_input != "E" or fare_input != "F":
            print("Did you make a typo? Let's try that again.")
        else:
            print("This code sure is broken, ain't it.")

def total_cost_int():



def main():
    user_age = ticket_age_int()
    print(user_age)
    blib = fare_type_string_egggg()
    print("You have selected " + blib)


main()
