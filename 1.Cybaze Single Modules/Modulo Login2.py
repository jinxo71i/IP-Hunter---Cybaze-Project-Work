from tkinter import *
import sqlite3

root = Tk()
root.geometry("400x220")
root.title("LOGIN/REGISTER PAGE - Luca Longhi")
root.configure(background='black')
root.resizable(False,False)
root.grid_columnconfigure(0, weight=1)
root.iconbitmap("C:\cybaze.ico")


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
            print( "Register success")
            titolo = Label(regframe, text='REGISTRATION SUCCESS!', bg="black", fg="cyan",font=("helvetica", 13))
            titolo.grid(row=6, column=0, sticky="WE", padx=10, pady=10)
        else:
            conn.commit()
            conn.close()
            print ("User already in database")
            titolo = Label(regframe, text='USER ALREADY REGISTERED', bg="black", fg="orange", font=("helvetica", 13))
            titolo.grid(row=6, column=0, sticky="WE", padx=10, pady=10)

    regframe = Toplevel(root)
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
                print( "Login Success")
                titolo = Label(resultframe, text='     LOGIN SUCCESS!     ', bg="black", fg="green", font=("helvetica", 17))
                titolo.grid(row=6, column=0, sticky="WE", padx=30, pady=10)
            else:
                print( "Username or password is incorrect")
                titolo = Label(resultframe, text='Username or password\nis incorrect', bg="black", fg="red", font=("helvetica", 13))
                titolo.grid(row=6, column=0, sticky="WE", padx=10, pady=10)
        else:
            print( "Username or password is incorrect")
            titolo = Label(resultframe, text='Username or password\nis incorrect', bg="black", fg="red", font=("helvetica", 13))
            titolo.grid(row=6, column=0, sticky="WE", padx=10, pady=10)

    logframe = Toplevel(root)
    logframe.geometry("300x250")
    logframe.title("User Login")
    logframe.configure(background='black')
    logframe.resizable(False, False)
    logframe.grid_columnconfigure(0, weight=1)
    logframe.iconbitmap("C:\cybaze.ico")

    resultframe = Frame(logframe)
    resultframe.configure(background='black')
    resultframe.grid(row=6, column=0)

    titolo = Label(logframe, text='USER LOGIN', bg="black",fg="violet",font=("helvetica", 15))
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











titolo = Label(root, text="LOGIN OR REGISTER IF YOU\nWANT TO USE DATABASE", bg="black",fg="violet",font=("helvetica", 15))
titolo.grid(row=0, column=0, padx=20, pady=10)
button = Button(root, text="LOGIN", command=loginpage, font=("helvetica", 15))
button.grid(row=1, column=0, sticky="WE", padx=10, pady=15)
button = Button(root, text="NEW USER?", command=registerpage, font=("helvetica", 15))
button.grid(row=2, column=0, sticky="WE", padx=10, pady=15)

root.mainloop()