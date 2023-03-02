''' Transaction class with depots and withdrawals '''


class Transaction():
    ''' creates a transaction object and modifies class account_balance '''
    account_balance = 0

    def __init__(self, amount):
        Transaction.account_balance += amount
