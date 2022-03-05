import platform
import os
import requests
from tkinter import messagebox
def update():

    if platform.system() == "Windows":
        res = requests.get("https://github.com/Jamro90/voyage/raw/main/voyage_win.zip")
        try:
            file = open("voyage.exe", "wb")
        except:
            os.remove("voyage_win.zip")
            file = open("voyage_win.zip", "wb")
        for chunk in res.iter_content(chunk_size = 1024):
            file.write(chunk)
        messagebox.showinfo("UPDATE COMPLITED!", "Aktualizacja zakończona sukcesem. Kliknij OK aby zamknąć program.")
    elif platform.system() == "Linux":
        res = requests.get("https://github.com/Jamro90/voyage/raw/main/voyage.zip")
        try:
            file = open("voyage.zip", "wb")
        except:
            os.remove("voyage")
            file = open("voyage.zip", "wb")
        for chunk in res.iter_content(chunk_size = 1024):
            file.write(chunk)
        messagebox.showinfo("UPDATE COMPLITED!", "Aktualizacja zakończona sukcesem. Kliknij OK aby zamknąć program.")

    exit()

