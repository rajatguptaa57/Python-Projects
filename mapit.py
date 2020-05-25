# Script for Searching a Location from Google Maps from Terminal

import webbrowser, sys, pyperclip


sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

#Check if command line arguments are passed
if len(sys.argv) > 1:
     # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valenica St.'
     address = '  '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
    
