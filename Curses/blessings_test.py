#THIS MODULE WILL NOT WORK IN WINDOWS BECAUSE OF FCNTL.
#FCNTL IS UNIX SPECIFIC. NOT AVAILABLE FOR WINDOWS>

from blessings import Terminal

term = Terminal()
with term.location(0, term.height - 1):
    print('This is', term.underline('pretty!'))