from tkinter import *
from tkinter.ttk import *
import datetime
from commands import *
from update import *
from document_maker import sort_list, doc_make

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
    
    def sorting():
        # combine & sort array data
        sorted_data = sort_list(pchor_list, from_date, to_date, check_var)
        # print document form sorted data
        doc_make(sorted_data, window)

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
    
    # making array of arrays
    pchor_list_list = []
    for _pchor in pchor_list:
        pchor = _pchor.split(",")
        pchor_list_list.append(pchor)

    # reserving memory for xomboboxes & checkbuttons
    from_date = []
    to_date = []
    check_var = []
    for i in pchor_list_list:
        from_date.append(StringVar(window))
        to_date.append(StringVar(window))
        check_var.append(IntVar(window))
    from_date.pop(0)
    to_date.pop(0)
    check_var.pop(0)
    
    # showing widgets
    # showing labels & records
    row = 0
    for i in pchor_list_list:
        for col in range(0,3):
            if row == 0:
                Label(set_frame, text = i[col], font = (font_name, font_size)).grid(column = col, row = row, padx = 20, pady = 5)

            else:
                Label(set_frame, text = i[col], font = (font_name, font_size)).grid(column = col, row = row, padx = 20, pady = 5)
        row += 1
    
    # showing comboboxes
    row = 0
    labs = ["od", "do", "wpis"]
    for i in pchor_list_list:
        for col in range(3, 6):
            if row == 0:
                Label(set_frame, text = labs[col-3], font = (font_name, font_size)).grid(column = col, row = row, padx = 20, pady = 5)

            else:
                if from_date and col == 3:
                    from_combo = Combobox(set_frame, textvariable = from_date[row-1], width = 10)
                    from_combo["value"] = (datum)
                    from_combo.current(0)
                    from_combo["state"] = "readonly"
                    from_combo.grid(column = col, row = row, padx = 20, pady = 5)
                    
                elif to_date and col == 4:
                    to_combo = Combobox(set_frame, textvariable = to_date[row-1], width = 10)
                    to_combo["value"] = (datum)
                    to_combo.current(0)
                    to_combo["state"] = "readonly"
                    to_combo.grid(column = col, row = row, padx = 20, pady = 5)
                
                else:
                    check = Checkbutton(set_frame, variable = check_var[row-1], onvalue = 1, offvalue = 0)
                    check.grid(column = col, row = row, padx = 20, pady = 5)
        row += 1

    # buttons
    # exec for btn
    btn_exec = Button(set_frame, text = "VOYAGE", command = sorting).grid(column = 4, row = 500, padx = 15, pady = 5)
    btn_exit = Button(set_frame, text = "Wyjdź (ESC)", command = window.destroy).grid(column = 3, row = 500, padx =  15, pady = 5)
    # display
    frame.pack(fill = BOTH, expand = 1)
    window.config(menu = menu_obj)
    window.mainloop()

