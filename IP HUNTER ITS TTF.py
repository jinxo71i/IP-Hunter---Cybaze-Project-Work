'''
Created by:       Luca Longhi
Mail:             lucalonghi18@yahoo.it
Personal Website: www.lucalonghi.it
Project Website:  www.iphunter.cloud
Last Update:      17-01-2021
Version:          2.17.1.1
'''


#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------IMPORTAZIONE MODULI E LIBRERIE-----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

from netaddr import *
from ipaddress import IPv4Address, IPv4Network
from tkinter import *
import urllib3
import json
import requests
import sqlite3
from socket import *
import dns.resolver
import time
import ssl
import socket as sk

#-----------------------------------------------------------------------------------------------------------------------
#-------------------------------------------CREAZIONE FINESTRA PRINCIPALE-----------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

root = Tk()
root.geometry("500x680")
root.title("ITS TTF IP HUNTER - Luca Longhi")
root.configure(background='black')
root.resizable(False,False)
root.grid_columnconfigure(0, weight=1)
root.iconbitmap("C:\cybaze.ico")

#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------PULIZIA ROOT WINDOW----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def clear(object):
    widget = object.grid_slaves()
    for x in widget:
        x.destroy()

#-----------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------MENU' INIZIALE------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


def menuiniziale():
    clear(root)
    root.title("ITS TTF IP HUNTER - Luca Longhi")
    ipv4frame = Frame(root)     #creazione frame di root per miglior gestione dei widget

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------IPV4 CHECKER WINDOW-----------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
    def primotasto():

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------IPV4 CHECKER FUNCTION---------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
        def IndirizzoIP():
            try:
                #testo se l'indirizzo è pubblico o privato
                indirizzoipdatestare = entry.get()
                stato = IPAddress(indirizzoipdatestare).is_private()
                # define classA,classB and classC

                classA = IPv4Network(("10.0.0.0", "255.0.0.0"))  # or IPv4Network("10.0.0.0/8")
                classB = IPv4Network(("172.16.0.0", "255.240.0.0"))  # or IPv4Network("172.16.0.0/12")
                classC = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")

                # convert string in input in a variable that will be used for define in which class is the IP
                ip1 = IPv4Address(indirizzoipdatestare)
                stato1 = ip1 in classA
                stato2 = ip1 in classB
                stato3 = ip1 in classC

                #test of class and private/public IP
                if (stato == True and stato1 == True):
                    clear(ipv4frame)
                    print("L'indirizzo IP è privato e di classe A")
                    file = open("indirizzi_testati_validi.txt", "a")
                    file.write("\nL'indirizzo IP " + indirizzoipdatestare + " e' di tipo Privato ed e' di classe A")  # a capo
                    file.close()
                    risultato = Label(ipv4frame, text="L'indirizzo IP testato è PRIVATO \nClasse A", fg="blue",
                                      bg="black")
                    risultato.config(font=('helvetica', 15))
                    risultato.grid(row=4, column=0, sticky="N", padx=20, pady=10)

                elif (stato == True and stato2 == True):
                    clear(ipv4frame)
                    print("L'indirizzo IP è privato e di classe B")
                    file = open("indirizzi_testati_validi.txt", "a")
                    file.write("\nL'indirizzo IP " + indirizzoipdatestare + " e' di tipo Privato ed e' di classe B")  # a capo
                    file.close()
                    risultato = Label(ipv4frame, text="L'indirizzo IP testato è PRIVATO \nClasse B", fg="blue",
                                      bg="black")
                    risultato.config(font=('helvetica', 15))
                    risultato.grid(row=4, column=0, sticky="N", padx=20, pady=10)

                elif (stato == True and stato3 == True):
                    clear(ipv4frame)
                    print("L'indirizzo IP è privato e di classe C")
                    file = open("indirizzi_testati_validi.txt", "a")
                    file.write("\nL'indirizzo IP " + indirizzoipdatestare + " e' di tipo Privato ed e' di classe C")  # a capo
                    file.close()
                    risultato = Label(ipv4frame, text="L'indirizzo IP testato è PRIVATO \nClasse C", fg="blue", bg="black")
                    risultato.config(font=('helvetica', 15))
                    risultato.grid(row=4, column=0, sticky="N", padx=20, pady=10)
                    buttonmenu.grid(row=10, column=0, sticky="N", padx=20, pady=250)
                else:
                    clear(ipv4frame)
                    print("L'indirizzo IP è un indirizzo IP pubblico")
                    file = open("indirizzi_testati_validi.txt", "a")
                    file.write("\nL'indirizzo IP " + indirizzoipdatestare + " e' di tipo Pubblico")  # a capo
                    file.close()

                    #using API ask for information of this Public IP from whois
                    http = urllib3.PoolManager()
                    url = "http://ipwhois.app/json/" + str(indirizzoipdatestare)
                    r = http.request('GET', url)
                    response = json.loads(r.data)
                    print(response)
                    file = open("IP_esterno_info.csv", "a")
                    file.write("\n" + str(response))  # a capo
                    file.close()

                    # using API ask for information of this Public IP from abuseipdb
                    headers = {
                        'Key': 'aa889d0c1cbfe0335d703695dc5e1f9cd511f4b43fe0d10c5ac493af5df91db9de5d35c83f5ebfc6',
                        'Accept': 'application/json', }
                    data = {
                        'ipAddress': indirizzoipdatestare
                    }
                    r = requests.request(method="GET", url='https://api.abuseipdb.com/api/v2/check', headers=headers,
                                         params=data)

                    decoderesponse = json.loads(r.text)
                    perstampare = decoderesponse["data"]

                    print(perstampare)


                    #show more and show less button for print the information from whois and abuseipdb
                    def lessinfo():
                        clear(ipv4frame)
                        publicIP = Label(ipv4frame, text="L'indirizzo IP testato è PUBBLICO\nINFORMAZIONI DA WHOIS:\n",
                                                    fg="blue", bg="black")
                        publicIP.config(font=('helvetica', 15))
                        publicIP.grid(row=4, column=0, sticky="N", padx=20, pady=0)
                        allinfowhois = Label(ipv4frame,text= "IP TESTED:                                   " + response["ip"] +
                                                             "\nCONTINENT:                              " + response["continent"] +
                                                             "\nCOUNTRY CODE:                      " + response["country_code"] +
                                                             "\nASN:                                            " + response["asn"] +
                                                             "\nISP:                                              " + response["isp"] +
                                                             "\nIS WHITE LISTED?:                      " + str(perstampare["isWhitelisted"])+
                                                             "\nTOTAL REPORT(S):                     " + str(perstampare["totalReports"]) +
                                                             "\nDISTINCT USERS' REPORTS:       " + str(perstampare["numDistinctUsers"]) +
                                                             "\n\n\n",justify=LEFT, bg="black", fg="white")
                        allinfowhois.grid(row=6, column=0, sticky="N", padx=10, pady=10)
                        button2 = Button(ipv4frame, text='SHOW MORE', command=moreinfo, bg="cyan")
                        button2.grid(row=7, column=0, sticky="N", padx=20, pady=15)

                        buttonmenu = Button(root, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
                        buttonmenu.grid(row=10, column=0, sticky="N", padx=10, pady=0)

                    def moreinfo():
                        clear(ipv4frame)
                        publicIP = Label(ipv4frame, text="L'indirizzo IP testato è PUBBLICO\nINFORMAZIONI DA WHOIS:\n",
                                                    fg="blue", bg="black")
                        publicIP.config(font=('helvetica', 15))
                        publicIP.grid(row=4, column=0, sticky="N", padx=20, pady=0)
                        allinfowhois = Label(ipv4frame,text= "IP TESTED:                                   " + response["ip"] +
                                                             "\nCONTINENT:                              " + response["continent"] +
                                                             "\nCOUNTRY CODE:                      " + response["country_code"] +
                                                             "\nASN:                                            " + response["asn"] +
                                                             "\nISP:                                              " + response["isp"] +
                                                             "\nIS WHITE LISTED?:                      " + str(perstampare["isWhitelisted"])+
                                                             "\nTOTAL REPORT(S):                     " + str(perstampare["totalReports"]) +
                                                             "\nDISTINCT USERS' REPORTS:       " + str(perstampare["numDistinctUsers"]) +
                                                             "\nLAST REPORT DATE:                   " + str(perstampare["lastReportedAt"]) +
                                                             "\nLATITUDE:                                    " + response["latitude"] +
                                                             "\nLONGITUDE:                                 " + response["longitude"]
                                                             ,justify=LEFT, bg="black",fg="white")
                        allinfowhois.grid(row=6, column=0, sticky="N", padx=10, pady=10)

                        button2 = Button(ipv4frame, text='  SHOW LESS  ', command=lessinfo, bg="cyan")
                        button2.grid(row=7, column=0, sticky="N", padx=20, pady=15)

                        buttonmenu = Button(root, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
                        buttonmenu.grid(row=10, column=0, sticky="N", padx=10, pady=0)

                    lessinfo()


            except:
                clear(ipv4frame)
                publicIP = Label(ipv4frame, text="INDIRIZZO IP NON VALIDO",
                                 fg="red", bg="black")
                publicIP.config(font=('helvetica', 15))
                publicIP.grid(row=4, column=0, sticky="N", padx=20, pady=10)
                print("Indirizzo IP inserito NON VALIDO")

                buttonmenu.grid(row=10, column=0, sticky="N", padx=10, pady=270)

        clear(root)
        root.title("ITS TTF IP HUNTER - IP CHECKER - Luca Longhi")

        titolo = Label(root, text='IP HUNTER CHECKER', bg="black", fg="violet")
        titolo.config(font=('helvetica', 30))
        titolo.grid(row=0, column=0, sticky="WE", padx=20, pady=40)

        sottotitolo = Label(root, text='Insert IP address to check:', bg="black", fg="white")
        sottotitolo.config(font=('helvetica', 15))
        sottotitolo.grid(row=1, column=0, sticky="WE", padx=20, pady=10)

        entry = Entry()
        entry.grid(row=2, column=0, sticky="WE", padx=140, pady=10)

        button1 = Button(text='Check IP address', command=IndirizzoIP, bg="cyan")
        button1.grid(row=3, column=0, sticky="N", padx=10, pady=20)
        ipv4frame = Frame(root)
        ipv4frame.grid(row=5, column=0, sticky="N", padx=10, pady=10)
        ipv4frame.configure(bg="black")

        buttonmenu = Button(root, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
        buttonmenu.grid(row=10, column=0, sticky="N", padx=10, pady=320)

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------DNS RESOLVER WINDOW-----------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    def secondotasto():
        def IndirizzoIP():
            dnsframe = Frame(root)
            dnsframe.configure(background='black')
            dnsframe.grid(row=6, column=0)
            try:
                clear(dnsframe)
                domain = entry.get()
                print ("\n\nThe IP Address of the Domain Name is: ")


                result = dns.resolver.resolve(str(domain), 'A')
                for ipval in result:
                    print('IP', ipval.to_text())
                risultati = Label(dnsframe, text="The DNS server of " + str(domain) + " is: \n" + str(ipval.to_text()), bg="black", fg="white")
                risultati.config(font=('helvetica', 15))
                risultati.grid(row=6, column=0)
                buttonmenu = Button(root, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
                buttonmenu.grid(row=10, column=0, sticky="N", padx=10, pady=260)
            except:
                clear(dnsframe)
                risultati = Label(dnsframe, text="\n               DNS NON VALIDO                  \n", bg="black", fg="red")
                risultati.config(font=('helvetica', 15))
                risultati.grid(row=6, column=0)


        clear(root)
        root.title("ITS TTF IP HUNTER - DNS RESOLVER- Luca Longhi")

        titolo = Label(root, text='DNS RESOLVER', bg="black", fg="violet")
        titolo.config(font=('helvetica', 30))
        titolo.grid(row=0, column=0, sticky="WE", padx=20, pady=40)

        sottotitolo = Label(root, text='Insert DNS to resolve:', bg="black", fg="white")
        sottotitolo.config(font=('helvetica', 15))
        sottotitolo.grid(row=1, column=0, sticky="WE", padx=20, pady=10)

        entry = Entry()
        entry.grid(row=2, column=0, sticky="WE", padx=140, pady=20)

        button1 = Button(text='Check DNS Server', command=IndirizzoIP, bg="cyan")
        button1.grid(row=5, column=0, sticky="N", padx=10, pady=10)

        ipv4frame = Frame(root)
        ipv4frame.grid(row=8, column=0, sticky="N", padx=10, pady=10)
        ipv4frame.configure(bg="black")
        buttonmenu = Button(root, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
        buttonmenu.grid(row=11, column=0, sticky="N",padx=10, pady=300)

# -----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------DATABASE WINDOW------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    def terzotasto():
        global log
        if(log==True):
            def inviowhitelist():
                try:
                    # creo e/o connetto al database
                    conn = sqlite3.connect("dati.db")

                    # creo la tabella, se non esiste, con determinati valori da inserire e primary key(ip) per il controllo
                    sql = "create table if not exists IndirizziIP (" \
                          "IP varchar(20) primary key," \
                          "CLIENT varchar(20) not null," \
                          "DOMAIN varchar(20) not null," \
                          "DEVICE varchar(20) not null," \
                          "SERVICES varchar(1000)," \
                          "NOTES varchar(1000)," \
                          "WHITELIST varchar(9));"
                    # esecuzione sql
                    conn.execute(sql)

                    # creo il cursore(puntatore)
                    c = conn.cursor()

                    # inserimento valori vari
                    ip = ipentry.get()
                    ip2 = IPAddress(ip).is_private()
                    cliente = clienteentry.get()
                    dominio = dominioentry.get()
                    dispositivo = dispositivoentry.get()
                    servizi = servizientry.get()
                    note = noteentry.get()
                    whitelist = "WHITELIST"
                    item = [str(ip), str(cliente), str(dominio), str(dispositivo), str(servizi), str(note), str(whitelist)]


                    # esecuzione inserimento valori dell'item in IndirizziIP
                    c.execute("insert into IndirizziIP values(?,?,?,?,?,?,?);",
                              item)  # punto di domanda ogni componente del database, ogni riga

                    # commit delle modifiche
                    conn.commit()

                    # chiudo database
                    conn.close()

                    print("Valore correttamente inserito nel database")
                    presente = Label(root, text="      VALORE CORRETTAMENTE INSERITO NEL DATABASE      ", bg="black", fg="green")
                    presente.config(font=('helvetica', 13))
                    presente.grid(row=10, column=0)

                    # gestione errore del valore già inserito
                except sqlite3.IntegrityError:
                    print("Valore già nel database")
                    presente = Label(root, text="      VALORE GIA' PRESENTE NEL DATABASE      ", bg="black", fg="orange")
                    presente.config(font=('helvetica', 15))
                    presente.grid(row=10,column=0)
                except AddrFormatError:
                    print("Valore non valido")
                    presente = Label(root, text="           VALORE DELL'IP NON VALIDO           ", bg="black", fg="red")
                    presente.config(font=('helvetica', 15))
                    presente.grid(row=10,column=0)

            def invioblacklist():
                try:
                    # creo e/o connetto al database
                    conn = sqlite3.connect("dati.db")

                    # creo la tabella, se non esiste, con determinati valori da inserire e primary key(ip) per il controllo
                    sql = "create table if not exists IndirizziIP (" \
                          "IP varchar(20) primary key," \
                          "CLIENT varchar(20) not null," \
                          "DOMAIN varchar(20) not null," \
                          "DEVICE varchar(20) not null," \
                          "SERVICES varchar(1000)," \
                          "NOTES varchar(1000)," \
                          "WHITELIST varchar(9));"
                    # esecuzione sql
                    conn.execute(sql)

                    # creo il cursore(puntatore)
                    c = conn.cursor()

                    # inserimento valori vari
                    ip = ipentry.get()
                    ip2 = IPAddress(ip).is_private()
                    cliente = clienteentry.get()
                    dominio = dominioentry.get()
                    dispositivo = dispositivoentry.get()
                    servizi = servizientry.get()
                    note = noteentry.get()
                    whitelist = "BLACKLIST"
                    item = [str(ip), str(cliente), str(dominio), str(dispositivo), str(servizi), str(note), str(whitelist)]


                    # esecuzione inserimento valori dell'item in IndirizziIP
                    c.execute("insert into IndirizziIP values(?,?,?,?,?,?,?);",
                              item)  # punto di domanda ogni componente del database, ogni riga

                    # commit delle modifiche
                    conn.commit()

                    # chiudo database
                    conn.close()

                    print("Valore correttamente inserito nel database")
                    presente = Label(root, text="      VALORE CORRETTAMENTE INSERITO NEL DATABASE      ", bg="black", fg="green")
                    presente.config(font=('helvetica', 13))
                    presente.grid(row=10, column=0)

                    # gestione errore del valore già inserito
                except sqlite3.IntegrityError:
                    print("Valore già nel database")
                    presente = Label(root, text="      VALORE GIA' PRESENTE NEL DATABASE      ", bg="black", fg="orange")
                    presente.config(font=('helvetica', 15))
                    presente.grid(row=10,column=0)
                except AddrFormatError:
                    print("Valore non valido")
                    presente = Label(root, text="           VALORE DELL'IP NON VALIDO           ", bg="black", fg="red")
                    presente.config(font=('helvetica', 15))
                    presente.grid(row=10,column=0)
            clear(root)
            root.title("ITS TTF IP HUNTER - IP DATABASE - Luca Longhi")

            titolo = Label(root, text='ADD IP TO DATABASE', bg="black", fg="violet")
            titolo.config(font=('helvetica', 30))
            titolo.grid(row=1, column=0, sticky="WE", padx=20, pady=40)

            ipentry = Entry()
            ipentry.grid(row=2, column=0, sticky="WE", padx=140, pady=10)
            ipentry.insert(END, 'IP Address')

            clienteentry = Entry()
            clienteentry.grid(row=3, column=0, sticky="WE", padx=140, pady=10)
            clienteentry.insert(END, 'Client')

            dominioentry = Entry()
            dominioentry.grid(row=4, column=0, sticky="WE", padx=140, pady=10)
            dominioentry.insert(END, 'Domain')

            dispositivoentry = Entry()
            dispositivoentry.grid(row=5, column=0, sticky="WE", padx=140, pady=10)
            dispositivoentry.insert(END, 'Device')

            servizientry = Entry()
            servizientry.grid(row=6, column=0, sticky="WE", padx=140, pady=10)
            servizientry.insert(END, 'Service')

            noteentry = Entry()
            noteentry.grid(row=7, column=0, sticky="WE", padx=140, pady=10)
            noteentry.insert(END, 'Notes')

            databaseframe= Frame(root)
            databaseframe.configure(bg="black")
            databaseframe.grid(row=8, column=0, columnspan=1)


            button1 = Button(databaseframe,text='Add IP as WHITELIST', command=inviowhitelist, bg="white", fg="blue")
            button1.grid(row=0, column=0, sticky="N", padx=10, pady=10)

            button2 = Button(databaseframe,text='Add IP as BLACKLIST', command=invioblacklist, bg="grey", fg="black")
            button2.grid(row=0, column=1, sticky="N", padx=10, pady=10)

            buttonmenu = Button(root, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
            buttonmenu.grid(row=11, column=0, sticky="N", padx=10, pady=220)
        else:
            lipage = Toplevel(root)
            lipage.geometry("400x220")
            lipage.title("LOGIN/REGISTER PAGE - Luca Longhi")
            lipage.configure(background='black')
            lipage.resizable(False, False)
            lipage.grid_columnconfigure(0, weight=1)
            lipage.iconbitmap("C:\cybaze.ico")

            def tablecreation():
                # db connection
                conn = sqlite3.connect("loginlist.db")
                c = conn.cursor()
                c.execute("""CREATE TABLE IF NOT EXISTS loginlist (
                            username text,
                            password text
                            )""")
                conn.commit()
                conn.close()

            def registerpage():

                def registration():
                    name = regus.get()
                    password = regpwd.get()
                    tablecreation()
                    stat = [name, password]
                    conn = sqlite3.connect("loginlist.db")
                    c = conn.cursor()
                    sqlite_select_query = """SELECT * from loginlist where username = ?"""
                    c.execute(sqlite_select_query, (name,))
                    data = c.fetchone()
                    if data is None:
                        c.execute("INSERT INTO loginlist VALUES (?,?);", stat)
                        conn.commit()
                        conn.close()
                        print("Register success")
                        titolo = Label(regframe, text='REGISTRATION SUCCESS!', bg="black", fg="cyan",
                                       font=("helvetica", 13))
                        titolo.grid(row=6, column=0, sticky="WE", padx=10, pady=10)
                    else:
                        conn.commit()
                        conn.close()
                        print("User already in database")
                        titolo = Label(regframe, text='USER ALREADY REGISTERED', bg="black", fg="orange",
                                       font=("helvetica", 13))
                        titolo.grid(row=6, column=0, sticky="WE", padx=10, pady=10)

                regframe = Toplevel(lipage)
                regframe.geometry("300x280")
                regframe.title("New User Registration")
                regframe.configure(background='black')
                regframe.resizable(False, False)
                regframe.grid_columnconfigure(0, weight=1)
                regframe.iconbitmap("C:\cybaze.ico")

                titolo = Label(regframe, text='NEW USER\nREGISTRATION', bg="black", fg="violet", font=("helvetica", 15))
                titolo.grid(row=0, column=0, sticky="WE", padx=30, pady=10)

                titolo = Label(regframe, text='Username:', bg="black", fg="yellow", font=("helvetica", 10))
                titolo.grid(row=1, column=0, sticky="WE")
                regus = Entry(regframe)
                regus.grid(row=2, column=0, padx=90, pady=5, sticky="WE")
                titolo = Label(regframe, text='Password:', bg="black", fg="yellow", font=("helvetica", 10))
                titolo.grid(row=3, column=0, sticky="WE")
                regpwd = Entry(regframe, show="*")
                regpwd.grid(row=4, column=0, padx=90, pady=5, sticky="WE")

                button = Button(regframe, text="REGISTER", command=registration, bg="cyan")
                button.grid(row=5, column=0, padx=20, pady=0)
                regframe.grab_set()

            def loginpage():

                def test_reg(name, password):
                    tablecreation()
                    conn = sqlite3.connect("loginlist.db")
                    c = conn.cursor()
                    sqlite_select_query = """SELECT * from loginlist where username = ?"""
                    c.execute(sqlite_select_query, (name,))
                    data = c.fetchone()
                    if data is None:
                        conn.commit()
                        conn.close()
                        return "user isn't Register success"
                    else:
                        conn.commit()
                        conn.close()

                        return "User already register"

                def login():
                    global log
                    name = logus.get()
                    password = logpwd.get()
                    result = test_reg(name, password)

                    conn = sqlite3.connect("loginlist.db")
                    c = conn.cursor()
                    if result == "User already register":
                        sqlite_select_query = """SELECT * from loginlist where username = ?"""
                        c.execute(sqlite_select_query, (name,))
                        query_result = c.fetchone()
                        if query_result[0] == name and query_result[1] == password:
                            print("Login Success")
                            titolo = Label(resultframe, text='     LOGIN SUCCESS!     ', bg="black", fg="green",
                                           font=("helvetica", 17))
                            titolo.grid(row=6, column=0, sticky="WE", padx=30, pady=10)
                            log = not log
                            lipage.destroy()
                            terzotasto()


                        else:
                            print("Username or password is incorrect")
                            titolo = Label(resultframe, text='Username or password\nis incorrect', bg="black", fg="red",
                                           font=("helvetica", 13))
                            titolo.grid(row=6, column=0, sticky="WE", padx=10, pady=10)
                    else:
                        print("Username or password is incorrect")
                        titolo = Label(resultframe, text='Username or password\nis incorrect', bg="black", fg="red",
                                       font=("helvetica", 13))
                        titolo.grid(row=6, column=0, sticky="WE", padx=10, pady=10)

                logframe = Toplevel(lipage)
                logframe.geometry("300x250")
                logframe.title("User Login")
                logframe.configure(background='black')
                logframe.resizable(False, False)
                logframe.grid_columnconfigure(0, weight=1)
                logframe.iconbitmap("C:\cybaze.ico")

                resultframe = Frame(logframe)
                resultframe.configure(background='black')
                resultframe.grid(row=6, column=0)

                titolo = Label(logframe, text='USER LOGIN', bg="black", fg="violet", font=("helvetica", 15))
                titolo.grid(row=0, column=0, sticky="WE", padx=30, pady=10)

                titolo = Label(logframe, text='Username:', bg="black", fg="yellow", font=("helvetica", 10))
                titolo.grid(row=1, column=0, sticky="WE")
                logus = Entry(logframe)
                logus.grid(row=2, column=0, padx=90, pady=5, sticky="WE")
                titolo = Label(logframe, text='Password:', bg="black", fg="yellow", font=("helvetica", 10))
                titolo.grid(row=3, column=0, sticky="WE")
                logpwd = Entry(logframe, show="*")
                logpwd.grid(row=4, column=0, padx=90, pady=5, sticky="WE")

                button = Button(logframe, text="LOGIN", command=login, bg="cyan")
                button.grid(row=5, column=0, padx=20, pady=0)
                logframe.grab_set()

            titolo = Label(lipage, text="LOGIN OR REGISTER IF YOU\nWANT TO USE DATABASE", bg="black", fg="violet",
                           font=("helvetica", 15))
            titolo.grid(row=0, column=0, padx=20, pady=10)
            button = Button(lipage, text="LOGIN", command=loginpage, font=("helvetica", 15))
            button.grid(row=1, column=0, sticky="WE", padx=10, pady=15)
            button = Button(lipage, text="NEW USER?", command=registerpage, font=("helvetica", 15))
            button.grid(row=2, column=0, sticky="WE", padx=10, pady=15)
            lipage.grab_set()
            lipage.mainloop()

# -----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------SSL SCAN WINDOWS-----------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    def quartotasto():
        def sslscan():
            hostname = str(entry5.get())

            context = ssl.create_default_context()
            try:

                with sk.create_connection((hostname, 443)) as sock:
                    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                        print(ssock.version())
                        clear(framescritta)
                        result = Label(framescritta, text="Site " + hostname + " use a \n" + ssock.version() + " certificate", font=("helvetica", 18), bg="black", fg="green")
                        result.grid(row=7, column=0, padx=20, pady=30)
                        buttonmenu = Button(framescritta, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
                        buttonmenu.grid(row=10, column=0, sticky="N", padx=20, pady=260)

            except :
                print("Site not valid or SSL not on site")
                clear(framescritta)
                result = Label(framescritta, text="Site not valid or SSL not on site", font=("helvetica", 18), bg="black", fg="orange")
                result.grid(row=7, column=0, padx=20, pady=30)
                buttonmenu = Button(framescritta, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
                buttonmenu.grid(row=10, column=0, sticky="N", padx=20, pady=290)

        clear(root)
        root.title("ITS TTF IP HUNTER - SSL Scanner - Luca Longhi")
        titolo = Label(root, text='SSL SCANNER', bg="black", fg="violet")
        titolo.config(font=('helvetica', 30))
        titolo.grid(row=0, column=0, sticky="WE", padx=20, pady=40)

        sottotitolo = Label(root, text="Enter the site you want to scan for certificate: ", bg="black", fg="white")
        sottotitolo.config(font=('helvetica', 15))
        sottotitolo.grid(row=1, column=0, sticky="WE", padx=20, pady=0)

        entry5 = Entry()
        entry5.grid(row=2, column=0, sticky="WE", padx=140, pady=10)
        button1 = Button(text='Scan SSL Certificate', command=sslscan, bg="cyan")
        button1.grid(row=6, column=0, sticky="N", padx=10, pady=10)
        framescritta = Frame(root, bg="black")
        framescritta.grid(row=7, column=0)
        buttonmenu = Button(root, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
        buttonmenu.grid(row=10, column=0, sticky="N",padx= 20 ,pady=380)

# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------MAIL SCAN WINDOW-------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    def quintotasto():
        clear(root)
        root.title("ITS TTF IP HUNTER - Mail Scan - Luca Longhi")
        titolo = Label(root, text='MAIL SCANNER', bg="black", fg="violet")
        titolo.config(font=('helvetica', 30))
        titolo.grid(row=0, column=0, sticky="WE", padx=20, pady=40)

        titolo = Label(root, text='NOT YET TESTED SECTION\n\n'
                                  'COMING SOON :)', bg="black", fg="ORANGE")
        titolo.config(font=('helvetica', 15))
        titolo.grid(row=1, column=0, sticky="WE", padx=20, pady=40)

        buttonmenu = Button(root, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
        buttonmenu.grid(row=10, column=0, sticky="N", padx=10, pady= 340)

# -----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------NETWORK SCAN WINDOW---------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    def sestotasto():
        clear(root)
        #root.geometry("500x750")
        root.title("ITS TTF IP HUNTER - Network Scanner - Luca Longhi")


        def networkscan():
            try:
                startTime = time.time()
                target = entry.get()
                number1 = entry2.get()
                number = int(number1) + 1
                t_IP = gethostbyname(target)
                print('Starting scan on host: ', t_IP)
                franco.tag_config("end", background="#7fbfbf", foreground="white", justify='center')
                franco.tag_config("divisorio", background="#000000", foreground="#003333", justify='center')
                franco.insert(END, "   \n", "divisorio")
                franco.insert(END, f"Scan of \'{t_IP}\' host on: {number1} port(s)\n", "end")
                for i in range(1, int(number)):

                    s = socket(AF_INET, SOCK_STREAM)
                    s.settimeout(0.08)
                    conn = s.connect_ex((t_IP, i))
                    franco.tag_config("open", background="green", foreground="white", justify='center')
                    if (conn == 0):
                        print('Port %d: OPEN' % (i,))
                        franco.insert(END, 'Port %d: OPEN' % (i,) + "\n" ,"open")

                    '''else:
                        print('Port %d: CLOSED' % (i,))
                        franco.insert(END, 'Port %d: CLOSED' % (i,) + "\n")'''
                    s.close()
                    root.update()

                finishTime = time.time()
                minuti = finishTime - startTime
                print('Time taken: ', float(minuti))


                franco.insert(END, "Time taken by script: %.2f second(s)\n" % (minuti), "end")
                franco.tag_config("divisorio", background="#000000", foreground="#003333", justify='center')
                franco.insert(END, "   \n", "divisorio")
            except ValueError:
                franco.tag_config("error", background="red", foreground="white", justify='center')
                franco.insert(END, "NUMBER OF PORT(S) NOT VALID\n" , "error")
            except gaierror:
                franco.tag_config("error", background="red", foreground="white", justify='center')
                franco.insert(END, "HOST NOT VALID\n", "error")

        titolo = Label(root, text='NETWORK SCANNER', bg="black", fg="violet")
        titolo.config(font=('helvetica', 30))
        titolo.grid(row=0, column=0, sticky="WE", padx=20, pady=12)

        sottotitolo = Label(root, text="Enter the host to be scanned: ", bg="black", fg="white")
        sottotitolo.config(font=('helvetica', 15))
        sottotitolo.grid(row=1, column=0, sticky="WE", padx=20, pady=0)

        entry = Entry()
        entry.grid(row=2, column=0, sticky="WE", padx=140, pady=10)

        sottotitolo = Label(root, text="How many ports you want to scan? ", bg="black", fg="white")
        sottotitolo.config(font=('helvetica', 15))
        sottotitolo.grid(row=3, column=0, sticky="WE", padx=20, pady=0)

        entry2 = Entry()
        entry2.grid(row=4, column=0, sticky="WE", padx=220, pady=5)

        frame = Frame(root)
        frame.grid(row=5, column=0)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        franco = Text(frame, wrap=NONE, yscrollcommand=scrollbar.set)
        franco.pack()
        franco.pack(side="left")

        scrollbar.config(command=franco.yview)




        button1 = Button(text='Scan Network Port', command=networkscan, bg="cyan")
        button1.grid(row=6, column=0, sticky="N", padx=10, pady=10)



        buttonmenu = Button(root, text="GO BACK TO MAIN", command=menuiniziale, bg="yellow", fg="black")
        buttonmenu.grid(row=10, column=0, sticky="N")

# -----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------CREDITS WINDOW-----------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

    def settimotasto():
        credit = Toplevel(root)
        credit.geometry("320x350")
        credit.title("Credits IP Hunter")
        credit.configure(background='black')
        credit.resizable(False, False)
        credit.iconbitmap("C:\cybaze.ico")

        titolo = Label(credit, text='\n\n'
                                    'CREATED BY:\n\n'
                                    'MAIL:\n\n'
                                    'SITO:\n\n'
                                    'LAST UPDATE:\n\n'
                                    'VERSION:\n\n'
                                    'Collaborator:\n\n\n\n', bg="black", fg="violet", justify=LEFT)
        titolo.config(font=('helvetica', 10))
        titolo.grid(row=0, column=1,sticky="WE", padx=20, pady=10)

        sotto = Label(credit, text='\n\n'
                                   'Luca Longhi\n\n'
                                    'lucalonghi18@yahoo.it\n\n'
                                    'www.lucalonghi.it\n\n'
                                    '23-09-2020\n\n'
                                    '0.09.23.4\n\n'
                                    'Giulio Monaco\nPietro Melillo\nAndrea Vercesi\nPatrizia Garavaglia\n', bg="black", fg="yellow",justify=LEFT)
        sotto.config(font=('helvetica', 10))
        sotto.grid(row=0, column=2, sticky="WE", padx=20, pady=10)


        exitbutton= Button(credit, text="EXIT", bg= "red",fg="white" ,command=credit.destroy)
        exitbutton.grid(row=1, column=0, sticky="WE", padx=80, pady=0, columnspan=3)
        credit.grab_set()

# -----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------CREATE GRAPHICS AND BUTTON OF THE MENU PAGE-------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


    titolo = Label(root, text='SELECT THE OPERATION', bg="black", fg="violet")
    titolo.config(font=('helvetica', 25))
    titolo.grid(row=0, column=0, sticky="N", padx=20, pady=50)

    tasto1 = Button(root, text="Check an IP Address", command=primotasto, font=("helvetica", 14), bg="yellow")
    tasto1.grid(row=1, column=0, sticky="WE", padx=80, pady=10)
    tasto2 = Button(root, text="DNS Resolver", command=secondotasto, font=("helvetica", 14), bg="yellow")
    tasto2.grid(row=2, column=0, sticky="WE", padx=80, pady=10)
    tasto3 = Button(root, text="Add a private IP to your database", command=terzotasto, font=("helvetica", 14),bg="yellow")
    tasto3.grid(row=3, column=0, sticky="WE", padx=80, pady=10)
    tasto4 = Button(root, text="SSL Scanner", command=quartotasto, font=("helvetica", 14),bg="yellow")
    tasto4.grid(row=4, column=0, sticky="WE", padx=80, pady=10)
    tasto5 = Button(root, text="Mail Scanner", command=quintotasto, font=("helvetica", 14), bg="yellow")
    tasto5.grid(row=5, column=0, sticky="WE", padx=80, pady=10)
    tasto6 = Button(root, text="Network Scanner", command=sestotasto, font=("helvetica", 14), bg="yellow")
    tasto6.grid(row=6, column=0, sticky="WE", padx=80, pady=10)
    tasto7 = Button(root, text="CREDITS", command=settimotasto, font=("helvetica", 10), bg="violet", fg="black")
    tasto7.grid(row=7, column=0, sticky="WE", padx=160, pady=120)

global log

log = False

menuiniziale()


root.mainloop()
