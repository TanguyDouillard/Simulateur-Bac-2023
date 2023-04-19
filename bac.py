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


canevas = Canvas(fenetre, width=500, height=600, bg="SteelBlue4")
canevas.pack(padx=5,pady=5)
canevas.place(x=5, y=100)

titre= Label(fenetre,text = "Simulateur Bac 2023",fg = 'black',font = "Arial 15 italic")
titre.place(x=5, y=5)




fenetre.mainloop()
