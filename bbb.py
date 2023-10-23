# Name: Devin Smith
# Name: Wyatt Pennington
# Prog Purpose: This program finds the cost of BBQ Buffet
#   Price for one adult: $19.95
#   Price for one child: $11.95
#   Service Fee: 10%
#   Sales tax rate: 6.2%

import datetime

############## define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .062
PR_ADULT = 19.95
PR_CHILD = 11.95
SERVICE_FEE = .1

# define global variables
num_adult = 0
num_child = 0
ser_fee = 0
cost_adult = 0
cost_child = 0
subtotal = 0
sales_tax = 0
total = 0

############## define programs functions ################
def main():

    more_food = True

    while more_food:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again (Y or N)?: " )
        if askAgain.upper() == "N" or askAgain == "n":
            more_food = False
            print("Thank you for your order. Enjoy your meal!")

            
def get_user_data():
    global num_adult
    global num_child
    num_adult = int(input("Number of adults: "))
    num_child = int(input("Number of children: "))

def perform_calculations():
    global cost_adult, cost_child, ser_fee, sales_tax, total, subtotal
    cost_adult = num_adult * PR_ADULT
    cost_child = num_child * PR_CHILD
    subtotal = cost_adult + cost_child
    ser_fee = subtotal * SERVICE_FEE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax + ser_fee

def display_results():
    moneyf = '8,.2f'
    line = '------------------------------'
    print(line)
    print('*** BRANCH BARBECUE BUFFET ***')
    print('* Your neighborhood BBQ house*')
    print(line)
    print('Adults             $ ' + format(cost_adult,moneyf))
    print('Children           $ ' + format(cost_child,moneyf))
    print(line)
    print('Subtotal           $ ' + format(subtotal,moneyf))
    print('Service Fee        $ ' + format(ser_fee,moneyf))
    print('Sales Tax          $ ' + format(sales_tax,moneyf))
    print('Total              $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

##########  call on main program to execute ############
main()
