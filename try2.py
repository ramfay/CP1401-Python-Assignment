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


    destination_return_input = input()
    return destination_return_input


def fare_type_string():
    fare_error = False
    while fare_error == False:
        fare_input = str(input("Please select which class you would like for your travels by entering the corresponding code:"
          "\nBusiness - $ (Code: B)"
          "\nEconomy - $ (Code: E)"
          "\nFrugal - $ (Code:F)"))
        if fare_input == "B" or "b" or "E" or "e" or "F" or "f":
            fare_error = True
        else:
            print("Did you make a typo? Let's try that again.")
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
        if age_input > 0 and age_input <= 130:
            age_error = True
        else:
            print("Please ensure you entered the correct age of the passenger")
    return age_input


def main():



main()