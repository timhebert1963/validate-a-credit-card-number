from modules_validate_credit_card_number import *
from Tim_common import *
import os
import random



def display_ccn_issuers():
    
    print(" Credit Card Issuers:")
    print(" ____________________________________________________________________________________")
    print('\n')
    print("  1. {:20s}    5. {:30s}     9. {:30s}".format('Visa', 'JCB', 'Maestro'))
    print("  2. {:20s}    6. {:30s}    10. {:30s}".format('MasterCard', 'Diners Club - North America', 'Visa Electron'))
    print("  3. {:20s}    7. {:30s}    11. {:30s}".format('Amercican Express', 'Diners Club - Carte Blanche', 'InstaPayment'))
    print("  4. {:20s}    8. {:30s}              ".format('Discover', 'Diners Club - International'))
    print('\n')
    print(" ____________________________________________________________________________________")
    print('\n')

# **** End of function display_ccn_issuers() **** #


def select_ccn_issuer():

    valid_input = False

    while not valid_input:

        # user selects the Credit Card Issuer
        ccn_issuer = int(input(" Select the Credit Card Issuer from the list above. Enter 1 - 11  "))
        print('\n')

        if ccn_issuer >= 1 or ccn_issuer <= 11:
            if ccn_issuer == 1:
                valid_input = True
                issuer = 'Visa'

            elif ccn_issuer == 2:
                valid_input = True
                issuer = 'MasterCard'

            elif ccn_issuer == 3:
                valid_input = True
                issuer = 'American Express'

            elif ccn_issuer == 4:
                valid_input = True
                issuer = 'Discover'

            elif ccn_issuer == 5:
                valid_input = True
                issuer = 'JCB'

            elif ccn_issuer == 6:
                valid_input = True
                issuer = 'Diners Club - North America'

            elif ccn_issuer == 7:
                valid_input = True
                issuer = 'Diners Club - Carte Blanche'

            elif ccn_issuer == 8:
                valid_input = True
                issuer = 'Diners Club - International'

            elif ccn_issuer == 9:
                valid_input = True
                issuer = 'Maestro'

            elif ccn_issuer == 10:
                valid_input = True
                issuer = 'Visa Electron'

            elif ccn_issuer == 11:
                valid_input = True
                issuer = 'InstaPayment'

            else:

                clear_screen()

                print(" You did not provide a valid Credit Card Issuer. Please try again.")
                print('\n')
                display_ccn_issuers()

    return issuer

# **** End of function select_ccn_issuer() **** #


def create_ccn_issuer_object(ccn_issuer):

    if ccn_issuer == 'Visa':
        ccn_issuer_object = Visa()
        return ccn_issuer_object

    elif ccn_issuer == 'MasterCard':
        ccn_issuer_object = MasterCard()
        return ccn_issuer_object

    elif ccn_issuer == 'American Express':
        ccn_issuer_object = AmericanExpress()
        return ccn_issuer_object

    elif ccn_issuer == 'Discover':
        ccn_issuer_object = Discover()
        return ccn_issuer_object

    elif ccn_issuer == 'JCB':
        ccn_issuer_object = JCB()
        return ccn_issuer_object

    elif ccn_issuer == 'Diners Club - North America':
        ccn_issuer_object = DinersClub_NA()
        return ccn_issuer_object

    elif ccn_issuer == 'Diners Club - Carte Blanche':
        ccn_issuer_object = DinersClub_CB()
        return ccn_issuer_object

    elif ccn_issuer == 'Diners Club - International':
        ccn_issuer_object = DinersClub_Int()
        return ccn_issuer_object

    elif ccn_issuer == 'Maestro':
        ccn_issuer_object = Maestro()
        return ccn_issuer_object

    elif ccn_issuer == 'Visa Electron':
        ccn_issuer_object = VisaElectron()
        return ccn_issuer_object

    elif ccn_issuer == 'InstaPayment':
        ccn_issuer_object = InstaPayment()
        return ccn_issuer_object

# **** End of function create_ccn_issuer_object() **** #


