#RichardKudrya_ProgrammingExercise_1

# Description:
# This program allows each buyer to buy up to 4 cinema tickets selling a
# maximum of 20 tickets. The program will prompt the user with how many
# tickets they would like to purchase, then updating the remaining tickets
# available while tracking how many people bought tickets. 


# This is the constant for the total number of tickets available
# Total tickets changed from 20 to 10
TOTAL_TICKETS = 10


def process_purchase(tickets_remaining):

    while True:

        # Here the user will be asked how many tickets they would like to purchase
        try:
            tickets_requested = int(input("How many tickets would you like to purchase? "))

            # Here the program will check if the requested number of tickets is within purchase limits
            if tickets_requested < 1 or tickets_requested > 4:
                print("You may only purchase up to 4 tickets.")
                continue

            # Here the program checks the amount of tickets remaining
            if tickets_requested > tickets_remaining:
                print(f"There are only {tickets_remaining} tickets remaining. Please try again.")
                continue

            # Here the program returns the amount of tickets purchased
            return tickets_requested

        except ValueError:
            # Here the program prompts the user if invalid input
            print("Invalid input. Please enter a number.")


def ticket_sales():

    # Here the variables are initialized
    tickets_remaining = TOTAL_TICKETS
    buyer_count = 0

    # Here the program displays a welcome message
    print("Welcome to the Cinema Ticket Presale!")
    print("There are ONLY 20 Tickets available!.")
    print("May purchase up to 4 tickets maximum!\n")

    # Here the program will repeat until all 20 tickets are sold
    while tickets_remaining > 0:

        # Here the program shows the remaining tickets
        print(f"There are {tickets_remaining} tickets remaining.")

        # Here the purchases get processed
        tickets_bought = process_purchase(tickets_remaining)

        # Here the remaining tickets are calculated
        tickets_remaining -= tickets_bought

        # Here adds a buyer to the buyer count
        buyer_count += 1

        # Here the program displays purchase confirmation
        print(f"You purchased {tickets_bought} ticket(s).")
        print(f"There are {tickets_remaining} ticket(s) remaining.\n")

    # Here the program displays the final number of buyers
    print("Tickets are sold out!")
    print(f"Number of buyers: {buyer_count}")


# Here the program runs
ticket_sales()
