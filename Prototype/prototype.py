import random
import tkinter
import customtkinter


#Funtion to insert a new anime in the list
def inrt():
    a = name.get()
    with open("Storage.txt","a+") as fh:
        b = "\n"+a
        fh.write(b)
    crulist(listbox)

#Function to remove an anime from the list
def rev():
    a = name.get()
    with open("Storage.txt", "r") as fh:
        words = fh.read()
        anlist = words.split('\n')
        for anime in anlist:
            if anime == a:
                anlist.remove(anime)
    with open("Storage.txt", "w") as fh:
        for anime in anlist:
            if anime:#To avoid writing empty lines
                fh.write(anime+"\n")
    crulist(listbox)
        
#To read your current list
def read_list():
    #To read the wishlist 
    fh = open("Storage.txt", "r")
    f = fh.readlines()
    namelist = f
    return list(namelist)


#To show your current wishlist 
def crulist(listbox):
    namelist = read_list()
    if len(namelist) == 0:
        x = "Your wishlist is empty."
        return x
    else:
        x = "\n".join([f"{i + 1}) {anime}" for i, anime in enumerate(namelist[:-1])])
    listbox.configure(text=x)


#To chose a random anime from the list
def randeer():
    crulist(listbox)
    namelist = read_list()
    randomizer = 0
    randomizer = random.randint(0,len(namelist)-1)
    choice = namelist[randomizer]
    status.configure(text= "Korone choses the following anime for you: \n"+choice)


#GUI----------------------------------------------------------------------------------------------------------------------------------------
#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app = customtkinter.CTk()
app.geometry("700x750")
app.title("Korone")
app.grid_columnconfigure(0, weight=1)

#App elements
#welcome note:
welcome = customtkinter.CTkLabel(app, text="Welcome to Korone")
welcome.grid(row=0, column=1, padx=20, pady=20)

#This is where the list is supposed to show
listbox = customtkinter.CTkLabel(app, text = "")
listbox.grid(row=1, column=1, padx=20, pady=20)
crulist(listbox)

#text space to enter anime name:
animename = tkinter.StringVar()
name = customtkinter.CTkEntry(app, width=300, height=30, textvariable=animename)
name.grid(row=2, column=1, padx=20, pady=20)

#button add a new anime in the list
adder = customtkinter.CTkButton(app, text="Add", command=inrt)
adder.grid(row=3, column=0, padx=20, pady=20)


#button to remove an anime from the lsit
remover = customtkinter.CTkButton(app, text="Remove", command=rev)
remover.grid(row=3, column=2, padx=20, pady=20)

#to show list
Wishlist = customtkinter.CTkButton(app, text="Refresh Wishlist", command=crulist(listbox))
Wishlist.grid(column=1,padx=20, pady=20)

#button to chose random anime from the list
Korone = customtkinter.CTkButton(app, text="Korone", command=randeer)
Korone.grid(column = 1, padx=20,pady=20)

#label to show anime name
status = customtkinter.CTkLabel(app, text="")
status.grid(row=3, column=1,padx=20,pady=20)


#to run the app
app.mainloop()