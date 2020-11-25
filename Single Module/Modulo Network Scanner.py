from socket import *
import time
from tkinter import *


root = Tk()
root.geometry("500x680")
root.title("ITS TTF IP HUNTER - Luca Longhi")
root.configure(background='black')
root.resizable(False,False)
root.grid_columnconfigure(0, weight=1)
root.iconbitmap("C:\cybaze.ico")




if __name__ == '__main__':
    def IndirizzoIP():
        startTime = time.time()
        target = entry.get()
        t_IP = gethostbyname(target)
        print('Starting scan on host: ', t_IP)
        franco.tag_config("open", background="green", foreground="white")
        franco.tag_config("close")
        for i in range(1, 9000000):

            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(0.001)
            conn = s.connect_ex((t_IP, i))
            if (conn == 0):
                print('Port %d: OPEN' % (i,))
                franco.insert(END, 'Port %d: OPEN' % (i,) + "\n","open")
            else:
                print('Port %d: CLOSED' % (i,))
                franco.insert(END, 'Port %d: CLOSED' % (i,)+ "\n", "close")
            s.close()
            root.update()

        finishTime = time.time()
        minuti = finishTime - startTime
        print('Time taken: ', float(minuti))




    titolo = Label(root, text="Enter the host to be scanned: ", bg="black", fg="yellow")
    titolo.grid(row=0, column=0, sticky="WE", padx=20, pady=10)

    entry = Entry()
    entry.grid(row=2, column=0, sticky="WE", padx=140, pady=10)

    frame = Frame(root)
    frame.grid(row=3, column=0)


    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    franco = Text(frame,wrap=NONE, yscrollcommand=scrollbar.set)
    franco.pack()
    franco.pack(side="left")

    scrollbar.config(command=franco.yview)


    button1 = Button(text='Check IP address', command=IndirizzoIP, bg="cyan")
    button1.grid(row=4, column=0, sticky="N", padx=10, pady=20)

root.mainloop()



