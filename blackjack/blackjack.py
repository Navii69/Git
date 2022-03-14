var,cash,var2=1,500,2
bjval=['2','2','2','2','3','3','3', '3','4','4','4', '4','5','6','7','8','9', '10','J','K','Q', 'A']
bjfaceval=['J','K','Q']
player=None
bot=None
player_ace,bot_ace=0,0
import random
from rich import print as print
import sys
from rich.progress import track
from time import sleep
from rich.console import Console

for i in track(range(100), description='[green]Processing data'):
    sleep(0.015)
console = Console()
print("[#A1045A]Welcome to BlackJack[/#A1045A]")
#USER DEFINED FUNCTIONS_______________________________________
def cardsshow(a):
    print("[#d279a6]Dealer-\nCards: [/#d279a6]")
    for i in range(0,a):
        print(bot[i],end=' ')
    print("[#d279a6]\nTotal: [/#d279a6]",botpoints)
    print("______________")
    print("[#FFB6C1]You-\nCards: [/#FFB6C1]")
    for j in range(0,a):
        print(player[j],end=' ')
    print("[#FFB6C1]\nTotal: [/#FFB6C1]",playerpoints)
    
#_____________________________________________________
def cards(a):
    print("[#d279a6]Dealer-\nCards: \n[/#d279a6]",bot[0],"?"*(a-1))
    print("[#d279a6]Total: ?[/#d279a6]")
    print("______________")
    print("[#FFB6C1]You-\nCards: [/#FFB6C1]")
    for j in range(0,a):
        print(player[j],end=' ')
    print("[#FFB6C1]\nTotal: [/#FFB6C1]",playerpoints)
#_____________________________________________________
def stand():
        print('[#c56363]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[/#c56363]')
        global cash
        if playerpoints>botpoints:
            print("[#FFA500]YOU WON[/#FFA500]")
            cash+=cash_to_bid*2
            print("[#d1dd24]Your cash now is[/#d1dd24]",cash)
        elif playerpoints<botpoints:
            print("[#FFA500]YOU LOST[/#FFA500]")
            print("[#d1dd24]Your cash now is[/#d1dd24]",cash)
        else:
            print("[#FFA500]TIED[/#FFA500]")
            cash+=cash_to_bid
            print("[#d1dd24]Your cash now is[/#d1dd24]",cash)
#__________________________________________
def situation():
        global cash,con
        print('[#c56363]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[/#c56363]')
        if playerpoints==21:
            print("[#FFA500]YOU WON[/#FFA500]")
            cash+=cash_to_bid*2
            print("[#d1dd24]Your cash now is[/#d1dd24]",cash)
            con=1
        elif playerpoints>21:
            print("[#FFA500]YOU LOST[/#FFA500]")
            print("[#d1dd24]Your cash now is[/#d1dd24]",cash)
            con=1
        elif botpoints==21:
            print("[#FFA500]YOU LOST[/#FFA500]")
            print("[#d1dd24]Your cash now is[/#d1dd24]",cash)
            con=1
        elif botpoints>21:
            print("[#FFA500]YOU WON[/#FFA500]")
            cash+=cash_to_bid*2
            print("[#d1dd24]Your cash now is[/#d1dd24]",cash)
            con=1
#__________________________________________
def points():
        global player_ace,bot_ace,botpoints,playerpoints
        if player.count('A')>1:
            player_ace+=1
        elif player_ace==0 and 'A' in player:
            player_ace+=1
        elif bot.count("A")>1:
            bot_ace+=1
        elif bot_ace==0 and "A" in bot:
            bot_ace+=1
        botpoints,playerpoints=0,0
        for i in bot:
            if i in bjfaceval:
                botpoints+=10
            elif i=="A":
                continue
            else:
                botpoints+=int(i)
        botpoints+=bot_ace
        for j in player:
            if j in bjfaceval:
                playerpoints+=10
            elif j=='A':
                continue
            else:
                playerpoints+=int(j)
        playerpoints+=player_ace
#_____________________________________________
def res():
    global var,var2
    restart=int(console.input("[#bd8a4e]Do you wanna play again\nWrite 1 for YES and 2 for NO: [/#bd8a4e]"))
    if restart==1:
        var2=1
    elif restart==2:
        print("[#48c2ce]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nHave a great time\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[/#48c2ce]")
        var=2
        sys.exit()

