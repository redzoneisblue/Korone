import random

#Funtion to insert a new anime in the list
def inrt(a):
    global namelist
    l = len(namelist)-1
    namelist.insert(l, a)

#Function to show anime names in the list
def sl():
    global namelist
    i = 0
    for anime in namelist:
        i = i+1
        print(i,")",anime)

print("Welcome to Korone. Here, Korone will decide an anime for you to watch so you don't have to go through the emotional turmoil of trying to decide what to watch")

#To read the wishlist 
with open("Storage.txt", "r+") as fh:
    f = eval(fh.read())
    namelist = f

#To show your current wishlist 
print("Your current wishlist :")
sl()


print("Please enter an input as specified below :")
print("    enter I to insert a new anime in the list \n", "    enter R to remove an anime from the list \n", "    enter N to skip this part")
x = input()

'''
#To insert an anime in the list
if x == "i" or "I":
    a = input("Enter anime name : ")
    inrt(a)
    print(namelist)
'''

print("Korone chooses the following anime for you to watch :")
randomizer = 0

randomizer = random.randint(0,len(namelist)-1)
print(namelist[randomizer])