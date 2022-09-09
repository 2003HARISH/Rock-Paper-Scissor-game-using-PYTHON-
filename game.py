#  ROCK PAPER SCISSOR GAME

import random
 
def game(choise1,choise2):
    if choise1==choise2: 
        return None
    elif choise1=='r':
        if choise2=='p':
            return True
        elif choise2=='s':
            return False    
    elif choise1=='p':
        if choise2=='r':
            return False
        elif choise2=='s':
            return True
    elif choise1=='s':
        if choise2=='p':
            return False 
        elif choise2=='r':
            return True

print("computer,s turn"+" choose rock(r),paper(p),scissor(s)")
r=random.randint(1,3)
if r==1:
   choise1="r"
elif r==2:
    choise1="p"
else:
     choise1="s"
choise2=input("Your turn choose rock(r),paper(p),scissso(s) ")
 
gr=game(choise1,choise2)

print("your choise was "+choise2)
print("compute's choise was "+choise1)

if gr==None:
     print("  Its a Tie!! ")
elif gr==True:
     print("  You Win!!  ")
else:
    print("  You Lose!!  ")          
        