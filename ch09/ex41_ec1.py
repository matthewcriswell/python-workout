''' envelope class '''


class Envelope():
    ''' creates an envelop object '''

    postage_rate = 10

    def __init__(self, weight, was_sent=False):
        self.weight = weight
        self.was_sent = was_sent
        self.postage_balance = 0

    def send(self):
        ''' if sufficient credit, set was_sent to True '''
        if self.postage_balance >= self.postage_needed():
            print("Message sent")
            self.was_sent = True
        else:
            print("Insufficient credit")

    def add_postage(self, credit):
        ''' adds credit to post_balance '''
        self.postage_balance += credit

    def postage_needed(self):
        ''' calculates required postage based on weight and rate '''
        return self.weight * self.postage_rate


class BigEnvelop(Envelope):
    ''' creates a big envelop with a different postage_rage '''

    postage_rate = 15
