from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime
import ast
from tkinter import messagebox


#          class

f = open("id.txt", "r")
id_value = int(f.read())
f.close()


class Info:

    id = id_value

    def __init__(self, name="", age=0, filier='', admin=''):
        self.id = Info.id
        self.name = name
        self.age = age
        self.filier = filier
        self.admin = admin
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def class_add_data(self):
        self.name = fname_entry.get()
        self.age = age_entry.get()
        self.filier = filier_entry.get()
        self.admin = admin_var.get()

        if self.name == '' or self.age == '' or self.filier == "":
            messagebox.showerror("Error", "Empty data! Cannot write to file.")

        else:
            Info.id += 1
            with open("id.txt", "w") as f:
                f.truncate(0)
                f.write(str(Info.id))

            data = f"""[
                    ["id","{Info.id}"],
                    ["name","{self.name}"],
                    ["age", "{self.age}"],
                    ["filiere","{self.filier}"],
                    ["admin", "{self.admin}"],
                    ["date","{self.date}"]
                ],"""
            with open("text.txt", "a") as f:
                f.write(data)



# --------------------------------------   add function



def add_data():
    test = Info()
    test.class_add_data()



def display_data():
    with open("text.txt", "r") as f:
        data = f.read()
    my_list = ast.literal_eval(data)

    new_list = []
    for line in my_list:
        row = []
        for item in line:
            row.append(item[1])
        new_list.append(row)
    tree.delete(*tree.get_children())
    for item in new_list:
        tree.insert("", tk.END, values=item)


def delete_data():
    id = supp_entry.get()
    if id == '':
        messagebox.showerror("Error", "  ID ??")

    else:
        file_list = []
        condition=FALSE
        with open("text.txt", "r") as f:
            data = f.read()
        my_list = ast.literal_eval(data)

        new_list = []
        for line in my_list:
            row = []

            for item in line:
                row.append(item[1])
            new_list.append(row)

        for line in my_list:
            line = list(line)

            for lines in line:
                lines = list(lines)
                if lines[0] == 'id' and lines[1] == id:
                    condition=TRUE
                    break
                else:
                    if line not in file_list:
                        file_list.append(line)

        result = str(file_list)

        result = result[1:-1] + ","

        with open("text.txt", "w") as f:

            f.write(result)


        if condition:
            messagebox.showinfo("success", "success")
        else:
            messagebox.showwarning("Error","ID "+ id+" n'exist pas")




def search_data():
    re_value = recher_id.get()
    change_list = []
    afficher_list = []

    if re_value=="":
        messagebox.showerror("Error","No ID")

    else:
        with open("text.txt", "r") as f:
            data = f.read()

        my_list = ast.literal_eval(data)

        for lst in my_list:
            for item in lst:
                if item[0] == 'id' and item[1] == re_value:
                    change_list = lst
                    break

        for line in change_list:
            row = [line[1] for line in change_list]
            afficher_list.append(row)

        for item in afficher_list:
            tree.delete(*tree.get_children())
            tree.insert("", tk.END, values=item)





def search_data2():
    re_value = recher_nom.get()

    change_list = []
    afficher_list = []

    if re_value == "":
        messagebox.showerror("Error", "  No  Nom !!")

    else:
        with open("text.txt", "r") as f:
            data = f.read()

        my_list = ast.literal_eval(data)

        for lst in my_list:
            for item in lst:
                if item[0] == 'name' and item[1] == re_value:
                    change_list = lst
                    break

        for line in change_list:
            row = [line[1] for line in change_list]
            afficher_list.append(row)

        for item in afficher_list:
            tree.delete(*tree.get_children())
            tree.insert("", tk.END, values=item)


# --------------------------------------   Tkinter



main = Tk()


# ---------------  STYLE
main.title("Gestion")
main.geometry("1500x900")
main['bg'] = "#7b7f87"
main.iconbitmap("icon.ico")

# ---------------  affichage

# ----------------form
h1 = Label(main, text="Gestion De Etudiant", font="Times 30 italic bold", bg="#7b7f87", fg="#E0E0E0", width=100)
h1.grid(row=0, column=0, columnspan=2, sticky="w")


