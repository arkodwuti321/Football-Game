import time
import random
import sys
from tkinter import *
from tkinter import messagebox

print("Welcome to the Ultimate Football Game!!")
pt=100000

#Game sub-part(not main part)    
def remove(a5):
    a6.remove(a5)


    
#Second part
def market():
    import random
    global pt
    class player:
        def __init__(self,first,lvl,skill):
            self.first=first
            self.lvl=lvl
            self.skill=skill
            self.price=lvl*100

        def full_id(self):
            return "{} \nLevel:{} \nSpeciality:{} \nPrice:{}\n".format(self.first,self.lvl,self.skill,self.price)
                
    skill=['Dribbling','Shooting','Crossing','Speed','Physique']
    f=1
    print("\nWelcome to market---->")
    while True:
        sk=random.sample(skill,2)
        sc=random.randint(50,100)
        s1=player(f"\nPlayer{f}",sc,sk)
        print(s1.full_id())
        f+=1
        ask=input("You wish to buy this player?(Y/N)\n[Press R to exit market]: ").upper()
        if ask=="Y":
            print(f"Player sold")
            pt=pt-(s1.price)
            print(f"Points left: {pt}\n")
        elif ask=="N":
            continue
        elif ask=="R":
            break
        

#Third Part
def third():
    while True:
        a3=["Barcelona","Real Madrid","Roma","Juventus","Manchester city","Manchester United","New Castle","PSG","Atletico De Madrid","Inter Milan","AC Milan","Atlanta","Liverpool","Chelsea"]
        a4=random.choice(a3)
                
        print("Welcome to Ultimate Football League Match\nSearching for your opponent...Please Wait...\n")
        time.sleep(3)
        print(f"Matchday: {c} vs {a4}(Computer)")
        

        match(a4)
        print(f"Your total points is {pt}")
                    
                    
        en=input("\nPress Y to play again\nPress M to go to the market\nPress N to quit\nPress R to exit Match: ").upper()
        if en=="Y":
            continue
        elif en=="M":
            market()
            break
        elif en=="N":
                
            if messagebox.showwarning(title="Ultimate soccer league",message="You sure you want to exit?"):
                sys.exit("Game Ended!!")
        elif en=="R":
            break

