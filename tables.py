import tkinter as tk
import tkinter.messagebox as messagebox

root = tk.Tk()
root.geometry("720x500+280+110")
root.minsize("720","490")
root.maxsize("750","510")
root.title("tables")


heading_frame = tk.Frame(root,borderwidth = 5,relief = "sunken")
heading_frame.pack(fill = "x",anchor = "n")
heading_label = tk.Label(heading_frame,text = "TABLES",font = ("verdana",24,"bold"),bg = "dark blue",fg = "white")
heading_label.pack(fill = "x")

def result():

    listbox.delete(0,tk.END)
    table_value = tableentryvar.get()
    till_value = tillentryvar.get()

    vallen1 = len(table_value)
    vallen2 = len(till_value)

    if vallen1 == 0 and vallen2 == 0:
        messagebox.showerror("error","please enter values to proceed")
        error1.config(text = "",font = ("verdana",1,"bold"))
        error2.config(text = "",font = ("verdana",1,"bold"))

    elif vallen1 == 0 and vallen2 > 0:
        messagebox.showerror("error","please enter values to proceed")
        error1.config(text = "",font = ("verdana",1,"bold"))
        error2.config(text = "",font = ("verdana",1,"bold"))

    elif vallen1 > 0 and vallen2 == 0:
        messagebox.showerror("error","please enter values to proceed")
        error1.config(text = "",font = ("verdana",1,"bold"))
        error2.config(text = "",font = ("verdana",1,"bold"))
        
    else:
        e1 = 1
        e2 = 1

        try:
            b = int(table_value)
            e1 = 1
        except:
            e1 = 0

        try:
            a = int(till_value)
            e2 = 1
        except:
            e2 = 0

        if e1 == 0 and e2 == 0:
           error1.config(text = "error,hi i am lovish grover",font = ("verdana",10,"bold"))
           error2.config(text = "error,please enter int value",font = ("verdana",10,"bold"))
        elif e1 == 0 and e2 == 1:
            error1.config(text = "error,please enter int value",font = ("verdana",10,"bold"))
            error2.config(text = "",font = ("verdana",1,"bold"))
        elif e1 == 1 and e2 == 0:
            error1.config(text = "",font = ("verdana",1,"bold"))
            error2.config(text = " grover,please enter int value",font = ("verdana",10,"bold"))
        else :
            error1.config(text = "",font = ("verdana",1,"bold"))
            error2.config(text = "",font = ("verdana",1,"bold"))
        
            for i in range(1,a+1):
                listbox.insert(i,f"{b} X {i} = {b*i}")


listframe = tk.Frame(root)
listframe.pack(fill = "both",anchor = "ne",side = "right",expand = True)

ans = tk.Label(listframe,borderwidth = 5,relief = "solid",text = "ANSWER",font = ("verdana",23,"bold"),fg = "red",bg ="yellow")
ans.pack(fill = "x",anchor = "n")

scrollbar = tk.Scrollbar(listframe)
scrollbar.pack(side = "right",fill = "y")
    
listbox = tk.Listbox(listframe,borderwidth = 5,relief = "sunken")
listbox.pack(fill = "both",anchor = "ne",side = "right",expand = True)

listbox.config(yscrollcommand = scrollbar.set)

scrollbar.config(command = listbox.yview)


query_frame = tk.Frame(root,borderwidth = 5,bg = "light grey",relief = "sunken")
query_frame.pack(fill = "both",expand = True,anchor = "n",side = "left")

table_of = tk.Label(query_frame,text = "TABLE OF",font = ("ariel",18,"bold"),bg = "light grey")
table_of.pack(ipady = 20)

tableentryvar = tk.StringVar()

entry1 = tk.Entry(query_frame,textvariable = tableentryvar,font = ("verdana",17,"bold"),bg = "white",fg = "black")
entry1.pack(pady = 10)

error1 = tk.Label(query_frame,text = "",font = ("verdana",1,"bold"),bg = "light grey",fg = "red")
error1.pack()

till = tk.Label(query_frame,text = "TILL",font = ("ariel",18,"bold"),bg = "light grey")
till.pack(ipady = 20,)

tillentryvar = tk.StringVar()

entry2 = tk.Entry(query_frame,textvariable = tillentryvar,font = ("verdana",17,"bold"),bg = "white",fg = "black")
entry2.pack(padx = 20)

error2 = tk.Label(query_frame,text = "", font = ("verdana",1,"bold"),bg = "light grey",fg = "red")
error2.pack()

go = tk.Button(query_frame,text = "GO!",font = ("verdana",20,"bold"),fg = "yellow",bg = "red",padx = 20,command = result)
go.pack(pady = 40)

root.mainloop()

