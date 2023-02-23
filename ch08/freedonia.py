'''
provides calculate_tax() and supporting functions
'''
from decimal import Decimal

class HourTooLowError(Exception): pass
class HourTooHighError(Exception): pass

PROVINCE_TAX_RATE = {
    'chico': Decimal('.5'),
    'groucho': Decimal('.7'),
    'harpo': Decimal('.5'),
    'zeppo': Decimal('.4')
}

def calculate_tax(purchase_price, province, hour):
    ''' calculate tax and return total value '''
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is less than 0')
    if hour > 24:
        raise HourTooHighError(f'Hour of {hour} is greater than 24')
    
    return purchase_price + (purchase_price *
                             PROVINCE_TAX_RATE[province.lower()] * hour /
                             Decimal('24'))
