'''
Create a dict whose keys are currency names and whose values are the price of that currency in U.S. dollars. Write a function that asks the user what currency they use, then returns the dict from the previous exercise as before, but with its prices converted into the requested currency.
'''

exchange_rate = {
    'peso': 18.36,
    'euro': .93,
    'yen': 134.11,
    'ruble': 74.00,
    'usd': 1.00
}


def exchange_currency():
    ''' convert exchange rate dict '''
    user_cur = input("What currency do you use?")
    return {
        k: round(v / exchange_rate[user_cur], 3)
        for k, v in exchange_rate.items()
    }
