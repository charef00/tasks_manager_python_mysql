import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as popup
from model import Connexion as Cs



ID=None
conn=Cs()
conn.connect()

#-------------------------- controller ----------------
def addTask():
    desc=add_input.get()
    print(f"add Task {desc}")
    conn.add(desc)
    show()
    popup.showinfo('Message','tash added successfully')
def updateTask():
    global ID
    if ID != None:
        conn.update(id=ID,description=update_input.get())
        show()
        
    print(f"update Task {ID}")
def deleteTask():
    conn.delete(ID)
    show()
def selectItem(event):
    global ID
    seletedItem=my_tree.selection()[0]
    ID=my_tree.item(seletedItem)["text"]
    values=my_tree.item(seletedItem)["values"]
    update_input.delete(0,'end')
    update_input.insert(0,values[0])
    print(f"select {id}")

def show():
    add_input.delete(0,'end')
    global ID
    update_input.delete(0,'end')
    ID=None
    my_tree.delete(*my_tree.get_children())
    tasks=conn.getAll()
    for task in tasks:
        my_tree.insert('', tk.END, text=task[0],values=(task[1],task[2]))


#---------------- view ----------------------
frame=tk.Tk()
frame.geometry("500x500")
frame.title("task manager")

my_tree=ttk.Treeview(frame,columns=("description","indicateur"))
my_tree.heading("#0",text="ID")
my_tree.heading("description",text="Description")
my_tree.heading("indicateur",text="Indicateur")
my_tree.column("#0",width=50)
my_tree.column("description",width=200)
my_tree.column("indicateur",width=50)
my_tree.pack(side=tk.LEFT,fill=tk.BOTH,)

desc_label=tk.Label(frame,text="ADD Description")
desc_label.pack(side=tk.TOP,padx=10,pady=10)
add_input=tk.Entry(frame)
add_input.pack(side=tk.TOP)
add_button=tk.Button(frame,text="add",command=addTask)
add_button.pack(side=tk.TOP,padx=20,pady=10)

update_label=tk.Label(frame,text="Update or Delete Description")
update_label.pack(side=tk.TOP,padx=10,pady=10)
update_input=tk.Entry(frame)
update_input.pack(side=tk.TOP)
update_button=tk.Button(frame,text="Update",command=updateTask)
update_button.pack(side=tk.TOP, padx=5, pady=5)
delete_button=tk.Button(frame,text="Delete",command=deleteTask)
delete_button.pack(side=tk.TOP, padx=5, pady=5)
my_tree.bind('<ButtonRelease-1>',selectItem)
show()



frame.mainloop()