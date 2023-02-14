'''
area code changer
'''

def shift_area_code(phone_numbers):
    ''' takes a list of phone numbers, increments the area code and returns the list '''
    split_nums = [number.split('-') for number in phone_numbers]
    for i in split_nums:
        if i[1][0] in '012345':
            i[0] = str(int(i[0])+1)
    zip_nums = ['-'.join(number) for number in split_nums]
    output = zip_nums
    return output
