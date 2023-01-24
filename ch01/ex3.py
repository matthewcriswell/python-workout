def mysum(nums):
    i = 0
    total = 0.0
    for num in nums:
        total += num
        i += 1
    return (i, total,)
    
        


def run_timing():
    times = []
    runs = 0
    while True:
        time = input("Enter 10 km run time: ")
        if time == '':
            break
        else:
            try:
                times.append(float(time))
                runs += 1
            except:
                print("Bad value")
    sample_size, total = mysum(times) 
    average = total/runs
    print(f"Average of {average:.2f}, over {runs} runs") 
    
    return times

run_times = run_timing()
