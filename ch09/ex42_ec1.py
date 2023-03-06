''' StringDictKey: dicts where keys converted to strings '''

class StringDictKey(dict):
    ''' like a dict but always convert keys into strings '''
    def __setitem__(self, key, value):
        key = str(key)
        super().__setitem__(key, value)
