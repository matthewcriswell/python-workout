''' FlatList class for flattening lists '''
from collections.abc import Sequence


class FlatList(list):
    ''' a list type which automatically flattens any sequences '''

    def append(self, value):
        if isinstance(value, Sequence):
            for item in value:
                super().append(item)
        else:
            super().append(value)
