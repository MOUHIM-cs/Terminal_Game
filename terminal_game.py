health = 100 

Hero = input("Enter the name of your hero :")
print("Hello !",Hero ,"This game is for survaving ")

print("Welcome to Day in Life !")
#-------------------------------------------------------#
print("Q1)  You should fight one of them :")
print(" 1) Dawn")
print(" 2) Dusk")

answer = int(input("Enter anssweer (1-2) :"))

if answer == 1 :
    health += 10
    print ("WOHOA YOU WON 10 HP MORE")
elif answer == 2 :
    health -=7 
    print("OOPS ! , YOU'RE NOT READY FOR THAT")
else :
    print("WRONG INPUT")

#-------------------------------------------------------#
print("The emergency message was stark: Monster")
print("Q2)  Choose one who help :")
print(" 1) Your Wife")
print(" 2) Your World")

answer = int(input("Enter anssweer (1-2) :"))

if answer == 1 :
    print ("WOHOA YOU HELPED YOUR WIFE BUT YOUR WORLD IS ATTACKED BY THE MONSTER")
print("What should you do ?:")
print(" 1) You Stay with your wife and choose the love")
print(" 2) You run to help your world from the monster")
answer = int(input("Enter anssweer (1-2) :"))
if answer == 2 :
    print("That's your opinion but make sure you are not the hero more in your world")
elif answer == 2 :
    print("Your wife is scared from losing you , but you are such a brave hero and you gain the respect and the love from your world")
else :
    print("WRONG INPUT")

#-------------------------------------------------------#
print("The Monster")
print("Q2)  Choose Your Weapon :")
print(" 1) Aetherium Lance")
print(" 2) Harmonic Mallet")

answer = int(input("Enter anssweer (1-2) :"))

if answer == 1 :
    health += 90
    print ("Good choice")
    print ("The weapon you choosed , it gives enough health to kill the monster")
    print("You are such a brave hero")
    print("Congralution",Hero,"you won the battle and you gain honor")
    print()
    print("Hero :", health)
    print("The End of the game , we appreciate you ",Hero," see you later our Hero")
    

elif answer == 2 :
    print("Sorry for that ! but it's a bad weapon and the monster won the battle")
    print("I know it's a bad ending but you tryed your best",Hero,"Maybe in another life ! ")
else :
    print("WRONG INPUT")




