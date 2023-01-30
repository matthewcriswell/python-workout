PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(people):
    ''' takes a people list and returns a formatted string '''
    fmt_str = ''
    for person in people:
        fmt_str = fmt_str + f'{person[1]:10s} {person[0]:10s} {person[2]:5.2f}\n'
    return fmt_str

print(format_sort_records(PEOPLE), end='')
