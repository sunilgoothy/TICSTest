from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
# lbl = Label(window, text="Hello")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')

lbl1 = Label(tab1, text= 'label1', font=("Arial Bold", 10))
lbl1.grid(column=0, row=0)

txt = Entry(tab1,width=10)
txt.grid(column=1, row=0)
txt.focus()

def clicked():
    res = "Welcome to " + txt.get()
    lbl1.configure(text= res)

btn = Button(tab1, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

combo = Combobox(tab1)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=1)

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(tab1, text='Choose', var=chk_state)

chk.grid(column=0, row=2)

lbl2 = Label(tab2, text= 'label2', font=("Arial Bold", 25))
lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()