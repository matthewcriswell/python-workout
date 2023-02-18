'''
Create a list of tuples in which each tuple contains three elements: (1) the author’s first and last names, (2) the book’s title, and (3) the book’s price in U.S. dollars. Use a dict comprehension to turn this into a dict whose keys are the book’s titles, with the values being another (sub -) dict, with keys for (a) the author’s first name, (b) the author’s last name, and (c) the book’s price in U.S. dollars.
'''
book_list = [('Kurt Vonnegut', 'Slaughterhouse-Five: A Novel', 14.39),
             ('Joseph Heller', 'Catch-22', 10.99),
             ('James Joyce', 'Ulysses', 10.99),
             ('Kurt Vonnegut', 'Cat\'s Cradle: A Novel', 14.99)]

#{entry[1]:{'first':entry[0].split()[0],'last':entry[0].split()[1],'price':entry[2]} for entry in book_list}
new_dict = {
    item[0]: item[1]
    for item in [(entry[1], {
        'first_name': name[0],
        'last_name': name[1],
        'price_usd': entry[2]
    }) for name, entry in [(entry[0].split(), entry) for entry in book_list]]
}