#main game part
def match(a4):
        while True:
            try:
                a5=int(input("Enter the number of goals you want to play for: "))
                break
            except ValueError:
                print("Enter a number...1,2,3...")
                continue

        l2=["H","H"]
        s2=random.choice(l2)

        user=input("\nEnter Heads(H) or Tails(T): ").upper()

        def game(user,comp):
                global pt
                pt=100000
                l3=[1,2,3,4]
                l4=[5,6]
                z=0
                u=0
                flag=False
                print(f"Computer : {comp}\n{b} : {user}")
                if user==s2:
                    print(f"{b} won the toss\n")
                    g=input("Choose to attack(a) or defense(d): ").lower()
                    if g=="a":
                        while u!=a5 or z!=a5:
                                v=0
                                print(f"The ball is with {b}.\n")
                                for k in range(4):
                                    p=int(input("Choose 1,2,3,4 to pass: "))
                                    s3=random.choice(l3)
                                    if p!=s3:
                                        v+=1
                                        print(f"pass {v}!\n")
                                        if v==4:
                                            g1=int(input("Goal Chance!!\nPress 5 or 6 to score: "))
                                            s4=random.choice(l4)
                                            if g1!=s4:
                                                print("Goaaaaaaaaaalllll!!!\n")
                                                u+=1
                                                print(f"Score: {c} - {u}  {a4} - {z}\n")
                                                if u==a5 or z==a5:
                                                    if z==a5:
                                                        pt+=50
                                                    else:
                                                        pt+=500
                                                    print(f"Your points in total is {pt}\n")
                                                    flag=True
                                                    break
                                                    
                                
                                                
                                            else:
                                                print("Save!\n")
                                                break
                                                
                                    elif p==s3:
                                        break
                                if flag:
                                    break
                                
                                
                                print(f"\nBall with {a4}.\nNow you are defending\n")
                                v=0
                                for i in range(4):
                                    p=int(input("Choose 1,2,3,4 to intercept: "))
                                    s3=random.choice(l3)
                                    if p!=s3:
                                        v+=1
                                        print(f"pass {v}!\n")
                                        if v==4:
                                            g2=int(input("Goal Chance!!\nPress 5 or 6 to save: "))
                                            s5=random.choice(l4)
                                            if g2!=s5:
                                                print("Goaaaaaaaaaalllll!!!\n")
                                                z+=1
                                                print(f"Score: {c} - {u}  {a4} - {z}\n")
                                            
                                                if u==a5 or z==a5:
                                                    if z==a5:
                                                        pt+=50
                                                    else:
                                                        pt+=500
                                                    print(f"Your points in total is {pt}\n")
                                                    flag=True
                                                    break
                                            else:
                                                print("Save!\n")
                                                break
                                    elif p==s3:
                                        break
                                if flag:
                                    break
                                

                    if g=="d":
                        while u!=a5 or z!=a5:
                                print(f"\nBall with {a4}.\nNow you are defending\n")
                                v=0
                                for i in range(4):
                                    p=int(input("Choose 1,2,3,4 to intercept: "))
                                    s3=random.choice(l3)
                                    if p!=s3:
                                        v+=1
                                        print(f"pass {v}!\n")
                                        if v==4:
                                            g2=int(input("Goal Chance!!\nPress 5 or 6 to save: "))
                                            s5=random.choice(l4)
                                            if g2!=s5:
                                                print("Goaaaaaaaaaalllll!!!\n")
                                                z+=1
                                                print(f"Score: {c} - {u}  {a4} - {z}\n")
                                                if u==a5 or z==a5:
                                                    if z==a5:
                                                        pt=pt+50
                                                    else:
                                                        pt+=500
                                                    print(f"Your points in total is {pt}\n")
                                                    flag=True
                                                    break
                                            else:
                                                print("Save!\n")
                                                break
                                    elif p==s3:
                                        break
                                if flag:
                                    break
                                
                                v=0
                                print(f"The ball is with {b}.\n")
                                for k in range(4):
                                    p=int(input("Choose 1,2,3,4 to pass: "))
                                    s3=random.choice(l3)
                                    if p!=s3:
                                        v+=1
                                        print(f"pass {v}!\n")
                                        if v==4:
                                            g1=int(input("Goal Chance!!\nPress 5 or 6 to score: "))
                                            s4=random.choice(l4)
                                            if g1!=s4:
                                                print("Goaaaaaaaaaalllll!!!\n")
                                                u+=1
                                                print(f"Score: {c} - {u}  {a4} - {z}\n")
                                                if u==a5 or z==a5:
                                                    if z==a5:
                                                        pt+=50
                                                    else:
                                                        pt+=500
                                                    print(f"Your points in total is {pt}\n")
                                                    flag=True
                                                    break
                                            else:
                                                print("Save!\n")
                                                break
                                                
                                    elif p==s3:
                                        break
                                if flag:
                                    break
                                
             
                flag=False   
                if comp==s2:
                    
                    print(f"\n{a4} won the toss")
                    l5=["attack","defend"]
                    s5=random.choice(l5)
                    print(f"{a4} chooses to {s5}")
                    while u!=a5 or z!=a5:
                        if s5=="attack":
                           print(f"Ball with {a4}.\nNow you are defending\n")
                           v=0
                           for i in range(4):
                                p=int(input("Choose 1,2,3,4 to intercept: "))
                                s3=random.choice(l3)
                                if p!=s3:
                                    v+=1
                                    print(f"pass {v}!\n")
                                    if v==4:
                                        g2=int(input("Goal Chance!!\nPress 5 or 6 to save: "))
                                        s5=random.choice(l4)
                                        if g2!=s5:
                                            print("Goaaaaaaaaaalllll!!!\n")
                                            z+=1
                                            print(f"Score: {c} - {u}  {a4} - {z}\n")
                                            if z==a5 or u==a5:
                                                if z==a5:
                                                    pt+=50
                                                else:
                                                    pt+=500
                                                print(f"Your points in total is {pt}\n")
                                                flag=True
                                                break
                                        else:
                                            print("Save!\n")
                                            break
                                elif p==s3:
                                    break
                        if flag:
                            break
                                
                        v=0
                        print(f"The ball is with {b}.\n")
                        for k in range(4):
                            p=int(input("Choose 1,2,3,4 to pass: "))
                            s3=random.choice(l3)
                            if p!=s3:
                                v+=1
                                print(f"pass {v}!\n")
                                if v==4:
                                    g1=int(input("Goal Chance!!\nPress 5 or 6 to score: "))
                                    s4=random.choice(l4)
                                    if g1!=s4:
                                        print("Goaaaaaaaaaalllll!!!\n")
                                        u+=1
                                        print(f"Score: {c} - {u}  {a4} - {z}\n")
                                        if u==a5 or z==a5:
                                            if z==a5:
                                                pt+=50
                                            else:
                                                pt+=500
                                            print(f"Your points in total is {pt}\n")
                                            flag=True
                                            break
                                    else:
                                        print("Save!\n")
                                        break
                            elif p==s3:
                                break
                        if flag:
                            break
                                    
                        if s5=="defend":
                            while u!=a5 or z!=a5:
                                v=0
                                print(f"The ball is with {b}.\n")
                                for k in range(4):
                                    p=int(input("Choose 1,2,3,4 to pass: "))
                                    s3=random.choice(l3)
                                    if p!=s3:
                                        v+=1
                                        print(f"pass {v}!\n")
                                        if v==4:
                                            g1=int(input("Goal Chance!!\nPress 5 or 6 to score: "))
                                            s4=random.choice(l4)
                                            if g1!=s4:
                                                print("Goaaaaaaaaaalllll!!!\n")
                                                u+=1
                                                print(f"Score: {c} - {u}  {a4} - {z}\n")
                                                if u==a5 or z==a5:
                                                    if z==a5:
                                                        pt+=50
                                                    else:
                                                        pt+=500
                                                    print(f"Your points in total is {pt}\n")
                                                    flag=True
                                                    break
                                            else:
                                                print("Save!\n")
                                                break
                                                                
                                        elif p==s3:
                                            break
                                if flag:
                                    break

                                v=0
                                print(f"The ball is with {a4}.\n")
                                for k in range(4):
                                    p=int(input("Choose 1,2,3,4 to intercept: "))
                                    s3=random.choice(l3)
                                    if p!=s3:
                                        v+=1
                                        print(f"pass {v}!\n")
                                        if v==4:
                                            g1=int(input("Goal Chance!!\nPress 5 or 6 to score: "))
                                            s4=random.choice(l4)
                                            if g1!=s4:
                                                print("Goaaaaaaaaaalllll!!!\n")
                                                u+=1
                                                print(f"Score: {c} - {u}  {a4} - {z}\n")
                                                if z==a5 or u==a5:
                                                    if z==a5:
                                                        pt+=50
                                                    else:
                                                        pt+=500
                                                    print(f"Your points in total is {pt}\n")
                                                    flag=True
                                                    break
                                            else:
                                                print("Save!\n")
                                                break
                                    elif p==s3:
                                        break
                                if flag:
                                    break

        if user=="H":
            comp="T"
            game(user,comp)
                
                
        elif user=="T":
            comp="H"
            game(user,comp)
    
