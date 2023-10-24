# Name: Devin Smith
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Price for one bucket of popcorn: $12.99
#   Price for one drink: $4.99
#   Sales tax rate: 5.5%

import datetime

############## define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99
PR_POPCORN = 12.99
PR_DRINK = 4.99

# define global variables
num_tickets = 0
num_popcorn = 0
num_drink = 0
cost_tickets = 0
cost_popcorn = 0
cost_drink = 0
subtotal = 0
sales_tax = 0
total = 0

############## define programs functions ################
def main():

    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again (Y or N)?: " )
        if askAgain.upper() == "N" or askAgain == "n":
            more_tickets = False
            print("Thank you for your order. Enjoy your movie!")

            
def get_user_data():
    global num_tickets
    global num_popcorn
    global num_drink
    num_tickets = int(input("Number of movie tickets: "))
    num_popcorn = int(input("Number of popcorn buckets: "))
    num_drink = int(input("Number of drinks: "))

def perform_calculations():
    global cost_tickets, cost_popcorn, cost_drink, sales_tax, total, subtotal
    cost_tickets = num_tickets * PR_TICKET
    cost_popcorn = num_popcorn * PR_POPCORN
    cost_drink = num_drink * PR_DRINK
    subtotal = cost_tickets + cost_popcorn + cost_drink
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    moneyf = '8,.2f'
    line = '------------------------------'
    print(line)
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print(line)
    print('Tickets            $ ' + format(cost_tickets,moneyf))
    print('Popcorn            $ ' + format(cost_popcorn,moneyf))
    print('Drinks             $ ' + format(cost_drink,moneyf))
    print(line)
    print('Subtotal           $ ' + format(subtotal,moneyf))
    print('Sales Tax          $ ' + format(sales_tax,moneyf))
    print('Total              $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

##########  call on main program to execute ############
main()
