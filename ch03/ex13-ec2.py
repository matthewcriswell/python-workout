from collections import namedtuple
from operator import attrgetter

# name, length (in minutes), and director of the movies nominated for best picture
MOVIES = [
('CODA', 111, 'Sian Heder'),
('Bellfast', 97, 'Kenneth Branagh'),
("Don't Look Up", 138, 'Adam McKay'),
('Drive My Car', 179, 'Ryusuke Hamaguchi'),
('Dune', 156, 'Denis Villeneuve'),
('King Richard', 145, 'Reinaldo Marcus Green'),
('Licorice Pizza', 133, 'Paul Thomas Anderson'),
('Nightmare Alley', 150, 'Guillermo del Toro'),
('The Power of the Dog', 126, 'Jane Campion'),
('West Side Story', 156, 'Steven Spielberg')
]

movies = []
Movie = namedtuple('Movie',['title','length','director'])
for movie in MOVIES:
    movies.append(Movie(movie[0],movie[1],movie[2]))

USER_SELECTION = ''
print("2022 Academy best picture nominees.")
print("Sort by - (1) Title (2) Director (3) Length")
while True:
    USER_SELECTION = input("Selection: ")
    if USER_SELECTION == '1':
        SORT_STYLE = 'title'
        break
    if USER_SELECTION == '2':
        SORT_STYLE = 'director'
        break
    if USER_SELECTION == '3':
        SORT_STYLE = 'length'
        break
    else:
        print("Invalid selection")

if SORT_STYLE:
    for item in sorted(movies, key=attrgetter(SORT_STYLE)):
        print(f"{item.title:25} {item.director:25} {item.length:5}")
    #print(sorted(movies, key=attrgetter('length')))
    #print(sorted(movies, key=attrgetter('director')))
