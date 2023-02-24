'''  a module providing a function that, given a string, returns a dict indicating how many characters provide a True result to each of the following functions: str.isdigit, str.isalpha, and str.isspace. The keys should be isdigit, isalpha, and isspace '''


def string_analyzer(my_string):
    ''' analyzes a string and returns a dict '''
    output = {'isdigit': 0, 'isalpha': 0, 'isspace': 0}
    for i in my_string:
        if i.isdigit():
            output['isdigit'] += 1
        if i.isalpha():
            output['isalpha'] += 1
        if i.isspace():
            output['isspace'] += 1
    return output
