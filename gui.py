from tkinter import *
from tkinter.ttk import *
import datetime
from commands import *
from update import *
from doc import *
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
        import_window(ver, check_value, win)
    win.bind("<Return>", next_window)

    next_bnt = Button(win, text = "Start", command = lambda: import_window(ver, check_value, win))
    def win_exit(event = ""):
    	win.destroy()
    win.bind("<Escape>", win_exit)
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

def import_window(ver, check_value, window):
    if check_value.get() == 1:
        update()
    pchor_list = import_data()
    main_window(ver, pchor_list)

def main_window(ver, pchor_list):
    
    # defaults settings
    window = Tk()
    window.title("Voyage " + ver)
    window.geometry("800x1000+100+100")

    # menu config
    menu_obj = Menu(window)

    # chapter file
    file = Menu(menu_obj, tearoff = 0)
    menu_obj.add_cascade(label = "Plik", menu = file)
    file.add_command(label = "Zapisz jako Ctrl+s", command = lambda: save_as(data))
    file.add_separator()
    file.add_command(label = "Wyjdź ESC", command = window.destroy)

    edit = Menu(menu_obj, tearoff = 0)
    menu_obj.add_cascade(label = "Zmień", menu = edit)
    edit.add_command(label = "Zaznacz wszystko Ctrl+a", command = lambda:check_all())
    edit.add_command(label = "odznacz wszystko Ctr+o", command = lambda:uncheck_all())

    # shortcuts
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
    
    # calendar
    date = datetime.datetime.now()
    datum = []
    for day in range(0,7):
        date = date + datetime.timedelta(days = 1)
        datum.append(date.strftime("%d" + "." + "%m" + "." + "%Y"))
    
    # new working plane
    frame = Frame(window)
    
    # scrollbar settings
    canvas = Canvas(frame)
    canvas.pack(fill = BOTH, expand = 1)
    scrollbar = Scrollbar(window, orient = VERTICAL, command = canvas.yview)
    scrollbar.pack(side = RIGHT, fill = Y) 
    canvas.configure(yscrollcommand = scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
    
    # new frame for widgets
    set_frame = Frame(canvas)
    canvas.create_window((0,0), window = set_frame, anchor = "nw")

    k = 0
    for line in pchor_list:
        sline = line.split(",")
        #print(sline)
        j = 0
        for i in sline:
            Label(set_frame, text = i, font = (font_name, font_size)).grid(column = j, row = k, padx = 5, pady = 5)
            j = j + 1
        
        if k == 0:
            Label(set_frame, text = "od", font = (font_name, font_size)).grid(column = j+1, row = k, padx = 5, pady = 5)
            Label(set_frame, text = "do", font = (font_name, font_size)).grid(column = j+2, row = k, padx = 5, pady = 5)
            Label(set_frame, text = "wpis", font = (font_name, font_size)).grid(column = j+3, row = k, padx = 5, pady = 5)
        else: 
            # dates combo boxes
            from_var = StringVar()
            from_combo = Combobox(set_frame, textvariable = from_var, width = 10)
            from_combo["value"] = (datum)
            from_combo["state"] = "readonly"
            from_combo.grid(column = j+1, row = k, padx = 15, pady = 5)
            from_combo.current(0)

            to_var = StringVar()
            to_combo = Combobox(set_frame, textvariable = to_var, width = 10) 
            to_combo["values"] = (datum)
            to_combo["state"] = "readonly"
            to_combo.grid(column = j+2, row = k, padx = 15, pady = 5)
            to_combo.current(0)

            # check boxes
            check = IntVar()
            check_box = Checkbutton(set_frame, textvariable = check, onvalue = 1).grid(column = j+3, row = k, padx = 15, pady = 5)
    
        k = k + 1
    sort_list(pchor_list)
    # display
    frame.pack(fill = BOTH, expand = 1)
    window.config(menu = menu_obj)
    window.mainloop()


