import random

#Funtion to insert a new anime in the list
def inrt(a):
    with open("Storage.txt","a+") as fh:
        b = "\n"+a
        fh.write(b)
        fh.close()

#Function to remove an anime from the list
def rev(a):
    with open("Storage.txt", "r") as fh:
        words = fh.read()
        anlist = words.split('\n')
        for anime in anlist:
            if anime == a:
                anlist.remove(anime)
    with open("Storage.txt", "w") as fh:
        for anime in anlist:
            fh.write(anime+"\n")
        

#Function to show anime names in the list
def sl():
    global namelist
    i = 0
    for anime in namelist:
        i = i+1
        print(i,")",anime)


print("Welcome to Korone. Here, Korone will decide an anime for you to watch so you don't have to go through the emotional turmoil of trying to decide what to watch")

#To read the wishlist 
with open("Storage.txt", "r") as fh:
    f = fh.readlines()
    namelist = f
    fh.close()

#To show your current wishlist 
if len(namelist) == 0:
    print("Your wishlist is empty.")
else:
    print("Your current wishlist :")
    sl()


print("\n \nPlease enter an input as specified below :")
x = input("    enter I to insert a new anime in the list \n"+ "    enter R to remove an anime from the list \n"+ "    enter anything to skip this part\n   --> ")


#To insert or remove an anime in the list
if x == "i" or x == "I":
    a = input("Enter anime name : ")
    inrt()
elif x == "r" or x == "R":
    a = input("Enter anime name : ")
    rev(a)
else:
    pass

#To show the updated list
with open("Storage.txt", "r") as fh:
    f = fh.readlines()
    namelist = f
    print("The updated list is as follows : \n")
    sl()
    fh.close()


print("\n \nKorone chooses the following anime for you to watch :")
randomizer = 0

randomizer = random.randint(0,len(namelist)-1)
print("\n    ",namelist[randomizer])