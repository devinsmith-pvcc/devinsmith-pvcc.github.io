#Name: Jay and Devin
#PR
#appended by devin


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
outfile = 'tuition.html'

#################### Define Main Program ####################

def main():
    open_outfile()
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_result()
        yesno = input("\nWould you like to calculate tuition and fees for another student? (Y/N?): ")
        if yesno == "n" or yesno == "N":
            more = False
            print('Thank you for enrolling to PVCC!')
            print('Please open ' + outfile)
            f.write('</body></html>')
            f.close()
        



def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Tuition </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #583e23; background-image: url(wp-tuition.jpg); color: #b0a084;">\n')

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
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    line = '------------------------------------------'

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #13262f;  font-family: arial; margin: auto;">\n')            
    f.write('<tr><td colspan = 3>\n')
    f.write('<h2>Tuition Cost Calculator</h2></td></tr>')
    f.write('<tr><td colspan = 3>\n')
    f.write('*** For the betterment of your future ***\n')
    f.write(tr + 'ITEM' + endtd + 'RATE' + endtd + 'COST' + endtr)
    f.write(tr + 'Tuition' + endtd + str(tuition_cost) + endtd + format(tuition_total,moneyf) + endtr)
    f.write(tr + 'Capital Fee' + endtd + str(RATE_CAP_FEE) + endtd + format(cap_fee,moneyf) + endtr)
    f.write(tr + 'Institution Fee' + endtd + str(RATE_INSTITUTION_FEE) + endtd + format(instuition_fee, moneyf) + endtr)
    f.write(tr + 'Activity Fee' + endtd + str(RATE_ACTIVITY_FEE) + endtd + format(activity_fee,moneyf) + endtr)
    f.write(tr + 'Total' + endtd + sp + endtd + format(total,moneyf) + endtr)
    f.write(tr + 'Scholarship' + endtd + sp + endtd + format(scholarshipamt,moneyf) + endtr)
    f.write(tr + 'Total Balance' + endtd + sp + endtd + format(balance,moneyf) + endtr)
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

