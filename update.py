import platform
import os
import requests
from tkinter import messagebox
def update():

    if platform.system() == "Windows":
        res = requests.get("https://github.com/Jamro90/voyage/raw/main/voyage.exe")
        try:
            file = open("voyage.exe", "wb")
        except:
            os.remove("voyage.exe")
            file = open("voyage.exe", "wb")
        for chunk in res.iter_content(chunk_size = 1024):
            file.write(chunk)
        messagebox.showinfo("UPDATE COMPLITED!", "Aktualizacja zakończona sukcesem. Kliknij OK aby zamknąć program.")
    elif platform.system() == "Linux":
        res = requests.get("https://github.com/Jamro90/voyage/raw/main/voyage")
        try:
            file = open("voyage", "wb")
        except:
            os.remove("voyage")
            file = open("voyage", "wb")
        for chunk in res.iter_content(chunk_size = 1024):
            file.write(chunk)
        messagebox.showinfo("UPDATE COMPLITED!", "Aktualizacja zakończona sukcesem. Kliknij OK aby zamknąć program.")

    exit()

