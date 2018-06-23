import random

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
# Diners Club - Carte Blanche	300, 301, 302, 303, 304, 305 ...............................  14
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

class CreditCard():

    # The Luhn Formula:
    # 1. Drop the last digit from the number. The last digit is what we want to check against
    # 2. Reverse the numbers
    # 3. Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
    # 4. Add all the numbers together
    # 5. The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10 (Modulo 10)

    # credit card class
    def __init__(self, debug):

        self.debug = debug
        self.ccn   = ''        # ccn is Credit Card Number

        self.ccn_minus_last_digit         = ''
        self.last_digit                   = ''

        self.ccn_valid = False

    # **** End of CreditCard() method __init__() **** #


    def set_ccn(self, ccn):   # ccn credit card number

        self.ccn = ccn

    # **** End of CreditCard.set_ccn() **** #


    def minus_last_digit(self):   # ccn credit card number

        self.ccn_minus_last_digit = self.ccn[:-1]

    # **** End of CreditCard.minus_last_digit() **** #


    def last_digit(self):

    	self.last_digit = self.ccn[-1:]

    # **** End of CreditCard.last_digit() **** #


    def calculate_checksum(self):

        '''
        1. Reverse the numbers
        2. Multiply the digits in odd positions (1, 3, 5, etc.) by 2
        3. subtract 9 to all any result higher than 9
        4. Add all the numbers together
        5. The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10 (Modulo 10)
        '''

        # 1. reverse the numbers
        reverse = self.ccn_minus_last_digit[::-1]
        reverse_iter = iter(reverse)

        num = 0

        # 2. Multiply the digits in odd positions (1, 3, 5, etc.) by 2 
        # 3. subtract 9 to all any result higher than 9
        # 4. Add all the numbers together
        for i in range(len(reverse)):

            # 2. Multiply the digits in odd positions (1, 3, 5, etc.) by 2subtract 9 to all any result higher than 9
            if i == 0 or i % 2 == 0:
                x = 2 * int(next(reverse_iter))

            else:
                x = int(next(reverse_iter))

            # 3. subtract 9 to all any result higher than 9
            if x > 9:
                x -= 9

            # 4. Add all the numbers together
            num += x

        # 5. The check digit (the last number of the card) is the amount that you would
        #    need to add to get a multiple of 10 (Modulo 10)
        add_check_digit_num = num + int(self.last_digit)

        if add_check_digit_num % 10 == 0:
        	self.ccn_valid = True

    # **** End of CreditCard.calculate_checksum() **** #


    def shuffle_vaid_test_nums(self, valid_test_nums):

        for i in range (10):
            random.shuffle(self.valid_test_nums)

    # **** End of CreditCard() method shuffle_vaid_test_nums() **** #


    def shuffle_invalid_test_nums(self, valid_test_nums):

        for i in range (10):
            random.shuffle(self.invalid_test_nums)

    # **** End of CreditCard() method shuffle_invalid_test_nums() **** #


class AmericanExpress(CreditCard):

    # American Express credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = ['34', '37']
        self.range       = []
        self.length      = ['15']
        self.valid_test_nums     = ['346670120314698', '344250847513385', '346820169192865']
        self.invalid_test_nums   = ['346670120314699', '344250847513386', '346820169192866']

        CreditCard.__init__(self, self.debug)

    # **** End of AmericanExpress() method __init__() **** #


class DinersClub_CB(CreditCard):    # Diners Club - Carte Blanche

    # Diners Club - Carte Blanche credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = ['300', '301', '302', '303', '304', '305']
        self.range       = []
        self.length      = ['14']
        self.valid_test_nums     = ['30597994646759', '30396586831709', '30287405677086']
        self.invalid_test_nums   = ['30597994646758', '30396586831708', '30287405677087']

        CreditCard.__init__(self, self.debug)

    # **** End of DinersClub_CB() method __init__() **** #


