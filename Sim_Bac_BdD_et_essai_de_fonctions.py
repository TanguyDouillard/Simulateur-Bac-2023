from tkinter import *
from PIL import Image, ImageTk
import sqlite3

connection = sqlite3.connect("BdD_simulateur.db")
cursor = connection.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS eleves(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, prenom TEXT, nom TXT, note_oral_fr INT, note_ecrit_fr INT, note_spe_1 INT, note_spe_2 INT, note_grand_oral INT, note_philosophie INT)")
connection.commit()


fenetre = Tk()
fenetre.title("Simulateur des notes du Bac")


fenetre.geometry("1000x800")
fenetre.configure(bg = "SteelBlue3")


canevas = Canvas(fenetre, width=500, height=600, bg="SteelBlue4")
canevas.pack(padx=5,pady=5)
canevas.place(x=5, y=100)

titre= Label(fenetre,text = "Simulateur Bac 2023",fg = 'black',font = "Arial 15 italic")
titre.place(x=5, y=5)

cursor.execute("SELECT * FROM eleves")

liste=cursor.fetchall()
print(liste)


""" METTRE LA DEF TROUVER NOTES DIRECT DANS LA DEF MOYENNE"""

def moyenne(Prenom):
    trouver_notes(Prenom)
    print(liste)


def trouver_notes(Prenom):
    l=[Prenom]
    cursor.execute("SELECT note_oral_fr, note_ecrit_fr, note_spe_1, note_spe_2, note_grand_oral, note_philosophie FROM eleves WHERE prenom=?",l)
    liste=cursor.fetchall()
    return liste

fenetre.mainloop()
