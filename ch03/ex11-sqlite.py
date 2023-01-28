import sqlite3

con = sqlite3.connect("people-test.db")
cur = con.cursor()
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='people' ''')

if cur.fetchone()[0]==1 : {
	print('Table exists.')
}

else:
    cur.execute("CREATE TABLE people(first, last, email)")
    cur.execute("""
        INSERT INTO people VALUES
            ('James','Estes','jestes@teleworm.us'),
            ('Kenneth','Allen','kallen@dayrep.com'),
            ('Andrew','Hernandez','ahernandez@teleworm.us'),
            ('Frankie','Lemke','rborer@yahoo.com'),
            ('Christ','Collins','krajcik.lonny@satterfield.biz'),
            ('Vallie','Stokes','hoppe.maddison@gmail.com'),
            ('Hardy','Green','tobin.mueller@hotmail.com'),
            ('Lucienne','McKenzie','marjolaine23@kihn.com'),
            ('Norma','Dickens','tiana60@frami.org'),
            ('Gonzalo','Mosciski','xvandervort@zieme.com'),
            ('Jarrod','Legros','sabryna59@fritsch.com'),
            ('Savion','Collier','shyann98@gmail.com')
    """
    )
    print('Initializing table.')
    con.commit()
  

res = cur.execute("SELECT first,last,email FROM people")
r = res.fetchall()
people_list = []
for person in r: 
    people_list.append({'first':person[0],'last':person[1],'email':person[2]})

from operator import itemgetter
def alphabetize_names(people_list):
    people = sorted(people, key=itemgetter('last','first')) 
    return people