while True:
    
    #First Part
    while True: 
        a=input("\nAre you ready to play the game?(Press R to know the rules)\nEnter 'Y' for yes and 'N' for no: ").upper()

        if a=="Y":
           b=input("\nWelcome to the ultimate football league!\nEnter your name: ")
           c=input("Team Name: ")
           print(f"Welcome {b}!!!, your ultimate team is {c}.Lead your team to victory.\nYou have been given 100,000 points. Using this you can buy players and create your dream Team.")

           #control centre
           while True:
               en=input("\nPress K to start playing\nPress M to go to the market\nPress N to quit\nPress T to start as a new user: ").upper()
               if en=="K":
                    third()
                    continue
               elif en=="M":
                    market()
                    continue
               elif en=="N":
                    from tkinter import *
                    from tkinter import messagebox
                    if messagebox.showwarning(title="Ultimate soccer league",message="You sure you want to exit?"):
                       sys.exit("Game Ended!!")
               elif en=="T":
                   break
            

        elif a=="N":
           from tkinter import *
           from tkinter import messagebox
           if messagebox.showwarning(title="Ultimate soccer league",message="You sure you want to exit?"):
               sys.exit("Game ended")

        elif a=="R":
           print("""RULES:-

1) Create your Dream Team. Enter your name.

2) You will be given 100,000p in the beginning. Using that you can buy players. 
   Buying players increases your chances of winning. 

3) Your points will increase on the basis of your matches. 
    500p --- For winning
    100p --- For draw
    50p  --- For loss

4) Match Rules:
    a) Toss decides what you get - attacking/defending
    b) There will be a total of 4 passes where you have to press any no. from 1-4 and after that comes goal chance.
    c) In Goal Chance you can press 5 or 6. 
    d) Indifferent numbers will count to as a pass, similarly for goal chances indifferent numbers will count as a goal.
    e) Similar numbers will count as an intercept or save.
    f) You can choose for every match - max goals""")
           a1=input("\nPress 'b' to back to login or 'q' to quit: ").lower()
           if a1=="b":
                continue
           else:
                
                if messagebox.showwarning(title="Ultimate soccer league",message="You sure you want to exit?"):
                    sys.exit("Game ended")
            
    
                
    

    

    
    
    
    
    