class DinersClub_Int(CreditCard):    # Diners Club - International

    # Diners Club - International credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = ['36']
        self.range       = []
        self.length      = ['14']
        self.valid_test_nums     = ['36787559490388', '36852058606197', '36302552850008']
        self.invalid_test_nums   = ['36787559490389', '36852058606198', '36302552850009']

        CreditCard.__init__(self, self.debug)

    # **** End of DinersClub_Int() method __init__() **** #


class DinersClub_NA(CreditCard):    # Diners Club - USA and Canada (North America)

    # Diners Club - USA and Canada (North America) credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = ['54']
        self.range       = []
        self.length      = ['16']
        self.valid_test_nums     = ['5593851839825849', '5486165300355016', '5556271903957771']
        self.invalid_test_nums   = ['5593851839825848', '5486165300355017', '5556271903957772']

        CreditCard.__init__(self, self.debug)

    # **** End of DinersClub_NA() method __init__() **** #


class Discover(CreditCard):

    # Discover credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = ['6011', '644', '645', '646', '647', '648', '649', '65']
        self.range       = ['622126', '622925']
        self.length      = ['16', '19']
        self.valid_test_nums     = ['6011890688900222', '6011028044966849', '6011644174791364389']
        self.invalid_test_nums   = ['6011890688900223', '6011028044966848', '6011644174791364388']

        CreditCard.__init__(self, self.debug)

    # **** End of Discover() method __init__() **** #


class InstaPayment(CreditCard):

    # InstaPayment credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = ['637', '638', '639']
        self.range       = []
        self.length      = ['16']
        self.valid_test_nums     = ['6395513970325942', '6371166876186153', '6386402144476826']
        self.invalid_test_nums   = ['6395513970325943', '6371166876186154', '6386402144476827']

        CreditCard.__init__(self, self.debug)

    # **** End of InstaPayment() method __init__() **** #


class JCB(CreditCard):

    # JCB credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = []
        self.range       = ['3528', '3589']
        self.length      = ['16', '19']
        self.valid_test_nums     = ['3540377950273782', '3532065321740205', '3540614149080877918']
        self.invalid_test_nums   = ['3540377950273783', '3532065321740206', '3540614149080877919']

        CreditCard.__init__(self, self.debug)

    # **** End of JCB() method __init__() **** #


class Maestro(CreditCard):

    # Maestro credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']
        self.range       = []
        self.length      = ['16', '19']
        self.valid_test_nums     = ['6761190805824872', '6304159001213101', '5038487976042725']
        self.invalid_test_nums   = ['6761190805824873', '6304159001213102', '5038487976042726']

        CreditCard.__init__(self, self.debug)

    # **** End of Maestro() method __init__() **** #


class MasterCard(CreditCard):

    # MasterCard credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = ['51', '52', '53', '54', '55']
        self.range       = ['222100', '272099']
        self.length      = ['16']
        self.valid_test_nums     = ['5543469062264627', '5389688415680745', '2720997617128477']
        self.invalid_test_nums   = ['5543469062264628', '5389688415680746', '2720997617128478']

        CreditCard.__init__(self, self.debug)

    # **** End of MasterCard() method __init__() **** #


class Visa(CreditCard):

    # Visa credit card class
    def __init__(self, debug):

        self.debug       = debug

        self.starts_with = ['4']
        self.range       = []
        self.length      = ['13', '16', '19']
        self.valid_test_nums     = ['4485636321431121', '4556447302849370', '4716541217957882296']
        self.invalid_test_nums   = ['4485636321431122', '4556447302849371', '4716541217957882297']

        CreditCard.__init__(self, self.debug)

    # **** End of Visa() method __init__() **** #


class VisaElectron(CreditCard):

    # VisaElectron credit card class
    def __init__(self, debug):

        self.debug       = debug
        self.starts_with = ['4026', '417500', '4508', '4844', '4913', '4917']
        self.range       = []
        self.length      = ['16']
        self.valid_test_nums     = ['4913713744594363', '4844135973420603', '4508734969425126']
        self.invalid_test_nums   = ['4913713744594364', '4844135973420604', '4508734969425127']

        CreditCard.__init__(self, self.debug)

    # **** End of VisaElectron() method __init__() **** #
