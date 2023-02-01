"""
high level support for doing this and that.
"""

FILE_NAME = 'dns_capture.txt'


def num_sum(filename, whack_sum=False):
    ''' seeks over a text file looking for numbers and returning their sum '''
    nums = []
    with open(filename, 'rt', encoding='UTF-8') as file:
        for line in file.readlines():
            for word in line.split():
                if whack_sum:
                    # try to filter out control characters in words
                    word = ''.join([char for char in word if char.isalnum()])
                if word.isdigit():
                    nums.append(word)
    mysum = sum(int(num) for num in nums)
    return mysum


the_sum = num_sum(FILE_NAME, whack_sum=True)
print(f"Whacky sum: {the_sum}")

the_sum = num_sum(FILE_NAME)
print(f"Lame sum: {the_sum}")
