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
Movie = namedtuple('Movie',['title','length','director_firstname','director_lastname'])
for movie in MOVIES:
    title = movie[0]
    length = movie[1]
    director = movie[2].split()[0]
    movies.append(
        Movie(
            movie[0],
            movie[1],
            movie[2].split()[0],
            #str(movie[2].split()[1:])
            ' '.join(name for name in (movie[2].split()[1:]))
        )
    )

print("2022 Academy best picture nominees.")
print("Sort by - 'title', 'director_lastname', 'director_firstname', 'length'")
myBool = True
while myBool:
    user_input = input("Sort by (comma seperate list): ")
    myBool = False
    user_input_list =  user_input.split(',')

if user_input_list:
    for item in sorted(movies, key=attrgetter(*user_input_list)):
        print(f"{item.title:25} {item.director_lastname + ',' + ' ' +  item.director_firstname:25} {item.length:5}")
