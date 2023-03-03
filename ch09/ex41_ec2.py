''' phone class with subclasses '''


class Phone():
    ''' creates a phone object with a dial method '''

    dial_string = "Dialing out..."

    def __init__(self):
        pass

    def dial(self):
        print(self.dial_string)


class SmartPhone(Phone):
    ''' creates a phone with apps '''

    app_string = "Running app"

    def run_app(self):
        print(self.app_string)


class iPhone(SmartPhone):
    ''' creates the coolest phone '''

    def __init__(self):
        self.dial_string = Phone.dial_string.lower()
        self.app_string = SmartPhone.app_string.lower()
