# NAME: Devin
# PROG PURPOSE: Calculate Personal Property taxes in Charlottesville VA
TAX_RATE = .042
TAX_RELIEF = .33

import datetime

def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        
        askAgain = input("\nAnother vehicle (Y/N)? ")
        if askAgain.upper() == "N" or askAgain == "n":
            more = False
            print("Thank you!")
        
def get_user_data():
    global car_value, relief
    car_value = int(input('Assessed value of vehicle: '))
    relief = input('Is the vehicle eligible for tax relief (Y/N)? ')

def perform_calculations():
    global car_tax, relief_amt, total, annual
    car_tax = (car_value * TAX_RATE) / 2
    annual = car_value * TAX_RATE
    if relief.upper() == "Y":
        relief_amt = car_tax * TAX_RELIEF
    else:
        relief_amt = 0

    total = car_tax - relief_amt

def display_results():
    moneyf = '8,.2f'
    line = '----------------------------------'
    print(line)
    print('*City of Charlottesville, Virginia*')
    print('*******Personal Property Tax*******')
    print(line)
    print('Assessed Value         $ ' + format(car_value,moneyf))
    print('Annual Tax Amount      $ ' + format(annual,moneyf))
    print('Semi-Annual Tax Amount $ ' + format(car_tax,moneyf))   
    print('Relief                 $ ' + format(relief_amt,moneyf))
    print(line)
    print('Total Due              $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))




main()
