from operator import itemgetter

def sort_inner(sequence):
    transformed_list = []
    calculated = {}
    for inner_list in sequence:
        if inner_list:
            calculated = {
                'list': inner_list,
                'sum': sum(inner_list)
            }
            transformed_list.append(calculated)
    return transformed_list

nums = [[2,2,3,4],[3,4,5,9,100],[100,101,102,103,104], []]
sums = sort_inner(nums)
print(sorted(sums, key=itemgetter('sum')))
