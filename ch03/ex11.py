from operator import itemgetter
def alphabetize_names(people):
    people = sorted(people, key=itemgetter('last','first')) 
    for person in people:
        print(f"{person['last']}, {person['first']}: {person['email']}")
    return people
