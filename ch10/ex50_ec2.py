#import the os module
import os


#define mychain which accetps a sequence of arguments
def mychain(*args):
    #for each argument from the pass in arguments
    for arg in args:
        #for each item in a given argument
        for item in arg:
            #yield the item as a generator
            yield item


#function that accepts a pathname as an arg
def all_lines(path):
    #utilize my chain by using a generator to combine the path with each file in the path, if it's a file pass it in
    return mychain(*(open(os.path.join(path, filename))
                     for filename in os.listdir(path)
                     if os.path.isfile(os.path.join(path, filename))))

for i in all_lines('./test_dir'):
    print(i)
