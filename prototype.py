import random

print("Welcome to Korone. Here, Korone will decide an anime for you to watch so you don't have to go through the emotional turmoil of trying to decide what to watch")

namelist = ["Naruto", "Bleach", "Dragon Ball Z", "One Piece"]

print("Your current wishlist :")
for j in range(len(namelist)):
    print(j+1, ")", namelist[j])

print("Please enter an input as specified below :")
print("    enter I to insert a new anime in the list \n", "    enter R to remove an anime from the list \n", "    enter N to skip this part")
x = input()

print("Korone chooses the following anime for you to watch :")
randomizer = 0

randomizer = random.randint(0,len(namelist))
print(namelist[randomizer])