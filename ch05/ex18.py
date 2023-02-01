def get_file_line(filename):
    ''' opens a text file and returns the last line '''
    with open(filename, 'rt', encoding="utf-8") as file:
        for line in file.readlines():
            last_line = line
    return last_line

print(get_file_line('test.txt'), end='')

from io import StringIO

FAKE_FILE = StringIO('''
Friend? hope for the Guest while you are alive.
Jump into experience while you are alive!
Think... and think... while you are alive.
What you call "salvation" belongs to the time
            before death.

If you don't break your ropes while you're alive,
do you think ghosts will do it after?

The idea that the soul will join with the ecstatic
just because the body is rotten --
that is all fantasy.
What is found now is found then.
If you find nothing now,
you will simply end up with an apartment in the
          City of Death.
If you make love with the divine now, in the next
life you will have the face of satisfied desire.

So plunge into the truth, find out who the Teacher is,
Believe in the Great Sound!

Kabir says this: When the Guest is being searched for,
it is the intensity of the longing for the Guest
that does all the work.

Look at me, and you will see a slave of that intensity. 
''')

for line in FAKE_FILE:
    last_line = line
print(last_line, end='')

