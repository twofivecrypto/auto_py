#! python3
#mcb.pyw - Saves and loads pices of text to the clipboard
#Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       pyl.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

#TODO: Save clipboard content.
#TODO: List keyowars and load content.

mcbShelf.close()