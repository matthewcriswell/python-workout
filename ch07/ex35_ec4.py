'''
Create a dict whose keys are city names, and whose values are temperatures in Fahrenheit. Now use a dict comprehension to transform this dict into a new one, keeping the old keys but turning the values into the temperature in degrees Celsius.
'''


CITIES_TEMP = {'dallas': 101, 'austin':99, 'san antonio': 100, 'lubbock':95, 'houston': 104, 'el paso':109}

def fahr_to_cel(temp):
    ''' convert fahrenheit to celcius '''
    return round((temp-32)/1.8, 2)


print(CITIES_TEMP)
CITIES_TEMP = {k:fahr_to_cel(v) for k,v in CITIES_TEMP.items()}
print(CITIES_TEMP)
