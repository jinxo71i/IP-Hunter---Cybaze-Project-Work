import sqlite3
from tkinter import *



root = Tk()
root.geometry("450x400")
root.title("ITS TTF IP HUNTER - IP to Database - Luca Longhi")
root.configure(background='black')
root.resizable(False,False)
root.grid_columnconfigure(0, weight=1)
root.iconbitmap("C:\cybaze.ico")

try:
    # creo e/o connetto al database
    conn = sqlite3.connect("dati.db")

    #creo il database con determinati valori da inserire e primary key(ip) per il controllo
    sql = "create table if not exists IndirizziIP (" \
                                "IP varchar(15) primary key,"\
                                "CLIENT varchar(20) not null,"\
                                "DOMAIN varchar(20) not null,"\
                                "DEVICE varchar(20) not null,"\
                                "SERVICES varchar(1000),"\
                                "NOTES varchar(1000));"
    #esecuzione sql
    conn.execute(sql)

    #creo il cursore(puntatore)
    c = conn.cursor()

    #inserimento valori vari
    ip= "192.198.145.76"
    cliente = "google"
    dominio= "google"
    dispositivo="laptop"
    servizi = ""
    note = ""
    item = [str(ip),str(cliente),str(dominio), str(dispositivo), str(servizi), str(note)]

    #esecuzione inserimento valori dell'item in IndirizziIP
    c.execute("insert into IndirizziIP values(?,?,?,?,?,?);", item) #punto di domanda ogni componente del database, ogni riga

    #commit delle modifiche
    conn.commit()

    # chiudo database
    conn.close()

    print("Valore correttamente inserito nel database")

    #gestione errore del valore già inserito
except sqlite3.IntegrityError:
    print("Valore già nel database")

root.mainloop()