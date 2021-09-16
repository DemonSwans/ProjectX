'''
import string
haslo = "Kutas@12"
haslo_powt = "kutas@12"
special_characters = string.punctuation
DB_NAME = "database.db"
tfhaslo = list(map(lambda char: char in special_characters, haslo))

if not(haslo.islower() == False and haslo.isupper()== False):
    print("huj")
else:
    print("gj")

if not(any(map(str.isdigit, haslo))):
    print("huj")
else:
    print("gj")

if False:
    print('To nie email')
elif len(haslo) < 7 or not (haslo.islower() == False and haslo.isupper() == False) or not any(tfhaslo) or not (any(map(str.isdigit, haslo))) :
    print('Błędne hasło')
elif haslo != haslo_powt:
    print('Hasła nie są identyczne')
else:
    print("Utworzono Konto")

import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

difference_in_years = relativedelta(date.today(), datetime.datetime(1950,1,1)).years

print(date.today())
print(difference_in_years)
'''

import os
x = "kutas"
path = os.getcwd()
print(fr'{path}\Users_data')
os.chdir(fr'{path}\website\Users_data')
os.mkdir(x)
os.chdir(path)
print(os.getcwd())