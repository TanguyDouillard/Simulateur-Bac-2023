from tkinter import *
from PIL import Image, ImageTk
import sqlite3

connection = sqlite3.connect("BdD.db")
cursor = connection.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, prenom TEXT, nom TXT, numero INT, adresse TXT, email TXT, date TXT)")

fenetre = Tk()
fenetre.title("Simulateur des notes du Bac")


fenetre.geometry("1920x1000")
fenetre.configure(bg = "grey8")


def mention():
##    moy=moyenne(Prenom)
    moy = 16
    titre= Label(fenetre, text = moy, fg = 'light coral', bg="grey14")
    titre.configure(font=("Source Serif Pro Semibold",20))
    titre.place(x=620, y=604)

    if moy>=16:
        titre= Label(fenetre, text = " Mention très bien ! ",fg = 'light coral', bg="grey14")
        titre.configure(font=("Source Serif Pro Semibold",20))
        titre.place(x=965, y=300)

    elif moy>=14:
        titre= Label(fenetre, text = " Mention bien ! ",fg = 'light coral', bg="grey14")
        titre.configure(font=("Source Serif Pro Semibold",20))
        titre.place(x=987, y=300)

    elif moy>=12:
        titre= Label(fenetre, text = " Mention assez bien ! ",fg = 'light coral', bg="grey14")
        titre.configure(font=("Source Serif Pro Semibold",20))
        titre.place(x=950, y=300)

    elif moy>=10:
        titre= Label(fenetre, text = " Pas de mentions ",fg = 'light coral', bg="grey14")
        titre.configure(font=("Source Serif Pro Semibold",20))
        titre.place(x=975, y=300)

    else :
        titre= Label(fenetre, text = " Tu n'as pas eu ton bac :-( ",fg = 'light coral', bg="grey14")
        titre.configure(font=("Source Serif Pro Semibold",20))
        titre.place(x=920, y=300)

canevas = Canvas(fenetre, width=450, height=500, bg="grey12",  highlightbackground = "grey10")
canevas.pack(padx=5,pady=5)
canevas.place(x=400, y=200)

titre= Label(fenetre, text = "Simulateur Bac 2023",fg = 'black')
titre.configure(font=("Source Serif Pro Semibold",25))
titre.place(x=475, y=35)

titre= Label(fenetre, text = "Elèves",fg = 'black')
titre.configure(font=("Source Serif Pro Semibold",25))
titre.place(x=90, y=55)

titre= Label(fenetre, text = "Résultat",fg = 'black')
titre.configure(font=("Source Serif Pro Semibold",25))
titre.place(x=1008, y=55)

titre= Label(fenetre, text = " Mention : ",fg = 'dark violet', bg="grey14")
titre.configure(font=("Source Serif Pro Semibold",25))
titre.place(x=1000, y=235)

bouton_1 = Button(fenetre,text = " Alexis ",bg = 'blue violet',command = fenetre.destroy)
bouton_1.configure(height=4, width=25)
bouton_1.place(x=60,y=140)

bouton_2 = Button(fenetre,text = " Tanguy ",bg = 'forest green',command = fenetre.destroy)
bouton_2.configure(height=4, width=25)
bouton_2.place(x=60,y=215)

bouton_3 = Button(fenetre,text = " Félix ",bg = 'blue violet',command = fenetre.destroy)
bouton_3.configure(height=4, width=25)
bouton_3.place(x=60,y=290)

bouton_4 = Button(fenetre,text = " Phillip ",bg = 'forest green',command = fenetre.destroy)
bouton_4.configure(height=4, width=25)
bouton_4.place(x=60,y=365)

bouton_5 = Button(fenetre,text = " Massine ",bg = 'blue violet',command = fenetre.destroy)
bouton_5.configure(height=4, width=25)
bouton_5.place(x=60,y=440)

bouton_6 = Button(fenetre,text = " Flavie ",bg = 'forest green',command = fenetre.destroy)
bouton_6.configure(height=4, width=25)
bouton_6.place(x=60,y=515)

bouton_7 = Button(fenetre,text = " Rosita ",bg = 'blue violet',command = fenetre.destroy)
bouton_7.configure(height=4, width=25)
bouton_7.place(x=60,y=590)

bouton_8 = Button(fenetre,text = " Christian ",bg = 'forest green',command = fenetre.destroy)
bouton_8.configure(height=4, width=25)
bouton_8.place(x=60,y=665)

bouton_quit = Button(fenetre,text = " Quit ",bg = 'firebrick2',command = fenetre.destroy)
bouton_quit.configure(height=4, width=25)
bouton_quit.place(x=1050,y=850)

#################################################################
#################################################################

titre= Label(fenetre, text = " Ecrit de Français : ",fg = 'darkOrchid2', bg="grey14")
titre.configure(font=("Source Serif Pro Semibold",15))
titre.place(x=435, y=240)

titre= Label(fenetre, text = " Oral de Français : ",fg = 'darkOrchid2', bg="grey14")
titre.configure(font=("Source Serif Pro Semibold",15))
titre.place(x=435, y=300)

titre= Label(fenetre, text = " SPE 1 : ",fg = 'darkOrchid2', bg="grey14")
titre.configure(font=("Source Serif Pro Semibold",15))
titre.place(x=435, y=360)

titre= Label(fenetre, text = " SPE 2 : ",fg = 'darkOrchid2', bg="grey14")
titre.configure(font=("Source Serif Pro Semibold",15))
titre.place(x=435, y=420)

titre= Label(fenetre, text = " Philosophie : ",fg = 'darkOrchid2', bg="grey14")
titre.configure(font=("Source Serif Pro Semibold",15))
titre.place(x=435, y=480)
var_Philo = StringVar()
saisie_Philo = Entry(fenetre,textvariable = var_Philo , width =5)
saisie_Philo.place(x = 569 , y = 488)

titre= Label(fenetre, text = " Grand Oral : ",fg = 'darkOrchid2', bg="grey14")
titre.configure(font=("Source Serif Pro Semibold",15))
titre.place(x=435, y=540)
var_GO = StringVar()
saisie_GO = Entry(fenetre,textvariable = var_GO , width =5)
saisie_GO.place(x = 565 , y = 546)

bouton_9 = Button(fenetre,text = " ✓ ",bg = 'green yellow',command = mention)
bouton_9.configure(height=2, width=7)
bouton_9.place(x=755,y=502)

titre= Label(fenetre, text = " Moyenne : ",fg = 'dark violet', bg="grey14")
titre.configure(font=("Source Serif Pro Semibold",25))
titre.place(x=435, y=600)

#################################################################
#################################################################
fenetre.mainloop()