form_frame = Frame(main, bg="#a0a0a0", bd=0, relief="solid", highlightbackground="white", highlightthickness=1)
form_frame.grid(row=1, column=0, rowspan=5, padx=10, pady=10, sticky="nsew")

fname_label = Label(form_frame, text="Nom et Prenom", width=20, font="Times 12 italic bold")
fname_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

fname_entry = Entry(form_frame, width=40)
fname_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)

age_label = Label(form_frame, text="Age", width=20, font="Times 12 italic bold")
age_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

age_entry = Entry(form_frame, width=40)
age_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

filier_label = Label(form_frame, text="Filier", width=20, font="Times 12 italic bold")
filier_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

filier_entry = Entry(form_frame, width=40)
filier_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

admin_label = Label(form_frame, text="Admin", width=20, font="Times 12 italic bold")
admin_label.grid(row=6, column=0, sticky="e", padx=10, pady=10)

admin_frame = Frame(form_frame)


admin_frame.grid(row=6, column=1, sticky="w", padx=10, pady=10)

admin_var = StringVar()
admin_var.set("Oui")

admin_oui = Radiobutton(admin_frame, text="Oui", variable=admin_var, value="Oui")
admin_oui.pack(side="left")

admin_non = Radiobutton(admin_frame, text="Non", variable=admin_var, value="Non")
admin_non.pack(side="left")


columns = ("ID", "Nom", "Age", "Filier", "Admin", "inscription")
# Set the style for the Treeview
style = ttk.Style(main)
style.theme_use("clam")
style.configure("Treeview", background="#a0a0a0", fieldbackground="#a0a0a0", foreground="black")

# Create the Treeview widget
tree = ttk.Treeview(main, columns=columns, show='headings', height=6)
tree.grid(row=1, column=1, rowspan=6, padx=10, pady=10, sticky="nsew")

main.grid_rowconfigure(1, weight=1)
main.grid_columnconfigure(1, weight=1)


# headings
tree.heading('ID', text='ID')
tree.heading('Nom', text='Nom')
tree.heading('Age', text='Age')
tree.heading('Filier', text='Filier')
tree.heading('Admin', text='Admin')
tree.heading('inscription', text='inscription')

ajouter_button = Button(form_frame, text="Ajouter", width=25,height=1, font="arial 9 ",relief="groove",bg='#1aeaed',command=add_data)
ajouter_button.grid(row=7, column=0, sticky="w", padx=10, pady=20)

afficher_button = Button(form_frame, text="Afficher Les Donnees", width=25,height=1, font="arial 9 ",relief="groove",bg='#1aeaed', command=display_data)
afficher_button.grid(row=7, column=1, sticky="w", padx=10, pady=20)



supprimer_button = Button(form_frame, text="Supprimer par ID", width=25,height=1, font="arial 9 ",relief="groove",bg='#1aeaed', command=delete_data )
supprimer_button.grid(row=11, column=0, sticky="w", padx=10, pady=10)
supp_entry=Entry(form_frame,width=10, justify = CENTER,font=("courier ",9,'bold'))
supp_entry.grid(row=11,column=1, sticky="w", padx=10, pady=10)
recherch_button = Button(form_frame, text="Recherch (ID )", width=25,height=1, font="arial 9 ",relief="groove",bg='#1aeaed',  command=search_data)

recherch_button2 = Button(form_frame, text="Recherch (Nom )", width=25,height=1, font="arial 9 ",relief="groove",bg='#1aeaed',  command=search_data2)

recher_id = Entry(form_frame,width=10, justify = CENTER,font=("courier ",9,'bold'))

recher_nom = Entry(form_frame,width=10, justify = CENTER,font=("courier ",9,'bold'))
recher_nom.grid(row=9, column=1, sticky="w", padx=10, pady=10)

recher_id.grid(row=8, column=1, sticky="w", padx=10, pady=10)
recherch_button.grid(row=8, column=0, sticky="w", padx=10, pady=10)
recherch_button2.grid(row=9, column=0, sticky="w", padx=10, pady=10)












main.mainloop()
