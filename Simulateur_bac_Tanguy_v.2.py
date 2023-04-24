from tkinter import *
from PIL import Image, ImageTk
import sqlite3


#--------------------------------------------------------------

def moyenne(Prenom):
    liste_3=trouver_notes(Prenom)
    moy=0
    liste_des_notes=[]
    for elt in liste_3[0]:
        if elt == None:
            pass
        else:
            liste_des_notes.append(elt)
            moy=moy+elt
    moyenne=moy/len(liste_des_notes)
    return moyenne

def trouver_notes(Prenom):
    l=[Prenom]
    cursor.execute("SELECT note_oral_fr, note_ecrit_fr, note_spe_1, note_spe_2, note_grand_oral, note_philosophie FROM eleves WHERE prenom=?",l)
    liste_2=cursor.fetchall()
    print(liste_2)
    for i in range(len(liste_2)):
        for elt in liste_2:
            labels.append(Label(canevas,text=elt,bg='Skyblue3', font="Sans 7"))
            labels[i].place(x=10,y=10+(30*i))

    return liste_2

def mention(Prenom):
    moy=moyenne(Prenom)
    if moy>=16:
        return "Mention très bien"
    elif moy>=14:
        return "Mention bien"
    elif moy>=12:
        return "Mention assez bien"
    elif moy>=10:
        return "Tu n'as pas de mention, mais tu as ton Bac !"
    return "Malheureusement tu n'as pas ton Bac, mais peut-etre avec les rattrapages !"



#-----------------------------------------------------------------------------------------------------------------------------------------

connection = sqlite3.connect("BdD_simulateur.db")
cursor = connection.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS eleves(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, prenom TEXT, nom TXT, note_oral_fr INT, note_ecrit_fr INT, note_spe_1 INT, note_spe_2 INT, note_grand_oral INT, note_philosophie INT)")
connection.commit()

fenetre = Tk()
fenetre.title("Simulateur des notes du Bac")

#--------------------------------------------------------------

def moyenne(Prenom):
    liste_3=trouver_notes(Prenom)
    moy=0
    liste_des_notes=[]
    for elt in liste_3[0]:
        if elt == None:
            pass
        else:
            liste_des_notes.append(elt)
            moy=moy+elt
    moyenne=moy/len(liste_des_notes)
    return moyenne

def trouver_notes(Prenom):
    l=[Prenom]
    cursor.execute("SELECT note_oral_fr, note_ecrit_fr, note_spe_1, note_spe_2, note_grand_oral, note_philosophie FROM eleves WHERE prenom=?",l)
    liste_2=cursor.fetchall()
    labels=[]
    print(liste_2)
    for i in range(len(liste_2)):
        for elt in liste_2:
            labels.append(Label(canevas,text=elt,bg='Skyblue3', font="Sans 7"))
            labels[i].place(x=10,y=10+(30*i))
    return liste_2

def mention(Prenom):
    moy=moyenne(Prenom)
    if moy>=16:
        return "Mention très bien"
    elif moy>=14:
        return "Mention bien"
    elif moy>=12:
        return "Mention assez bien"
    elif moy>=10:
        return "Tu n'as pas de mention, mais tu as ton Bac !"
    return "Malheureusement tu n'as pas ton Bac, mais peut-etre avec les rattrapages !"



#-----------------------------------------------------------------------------------------------------------------------------------------


fenetre.geometry("1920x1000")
fenetre.configure(bg = "grey8")


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
titre.place(x=1000, y=55)

titre= Label(fenetre, text = "Mention : ",fg = 'dark violet', bg="grey8")
titre.configure(font=("Source Serif Pro Semibold",25))
titre.place(x=1000, y=235)

titre= Label(fenetre, text = "Moyenne : ",fg = 'dark violet', bg="grey8")
titre.configure(font=("Source Serif Pro Semibold",25))
titre.place(x=995, y=435)

bouton_1 = Button(fenetre,text = " Alexis ",bg = 'blue violet',command = trouver_notes("Alexis"))
bouton_1.configure(height=4, width=25)
bouton_1.place(x=60,y=140)

bouton_2 = Button(fenetre,text = " Tanguy ",bg = 'forest green',command = trouver_notes("Tanguy"))
bouton_2.configure(height=4, width=25)
bouton_2.place(x=60,y=215)

bouton_3 = Button(fenetre,text = " Félix ",bg = 'blue violet',command = trouver_notes("Felix"))
bouton_3.configure(height=4, width=25)
bouton_3.place(x=60,y=290)

bouton_4 = Button(fenetre,text = " Phillip ",bg = 'forest green',command = trouver_notes("Phillip"))
bouton_4.configure(height=4, width=25)
bouton_4.place(x=60,y=365)

bouton_5 = Button(fenetre,text = " Massine ",bg = 'blue violet',command = trouver_notes("Massine"))
bouton_5.configure(height=4, width=25)
bouton_5.place(x=60,y=440)

bouton_6 = Button(fenetre,text = " Flavie ",bg = 'forest green',command = trouver_notes("Flavie"))
bouton_6.configure(height=4, width=25)
bouton_6.place(x=60,y=515)

bouton_7 = Button(fenetre,text = " Rosita ",bg = 'blue violet',command = trouver_notes("Rosita"))
bouton_7.configure(height=4, width=25)
bouton_7.place(x=60,y=590)

bouton_8 = Button(fenetre,text = " Christian ",bg = 'forest green',command = trouver_notes("Christian"))
bouton_8.configure(height=4, width=25)
bouton_8.place(x=60,y=665)

bouton_quit = Button(fenetre,text = " Quit ",bg = 'firebrick2',command = fenetre.destroy)
bouton_quit.configure(height=4, width=25)
bouton_quit.place(x=1050,y=850)

fenetre.mainloop()
