# Reference http://urwid.org/tutorial/
#THIS MODULE WILL NOT WORK IN WINDOWS BECAUSE OF FCNTL.
#FCNTL IS UNIX SPECIFIC. NOT AVAILABLE FOR WINDOWS>

import urwid

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
loop.run()