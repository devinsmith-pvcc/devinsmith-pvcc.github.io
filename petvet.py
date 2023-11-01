# Name: Devin Smith
# Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats
#
# NOTE: Pet medications prescriibed by licensed veterinarians are not subject to sales tax in Virginia
#
# PET CARE MEDS Pricing
#-------------------------------------
# Canine Vaccines:
#   1. Bordatella $30.00
#   2. DAPP $35.00
#   3. Influenza $48.00
#   4. Leptospirosis $21.00
#   5. Lyme Disease $41.00
#   6. Rabies $25.00
#   7. Full Vaccine Package (includes all vaccines): 15% discount
# Feline Vaccines:
#   1. Leukemia $35.00
#   2. Viral Rhinotracheitis $30.00
#   3. Rabies (one year) $25.00
#   4. Full Vaccine Package 10% discount
#
# Canine Heartworm Preventative Chews (price per chew; one chew per month)
#   Small dogs, Up to 25 lbs: $9.99
#   Medium-sized dogs, 26 to 50 lbs: $11.99
#   Large dogs: 51 to 100 lbs: $13.99
#   Feline (one size) $8.00

import datetime

##############  define global variables #############
# define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEPTO = 21
PR_LYME = 41
PR_RABIES = 25

# define cat prices
PR_LEUK = 35
PR_RHINO = 30
PR_RAB = 25

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99
PR_CHEWS_CAT = 8

#define global variables

##############  define program functions ##################
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()

        askAgain = input("\nWould you like to process another pet (Y/N)?: ")
        if askAgain.upper() == "N" :
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("Is this pet a dog (D) or cat (C)? ")
    pet_weight = int(input("Weight of your pet (in pounds): "))


################ DOG functions #################

def get_dog_data():
    global dog_vax_type, num_chews
    dog1 = "\n** Dog Vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis"
    dog2 = "\n\t5.Lyme Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t8.NONE"
    dogmenu = dog1 + dog2
    dog_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all dogs.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))

    else:
            num_chews = 0

def perform_dog_calculations():
    global vax_cost, chews_cost, total

    ##### vaccines

    if dog_vax_type == 1 :
        vax_cost = PR_BORD

    elif dog_vax_type == 2 :
        vax_cost = PR_DAPP

    elif dog_vax_type == 3 :
        vax_cost = PR_FLU

    elif dog_vax_type == 4 :
        vax_cost = PR_LEPTO

    elif dog_vax_type == 5 :
        vax_cost = PR_LYME

    elif dog_vax_type == 6 :
        vax_cost = PR_RABIES

    elif dog_vax_type == 7 :
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU + PR_LEPTO + PR_LYME + PR_RABIES
        vax_cost = .85 * PR_ALL

    else:
        vax_cost = 0

    ##### heart worm chews
    if num_chews != 0 :
        if pet_weight < 25 :
            chews_cost = num_chews * PR_CHEWS_SMALL

        elif pet_weight >= 26 and pet_weight < 50 :
            chews_cost = num_chews * PR_CHEWS_MED

        else:
            chews_cost = num_chews * PR_CHEWS_LARGE

    if num_chews == 0 :
        chews_cost = 0

    #####find total
    total = vax_cost + chews_cost

def display_dog_results():
    moneyf = '8,.2f'
    line = '--------------------------------'
    print(line)
    print('******** PET CARE MEDS *********')
    print('Animal healthcare professionals')
    print(line)
    print('Canine Vaccine       $ ' + format(vax_cost,moneyf))
    print('Heartworm Chews      $ ' + format(chews_cost,moneyf))
    print(line)
    print('Total                $ ' + format(total,moneyf))

################ CAT functions ##################
def get_cat_data():
    global cat_vax_type, num_chews
    cat1 = "\n** Cat Vaccines: \n\t1.Leukemia \n\t2.Rhinotracheitis \n\t3.Rabies (One Year) \n\t4.Full Vaccine Package \n\t5.None"
    catmenu = cat1
    cat_vax_type = int(input(catmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all cats.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))

    else:
            num_chews = 0

def perform_cat_calculations():
    global vax_cost, chews_cost, total

    if cat_vax_type == 1 :
        vax_cost = PR_LEUK

    elif cat_vax_type == 2 :
        vax_cost = PR_RHINO

    elif cat_vax_type == 3 :
        vax_cost = PR_RAB

    elif cat_vax_type == 4 :
        PR_ALL = PR_LEUK + PR_RHINO + PR_RAB
        vax_cost = PR_ALL * .9

    else:
        vax_cost = 0

    chews_cost = num_chews * PR_CHEWS_CAT
    total = chews_cost + vax_cost

def display_cat_results():
    moneyf = '8,.2f'
    line = '--------------------------------'
    print(line)
    print('******** PET CARE MEDS *********')
    print('Animal healthcare professionals')
    print(line)
    print('Feline Vaccine       $ ' + format(vax_cost,moneyf))
    print('Heartworm Chews      $ ' + format(chews_cost,moneyf))
    print(line)
    print('Total                $ ' + format(total,moneyf))

################ call on main ################
main()
