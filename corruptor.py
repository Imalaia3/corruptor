import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('CORrUPTOR', font='starwars'),
       'white', 'on_red', attrs=['bold'])

warn="!!Double Check Your Corrupted File To See If it Worked!!"


cprint(figlet_format('WARNING THIS CANNOT BE UNDONE', font='starwars'),
       'white', 'on_red', attrs=['bold'])


print(warn)
files = ''
files = input("Enter File To Corrupt: ")
corr_lev = input("Enter Corruption level. Recommended 1300: ")


print("Finding File.....")
try:
    file_to_corrupt = open(files, "wb+")
except:
    print("ERROR: During file opening. TIP: CHECK IF YOU TYPED THE FILE CORRECTLY (AND THE FILE EXTENSION")
    exit()
print("Found File!")




print("CORRUPTING:")


for i in range(int(corr_lev)):
    print("." * i)
    file_to_corrupt.write(bytes(i))



print("CORRRUPTED!")