def will_test_ccn_be_used(ccn_issuer, ccn_issuer_object):

    # user decides if ccn issuer test ccn to be used
    valid_input = False

    # ask user if CCN Issuer Test CCN should be used
    while not valid_input:
        answer = input(" Do you want to use a CCN Issuer Test Credit Card Number? 'y' or 'n'  ")

        if answer.lower() == 'y' or answer.lower() == 'n':
        	valid_input = True

        else:
            print(" You did not answer 'y' or 'n'. Please try again!")

    # if answer is yes then user decided to use a Test CCN provided by CCN Issuer
    if answer.lower() == 'y':

        user_test_ccn = True

        # find out if user wants to use a valid or invalid ccn
        #
        # some CCNs have a valid format and proper length but the sequence of 
        # numbers may or may not pass the checksum.
        #
        # giving the option to test with valid and invalid CCNs
        valid_input = False

        while not valid_input:
            print('\n')
            print(" For a  Valid  CCN  ............ Enter 1")
            print(" For an Invalid CCN  ........... Enter 2")
            answer = input(" Enter 1 or 2 for the type of CCN to use   ")

            # check if answer is valid
            if answer == '1' or answer == '2':
                valid_input = True

            else:
                print(" You did not Enter a valid answer. Try again!")
                print('\n')

        # user decided to use a valid test_ccn
        if answer == '1':
            test_ccn_list = ccn_issuer_object.valid_test_nums

        # user decided to use an invalid test_ccn
        else:
            test_ccn_list = ccn_issuer_object.invalid_test_nums

        # shuffle the test_ccn_list to with random CCNs
        for i in range(10):
            random.shuffle(test_ccn_list)

        # return only 1 test_ccn. test_ccn_list[0]
        return user_test_ccn, test_ccn_list[0]

    # if answer is no then user decided NOT to use a Test CCN provided by CCN Issuer
    else:
        user_test_ccn = False
        test_ccn = ''
        return user_test_ccn, test_ccn

# **** End of function will_test_ccn_be_used() **** #


def user_provided_ccn(ccn_issuer, ccn_issuer_object):

    print('\n')
    ccn = input(" Enter the credit card number to validate. Do not use spaces!   ")
    return ccn

# **** End of function user_provided_ccn() **** #


def validate_ccn_starts_with_and_length(ccn, ccn_issuer, ccn_issuer_object):

    is_ccn_format_valid = False
    is_ccn_length_valid = False

    # check to see if ccn starts_with matches ccn issuers starts_with values
    # some issuers also have a range which needs to be validated
    issuer_starts_with_list = ccn_issuer_object.starts_with

    for i in range(len(ccn_issuer_object.starts_with)):
    	
        # grab the same number of starts_with digits from ccn to compare.        
        ccn_starts_with = ccn[:len(ccn_issuer_object.starts_with[0])]

        if  ccn_issuer_object.starts_with[i] == ccn_starts_with:
            is_ccn_format_valid = True
            break

    # check the ccn starts with ranges if is_valid_ccn_format == False
    if not is_ccn_format_valid:
        ccn_starts_with = ccn[:len(ccn_issuer_object.range[0])]

        if int(ccn_starts_with) >= int(ccn_issuer_object.range[0]) and int(ccn_starts_with) <= int(ccn_issuer_object.range[1]):
            is_ccn_format_valid = True

    if is_ccn_format_valid:

        # check if ccn length is valid
        for i in range(len(ccn_issuer_object.length)):
        	if int(len(ccn)) == int(ccn_issuer_object.length[i]):
        	    is_ccn_length_valid = True
        	    break

    if is_ccn_format_valid and is_ccn_length_valid:
        return True
    else:
    	return False

# **** End of function validate_ccn_starts_with_and_length() **** #


def format_ccn_for_display(ccn):

    new_ccn = ''

    for i in range(len(ccn)):

        # add a space after every 4 digits of ccn
        # if i == 0 pass (this is the 1st digit)
        if i == 0:
            pass

        elif i % 4 == 0:
            new_ccn = new_ccn + ' '

        new_ccn = new_ccn + ccn[i]

    return new_ccn


# **** End of function format_ccn_for_display() **** #


def ccn_valid_banner(issuer, ccn, is_valid):

    if is_valid:
        # strings to display in display banner
        first_string  = ("The {} Credit Card Number {} is ** Valid ** !!".format(issuer, ccn))

    else:
        first_string  = ("The {} Credit Card Number {} is ** NOT VALID ** !!".format(issuer, ccn))

    # assign values to Banner object attributes
    banner_object = assign_banner_attributes(first_string)

    # call display_banner
    display_banner(banner_object)
    del banner_object

# **** End of function get_radians() **** #


def validate_another_ccn_number():

    # Find out if user wants to validate another Credit Card Number
    yes_or_no = False

    while not yes_or_no:

        validate_ccn = input(" Do you want to validate another Credit Card Number? 'y' or 'n'  ")

        if validate_ccn.lower() == 'y':
            validate_ccn = True
            break

        elif validate_ccn.lower() == 'n':
            validate_ccn = False
            break

        else:
            print(" You did not enter 'y' or 'n'. Please try again.")

    
    return validate_ccn

# **** End of function validate_another_ccn_number() **** #