#START_______________________________________________________
while var==1:
    con=0
    random.shuffle(bjval)
    bjstartmenu=int(console.input("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬[#da1d4b]\n1.Start[/#da1d4b]\n[#d1dd24]2.View Cash[/#d1dd24]\n[#48c2ce]3.Exit[/#48c2ce]\n[#da1d4b]Enter you choice: [/#da1d4b]"))
    if bjstartmenu==3:
        print("[#48c2ce]Have a great time[/#48c2ce]")
        sys.exit()
#_________________________________________________________________
    elif bjstartmenu==2:
        print('[#d1dd24]You have[/#d1dd24]', cash)
        continue
#________________________________________________________________
    elif bjstartmenu==1:
        var2 = 2 
        cash_to_bid=int(console.input("[#0218f1]Enter the amount you wanna bid: [/#0218f1]"))
        if cash_to_bid>cash:
            print("[#0218f1]You dont have enough cash[/#0218f1]")
            continue
        elif cash_to_bid<125:
            print("[#0218f1]Minimum value to bid is  125[/#0218f1]")
            continue
        else:
            cash-=cash_to_bid
#RANDOM CARDS DISTRIBUTION FIRST PHASE____________________
            while var2==2:
                if var==1:
                    botpoints,playerpoints=0,0
                    player=random.sample(bjval,2)
                    bot=random.sample(bjval,2)
                    if 'A' in player:
                        player_ace=11
                    if 'A' in bot:
                        bot_ace=11
    #POINTS CALCULATION FIRST PHASE_________________________-
                    points()
                    a=2
                    cards(a)
    #SITUATION HANDLING FIRST PHASE_______________________________
                    situation()
                    if con==1:
                        cardsshow(a)
                        res()
    #FIRST CODE PHASE COMPLETED.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    choice=int(console.input("[#8d02f1]1 for Hit and 2 for Stand: [/#8d02f1]"))
    #RANDOM CARD DISTRIBUTION SECOND PHASE__________________________
                    if choice==1:
                        player.append(random.choice(bjval))
                        bot.append(random.choice(bjval))
    #POINTS CALCULATION SECOND PHASE___________________________________
                        points()
                        a=3
                        cards(a)
    #SITUATION HANDLING SECOND PHASE____________________________
                        situation()
                        if con==1:
                            cardsshow(a)
                            res()
    #SECOND PHASE CODE COMPLETED________________________________
                        choice_second=int(console.input("[#8d02f1]Press 1 to Hit and 2 to Stand: [/#8d02f1]"))
    #THIRD PHASE CODE_________________________________________________
                        if choice_second==1:
                            player.append(random.choice(bjval))
                            bot.append(random.choice(bjval))
    #POINTS CALCULATION THRID PHASE_____________________________________
                            points()
                            a=4
                            cards(a)
    #SITUATION HANDLING THIRD PHASE___________________________________
                            situation()
                            if con==1:
                                cardsshow(a)
                                res()
    #THIRD PHASE CODE COMPLETED_____________________________
                            choice_third=int(console.input("[#8d02f1]Press 1 to Hit and 2 to Stand: [/#8d02f1]"))
    #FOURTH PHASE CODE_________________________________________________
                            if choice_third==1:
                                player.append(random.choice(bjval))
                                bot.append(random.choice(bjval))
    #POINTS CALCULATION FOURTH PHASE_______________________________________
                                points()
                                a=5
                                cards(a)
    #SITUATION HANDLING_________________________________________________
                                situation()
                                if con==1:
                                    cardsshow(a)
                                    res()
    #FOURTH PHASE COMPLETED_________________________________________
                                choice_fourth=int(console.input("[#8d02f1]Press 1 to Stand and 0 to Fofeit[/#8d02f1]"))
    #STAND SITUATION(FOURTH PHASE)_________________________________________
                                if choice_fourth==1:
                                    stand()
                                    a=5
                                    cardsshow(a)
                                    res()
                                if choice_fourth==0:
                                    print("Dealer took all your money LOL")
                                    res()
    #STAND SITUATION(THIRD PHASE)__________________________________
                            elif choice_third==2:
                                stand()
                                a=4
                                cardsshow(a)
                                res()
    #STAND SITUATION(SECOND PHASE)____________________________________
                        elif choice_second==2:
                                stand()
                                a=3
                                cardsshow(a)
                                res()
    #STAND SITUATION(FIRST PHASE)___________________
                    elif choice==2:
                            stand()
                            a=2
                            cardsshow(a)
                            res()