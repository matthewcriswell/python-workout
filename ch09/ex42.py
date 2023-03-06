''' flexibledict '''


class FlexibleDict(dict):
    ''' inherits dict and extends it to be a little more forgiving with key values '''

    def __getitem__(self, key):
        if isinstance(key, int):
            try:
                return super().__getitem__(key)
            except:
                return super().__getitem__(str(key))
        if isinstance(key, str):
            if key.isdigit():
                try:
                    return super().__getitem__(int(key))
                except:
                    return super().__getitem__(key)
        return super().__getitem__(key)
