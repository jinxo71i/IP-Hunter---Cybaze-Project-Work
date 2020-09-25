from tkinter import *
import sqlite3

root = Tk()
root.geometry("500x680")
root.title("ITS TTF IP HUNTER - Luca Longhi")
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
        else:
            conn.commit()
            conn.close()
            print ("User already register")

    regframe = Toplevel(root)
    regframe.geometry("300x300")
    regframe.title("New User Registration")
    regframe.configure(background='black')
    regframe.resizable(False, False)
    regframe.grid_columnconfigure(0, weight=1)
    regframe.iconbitmap("C:\cybaze.ico")

    titolo = Label(regframe, text='registra nuovo utente')
    titolo.config(font=('helvetica', 10))
    titolo.grid(row=0, column=0, sticky="WE", padx=20, pady=10)

    regus = Entry(regframe)
    regus.grid(row=1, column=0)
    regpwd = Entry(regframe)
    regpwd.grid(row=2, column=0)
    button = Button(regframe, text="registra qui", command= registration)
    button.grid(row=3, column=0)


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
            else:
                print( "Username or password is incorrect")
        else:
            print( "Username or password is incorrect")
    logframe = Toplevel(root)
    logframe.geometry("300x300")
    logframe.title("New User Registration")
    logframe.configure(background='black')
    logframe.resizable(False, False)
    logframe.grid_columnconfigure(0, weight=1)
    logframe.iconbitmap("C:\cybaze.ico")

    titolo = Label(logframe, text='login user')
    titolo.config(font=('helvetica', 10))
    titolo.grid(row=0, column=0, sticky="WE", padx=20, pady=10)

    logus = Entry(logframe)
    logus.grid(row=1, column=0)
    logpwd = Entry(logframe)
    logpwd.grid(row=2, column=0)
    button = Button(logframe, text="LOGIN", command=login)
    button.grid(row=3, column=0)



button = Button(root, text="LogIn", command=loginpage)
button.grid(row=1, column=0)
button = Button(root, text="New User?", command=registerpage)
button.grid(row=2, column=0)

root.mainloop()