from modules_validate_credit_card_number import *
from functions_validate_credit_card_number import *
from Tim_common import *

# How to validate a Credit Card Number?
# Most credit card number can be validated using the Luhn algorithm, which is more or a less a glorified Modulo 10 formula!
#
# The Luhn Formula:
# 1. Drop the last digit from the number. The last digit is what we want to check against
# 2. Reverse the numbers
# 3. Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# 4. Add all the numbers together
# 5. The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10 (Modulo 10)
#
# ______________________________________________________________________________________________________________________
#
# Credit Card Issuer            Starts With (IIN Range)                                       Length (number of digits)
# ______________________________________________________________________________________________________________________
#
# American Express ..........   34, 37 .....................................................  15
# Diners Club - Carte Blanche   300, 301, 302, 303, 304, 305 ...............................  14
# Diners Club - International   36 .........................................................  14
# Diners Club - USA & Canada    54 .........................................................  16
# Discover ..................   6011, 622126 to 622925, 644, 645, 646, 647, 648, 649, 65 ...  16-19
# InstaPayment ..............   637, 638, 639 ..............................................  16
# JCB .......................   3528 to 3589 ...............................................  16-19
# Maestro ...................   5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763 .......  16-19
# MasterCard ................   51, 52, 53, 54, 55, 222100-272099 ..........................  16
# Visa ......................   4 ..........................................................  13-16-19
# Visa Electron .............   4026, 417500, 4508, 4844, 4913, 4917 .......................  16
#
# ______________________________________________________________________________________________________________________
#
# Test Card Numbers
# ______________________________________________________________________________________________________________________
#
# American Express ..........   346670120314698    344250847513385    346820169192865
# Diners Club - Carte Blanche   30597994646759     30396586831709     30287405677086
# Diners Club - International   36787559490388     36852058606197     36302552850008
# Diners Club - USA & Canada    5593851839825849   5486165300355016   5556271903957771
# Discover ..................   6011890688900222   6011028044966849   6011644174791364389
# InstaPayment ..............   6395513970325942   6371166876186153   6386402144476826
# JCB .......................   3540377950273782   3532065321740205   3540614149080877918
# Maestro ...................   6761190805824872   6304159001213101   5038487976042725
# MasterCard ................   5543469062264627   5389688415680745   2720997617128477
# Visa ......................   4485636321431121   4556447302849370   4716541217957882296
# Visa Electron .............   4913713744594363   4844135973420603   4508734969425126

def main(debug):

    validate_ccn = True

    while validate_ccn:

        if not debug:
            clear_screen()

        print(" Welcome to Credit Card Number Validator")
        print('\n')

        # display the credit card issuer
        display_ccn_issuers(debug)

        ################################################################
        #
        #  1. SELECT A CCN ISSUER
        #
        ################################################################
        ccn_issuer = select_ccn_issuer(debug)

        ################################################################
        #
        #  2. CREATE A CCN ISSUER OBJECT
        #
        ################################################################
        ccn_issuer_object = create_ccn_issuer_object(debug, ccn_issuer)

        ################################################################
        #
        #  3. USER DECIDES IF ISSUER TEST CCN TO BE USED
        # 
        #     
        #
        ################################################################

        # use_test_ccn will be assigned True or False
        # if True - user decided to use a test_ccn and ccn will be assigned a valid test_ccn
        # if False - user decided not to use a test_ccn and ccn will be assigned '' <empty string>
        use_test_ccn, ccn = will_test_ccn_be_used(debug, ccn_issuer, ccn_issuer_object)

        ################################################################
        #
        #  4. USER PROVIDES CCN
        #     
        #     IF TEST CCN IS NOT USED IN STEP 3. ABOVE
        #
        ################################################################

        # check to see if user decided to use a test_ccn
        if not use_test_ccn:

            # call user_provided_ccn()
            ccn = user_provided_ccn(debug, ccn_issuer, ccn_issuer_object)


        ################################################################
        #
        #  5. VALIDATE CCN IS A CCN ISSUER VALID NUMBER
        #    
        ################################################################

        is_starts_with_and_length_valid = validate_ccn_starts_with_and_length(debug, ccn, ccn_issuer, ccn_issuer_object)

        if is_starts_with_and_length_valid:
            ccn_issuer_object.ccn_minus_last_digit = ccn[:-1]
            ccn_issuer_object.last_digit = ccn[-1:]

            ccn_issuer_object.calculate_checksum()

            if not debug:
                clear_screen()

            # format CCN for display purposes
            display_ccn = format_ccn_for_display(debug, ccn)

            # call ccn_valid_banner() to announce if CCN is valid or not
            ccn_valid_banner(debug, ccn_issuer, display_ccn, ccn_issuer_object.ccn_valid)
            
            print('\n')
            input(" Press Enter to continue")
            print('\n')

        else:
            print(" Credit Card {} does not have proper format or length is NOT VALID".format(ccn))
            print('\n')
            input(" Press Enter to continue")


        ################################################################
        #
        #  X. VALIDATE ANOTHER CCN
        #   
        ################################################################
        # validate_another_ccn_number() will return True or False
        # the while loop will continue  if True
        # the while loop will terminate if False     
        validate_ccn = validate_another_ccn_number(debug)

    print(" Thank you for using Credit Card Number Validator!")

# **** End of function main() **** #

debug = False

main(debug)
