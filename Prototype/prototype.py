import random
import tkinter
import customtkinter


#Funtion to insert a new anime in the list
def inrt():
    a = name.get()
    with open("Storage.txt","a+") as fh:
        b = "\n"+a
        fh.write(b)

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
            fh.write(anime+"\n")
        
#To read your current list
def read_list():
    #To read the wishlist 
    fh = open("Storage.txt", "r")
    f = fh.readlines()
    namelist = f
    return list(namelist)

#To show your current wishlist 
def crulist():
    namelist = read_list()
    if len(namelist) == 0:
        x = "Your wishlist is empty."
        return x
    else:
        i = 0
        for anime in namelist:
            i = i+1
            #print(i,")",anime)
            x = str(i),")",anime
            return x
    listbox.configure(text=crulist)


#To chose a random anime from the list
def randeer():
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
app.geometry("720x480")
app.title("Korone")

#App elements
#welcome note:
welcome = customtkinter.CTkLabel(app, text="Welcome to Korone. Here, Korone will decide an anime for you to watch so you don't have to go through the emotional turmoil of trying to decide what to watch")
welcome.pack(padx=20, pady=20)

#This is where the list is supposed to show
listbox = customtkinter.CTkLabel(app, text = crulist)
listbox.pack(padx=10,pady=10)

#text space to enter anime name:
animename = tkinter.StringVar()
name = customtkinter.CTkEntry(app, width=350, height=40, textvariable=animename)
name.pack()

#button add a new anime in the list
adder = customtkinter.CTkButton(app, text="Add", command=inrt)
adder.pack(padx=20,pady=20)

#button to remove an anime from the lsit
remover = customtkinter.CTkButton(app, text="Remove", command=rev)
remover.pack(padx=20,pady=20)

#to show list
Wishlist = customtkinter.CTkButton(app, text="Refresh Wishlist", command=crulist)
Wishlist.pack(padx=20,pady=20)


#button to chose random anime from the list
Korone = customtkinter.CTkButton(app, text="Korone", command=randeer)
Korone.pack(padx=20,pady=20)

#label to show anime name
status = customtkinter.CTkLabel(app, text="")
status.pack(padx=20,pady=20)


#to run the app
app.mainloop()