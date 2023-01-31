from datetime import datetime 
from datetime import date
current_date = datetime.now()
current_date.isoformat()

birthdays = {
'matt': date(1984, 1, 31),
'josh': date(1982, 9, 29),
'bob': date(1962, 10, 22),
'chris': date(1964, 2, 15),
'adam': date(1966, 9, 9),
'norm': date(1959, 10, 17),
'sarah': date(1970, 12, 1)
}

for item in birthdays.keys():
    td = date.today() - birthdays[item]
    print(f'{item}: {birthdays[item]}, {td.days} days old')
