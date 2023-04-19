
from tkinter import *
from PIL import Image, ImageTk
import sqlite3

connection = sqlite3.connect("BdD.db")
cursor = connection.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, prenom TEXT, nom TXT, numero INT, adresse TXT, email TXT, date TXT)")

fenetre = Tk()
fenetre.title("Simulateur des notes du Bac")


fenetre.geometry("1000x800")
fenetre.configure(bg = "SteelBlue3")







fenetre.mainloop()
