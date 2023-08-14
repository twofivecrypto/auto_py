#! python3
#mapIt.py - launches a map in the browser using clipboard address

import webbrowser, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    #TODO; DOWNLOAD PYPERCLIP for REST OF TUTORIAL