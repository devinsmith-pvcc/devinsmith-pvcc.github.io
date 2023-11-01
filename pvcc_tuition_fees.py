#Name: Jay and Devin
#PR



import datetime

#Define Tuition & Fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAP_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#Define Global Variables
inout = 1 # 1 means in-state, 2 meanas out of state
numcredits = 0
scholarshipamt = 0


#################### Define Main Program ####################

def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_result()
        yesno = input("\nWould you like to calculate tuition and fees for another student? (Y/N?): ")
        if yesno == "n" or yesno == "N":
            more = False
            print('Thank you for enrolling to PVCC!') 
        





def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for In-State; Enter a 2 for Out-of-State: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount recieved: "))



def perform_calculations():
    global tuition_cost, tuition_total, cap_fee, instuition_fee, activity_fee, total, balance
    if inout == 1 :
        tuition_cost = RATE_TUITION_IN
        cap_fee = 0

    else:
        tuition_cost = RATE_TUITION_OUT
        cap_fee = RATE_CAP_FEE * numcredits


    tuition_total = tuition_cost * numcredits
    instuition_fee = RATE_INSTITUTION_FEE * numcredits
    activity_fee = RATE_ACTIVITY_FEE * numcredits
    total = tuition_total + cap_fee + instuition_fee + activity_fee
    balance = total - scholarshipamt 

    





def display_result():
    moneyf = '8,.2f'
    line = '------------------------------------------'
    print(line)
    print('PVCC')
    print(line)
    print('Tuition         $ ' + format(tuition_total, moneyf))
    print('Capital Fee     $ ' + format(cap_fee, moneyf))
    print('Institution Fee $ ' + format(instuition_fee, moneyf))
    print('Activity Fee    $ ' + format(activity_fee, moneyf))
    print(line)
    print('Total           $ ' + format(total, moneyf))
    print(line)
    print('Scholarship     $ ' + format(scholarshipamt, moneyf))
    print(line)
    print('Total Balance   $ ' + format(balance, moneyf))



main()

