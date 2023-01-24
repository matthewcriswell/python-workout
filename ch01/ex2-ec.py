def varfunc(nums_list, opti_add=0):
    return (nums_list, opti_add)

def mysum(*args):
    sum = 0
    args_list = list(args)
    for i in args_list:
        sum += int(i)
    return sum


def mysum2(nums_list, opt_add=0):
    sum = 0

    try:
        for item in nums_list:
            sum += int(item)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
      
    try:
        sum += opt_add
    except TypeError as e:
        print(f"Error: {e}")
    return sum

def myavg(nums_list):
    avg = 0
    count = 0
    total = 0
    for item in nums_list:
       total += item
       count += 1
    avg = total / count 
    print(f"avg: {avg}, total: {total}, count: {count}")
    return avg
   


def wordsfunc(words_list):
    print("wordsfunc") 
    words_total = 0
    words_len_total = 0
    shortest_len = -1
    longest_len = 0
    shorest_word = ''
    longest_word = ''
    for word in words_list:
        words_total += 1 

        word_len = len(word)
        words_len_total += word_len

        if shortest_len == -1:
            shortest_len = word_len
            shortest_word = word
        elif word_len < shortest_len:
            shortest_len = word_len 
            shortest_word = word
        else:
            pass

        if word_len > longest_len:
            longest_len = word_len
            longest_word = word
        
    avg_len = words_len_total/words_total
    print(f"Longest word: {longest_word}, at {longest_len} chars.  Shortest word: {shortest_word}, at {shortest_len} chars")
    print(f"Average word length: {avg_len}")
    print(f"{words_len_total}")

def objectsfunc(*args):
    args_list = list(args) 
    total = 0
    for thing in args_list:
        try:
            num = int(thing)
            total += num
        except:
            pass
    
    return total
