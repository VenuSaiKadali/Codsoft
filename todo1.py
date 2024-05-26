from tkinter import *
def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height = listbox.size())
    entry.delete(0,END)
def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height = listbox.size())
    
window = Tk()
window.geometry("700x700")
window.title("TO DO LIST")
label1 = Label(window,
              text = "To - Do List",
              font = ("Courier",30,"italic"),
              fg = "black",
              bg = "yellow",
              width = 100,
              height = 3,
              relief = RAISED
              )
label1.pack()

label2 = Label(window,
               text = "Add Items :",
               font = ("Courier",30),
               fg = "red"
               )
label2.place(x=10,y=150)

entry = Entry(window,
              font = ("Courier",25),
              fg = "black"
              )
entry.place(x=10,y=200)

addbutton = Button(window,
                   text = "Add task",
                   bg = "orange",
                   fg="black",
                   font = ("Courier",14),
                   command = add,
                   relief = RAISED,
                   bd = 5
                      )
addbutton.place(x=420,y=200)

deletebutton = Button(window,
                      text = "remove",
                      bg = "pink",
                      fg="black",
                      font = ("Courier",13),
                      command = delete,
                      relief = RAISED,
                      bd = 5
                      )
deletebutton.place(x=550,y=200)


label3 = Label(window,
               text = "Tasks to do",
               font = ("Courier",30),
               fg = "blue"
               )
label3.place(x=300,y=250)


listbox = Listbox(window,
                  width = 100,
                  fg = "black",
                  font = ("Courier",30),
                  bg = "lightgrey"
                  )
listbox.place(x=10,y=320)
               

window.mainloop()
