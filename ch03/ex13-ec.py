from collections import namedtuple
from operator import attrgetter
PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Bill', 'Putin', 3.626),
          ('Allison', 'Brie', 2.4),
          ('Jinping', 'Xi', 10.603),
          ('Ham', 'Burglar', 0.3),
          ('Cake', 'Burglar', 0.3),
          ('Jon', 'Hamm', 12.0),
          ('Jon', 'Kimble', 12.0),
          ('Sara', 'Putin', 3.626),
          ('Alison', 'Brie', 2.4),
          ('Jeb', 'Brie', 5.5)]


def format_sort_records(people):
    ''' takes a people list and returns a formatted string '''

    fmt_str = ''
    string_list = []
    Person = namedtuple('Person', ['first', 'last', 'travel_time'])
    people_list = [Person(person[0],person[1],person[2]) for person in people]

    # Sorted last, first
    people_list = sorted(people_list, key=attrgetter('last', 'first'))
    for person in people_list:
        fmt_str = fmt_str + f'{person.last:10s} {person.first:10s} {person.travel_time:5.2f}\n'
    string_list.append(('first_last',fmt_str))
    fmt_str = ''

    # sorted travel_time
    people_list = sorted(people_list, key=attrgetter('travel_time'), reverse=True)
    for person in people_list:
        fmt_str = fmt_str + f'{person.last:10s} {person.first:10s} {person.travel_time:5.2f}\n'
    string_list.append(('travel',fmt_str))
    fmt_str = ''

    # sorted last, travel_time
    people_list = sorted(people_list, key=attrgetter('last', 'travel_time'), reverse=True)
    for person in people_list:
        fmt_str = fmt_str + f'{person.last:10s} {person.first:10s} {person.travel_time:5.2f}\n'
    string_list.append(('last travel',fmt_str))
    fmt_str = ''

    return string_list

print_list = format_sort_records(PEOPLE)

for item in print_list:
    print(item[0])
    print(item[1])
