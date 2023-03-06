''' RecentDict class '''

from collections import UserDict


class RecentDict(UserDict):
    ''' implements a dict like object which holds
    the N most recent entries (where N is selectable) '''

    def __init__(self, max_len):
        self._max_len = max_len
        self.keys_pipe = []
        super().__init__()

    @property
    def max_len(self):
        ''' mex_len is the max number of objects allowed '''
        return self._max_len

    def pop_off(self):
        ''' deletes an entry from the dict and the pipe '''
        popper = self.keys_pipe.pop(0)
        del self[popper]

    def pop_forward(self):
        ''' pushes an entry to the front of the pipe without deleting it '''
        popper = self.keys_pipe.pop(0)
        self.keys_pipe.append(popper)

    @max_len.setter
    def max_len(self, value):
        ''' mex_len setter checks for int value and pops off entries if needed '''
        if not isinstance(value, int):
            raise TypeError('Expected int')
        if self._max_len > value:
            pipe_diff = self._max_len - value
            for _ in range(pipe_diff):
                self.pop_off()
        self._max_len = value

    def __setitem__(self, key, value):
        if len(self.keys()) < self.max_len:
            # we can freely append
            self.keys_pipe.append(key)
            super().__setitem__(key, value)
        else:
            # check if key already exists
            if key in self.keys():
                self.pop_forward()
                super().__setitem__(key, value)
            else:
                self.keys_pipe.append(key)
                self.pop_off()
                super().__setitem__(key, value)


if __name__ == '__main__':
    print("tests")

    a = RecentDict(5)
    a[1] = 1
    a[2] = 2
    a[3] = 3
    a[4] = 4
    a[5] = 5
    a[6] = 6
    a[7] = 7
    a[8] = 8
    a[9] = 9
    a[10] = 10
    print("Current contents:")
    for i in a:
        print(f'{a[i]}')
    print(f"Current max_len is {a.max_len}")
    print("Setting max_len to 3")
    a.max_len = 3

    a[1] = 1
    a[2] = 2
    a[3] = 3
    a[4] = 4
    a[5] = 5
    a[6] = 6
    a[7] = 7
    a[8] = 8
    a[9] = 9
    a[10] = 10
    print("Current contents:")
    for i in a:
        print(f'{a[i]}')
