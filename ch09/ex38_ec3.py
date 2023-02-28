''' LogFile class '''
class LogFile():
    ''' create a file object '''
    def __init__(self, filename):
        ''' open a file for writing '''
        self.file = open(filename, 'wt', encoding='UTF-8')

log_file = LogFile('test')
print("testing 1, 2, 3", file=log_file.file)
