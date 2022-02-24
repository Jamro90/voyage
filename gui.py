from tkinter import *
import tkinter.ttk
from commands import *
from update import *

font_name = "arial"
font_size = 10

def start_window(ver, update):
    # window default settings
    win = Tk()
    win.geometry("500x300+300+300")
    win.title("Voyage " + ver)

    title_label = Label(win, text = "Voyage " + ver, font = (font_name, font_size))
   
    # check for updates
    check_value = IntVar()
    check_label = Label(win, text = "Update:", font = (font_name, font_size))
    check = Checkbutton(win, onvalue = 1, offvalue = 0, variable = check_value, state = NORMAL)
    
    # buttons

    def next_window(event = ""):
        main_window(ver, check_value, win)
    win.bind("<Return>", next_window)

    next_bnt = Button(win, text = "Start", command = lambda: main_window(ver, check_value, win))
    exit_bnt = Button(win, text = "Wyjdź", command = win.destroy)

    update_label = Label(win, text = "ostatnia aktualizacja: " + update, font = (font_name, font_size))
    # display settings
    title_label.grid(column = 10, row = 10, padx = 5, pady = 5)
    check_label.grid(column = 10, row = 20, padx = 5, pady = 5)
    check.grid(column = 20, row = 10, padx = 5, pady = 5)
    next_bnt.grid(column = 30, row = 30, padx = 5, pady = 5)
    exit_bnt.grid(column = 20, row = 30, padx = 5, pady = 5)
    update_label.grid(column = 40, row = 40, padx = 5, pady = 5)
    win.mainloop()

def main_window(ver, check_value, win):
    # kill previous window
    win.destroy()
    
    # check for updates
    if check_value == 1:
        update()
    
    # defaults settings
    window = Tk()
    window.title("Voyage " + ver)
    window.geometry("800x800+100+100")

    # menu config
    menu_obj = Menu(window)

    # chapter file
    file = Menu(menu_obj, tearoff = 0)
    menu_obj.add_cascade(label = "Plik", menu = file)
    file.add_command(label = "Importuj dane Ctrl+i", command = lambda: import_data(data))
    file.add_command(label = "Zapisz jako Ctrl+s", command = lambda: save_as(data))
    file.add_separator()
    file.add_command(label = "Wyjdź ESC", command = window.destroy)

    edit = Menu(menu_obj, tearoff = 0)
    menu_obj.add_cascade(label = "Zmień", menu = edit)
    edit.add_command(label = "Zaznacz wszystko Ctrl+a", command = lambda:check_all())
    edit.add_command(label = "odznacz wszystko Ctr+o", command = lambda:uncheck_all())

    # shortcuts
    def short_import_data(event = ""):
        import_data(data)
    window.bind("<Control-i>", short_import_data)
    
    def short_save_as(event = ""):
        save_as(data)
    window.bind("<Control-s>", short_save_as)
   
    def exit(event = ""):
        window.destroy()
    window.bind("<Escape>", exit)

    def short_check_all(eveny = ""):
        check_all()
    window.bind("<Control-a>", short_check_all)

    def short_uncheck_all(event = ""):
        uncheck_all()
    window.bind("<Control-o>", short_uncheck_all)
   
    # new working plane

    frame = Frame(window)
    id_label = Label(frame, text = "Lp.", font = (font_name, font_size))
    name_label = Label(frame, text = "imię", font = (font_name, font_size))
    surname_label = Label(frame, text = "nazwisko", font = (font_name, font_size))
    date_from_label = Label(frame, text = "od", font = (font_name, font_size))
    date_to_label = Label(frame, text = "do", font = (font_name, font_size))
    check_label = Label(frame, text = "wyprowiantowany", font = (font_name, font_size))


    # display settings
    id_label.grid(column = 10, row = 10, padx = 25, pady = 5)
    name_label.grid(column = 20, row = 10, padx = 25, pady = 5)
    surname_label.grid(column = 30, row = 10, padx = 25, pady = 5)
    date_from_label.grid(column = 40, row = 10, padx = 25, pady = 5)
    date_to_label.grid(column = 50, row = 10, padx = 25, pady = 5)
    check_label.grid(column = 60, row = 10, padx = 25, pady = 5)


    frame.pack()
    window.config(menu = menu_obj)
    window.mainloop()

    
