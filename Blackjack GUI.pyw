import random
import tkinter as tk
from tkinter import ttk

score = 0
# window properties
window = tk.Tk()
window.geometry("500x300")
window.title("Blackjack")
lineskip1 = ttk.Label(text=' ')
title = tk.Label(text="Blackjack!")
title.pack()
cardlist = []
scoretext = ttk.Label(text='Score: 0')
yougota = ttk.Label(text='You have no cards!')
cards = ttk.Label(text='Cards: ')
bust = ttk.Label(text=' ')
opcardslabel = ttk.Label(text="Opponent's cards: ")
opcard1 = random.randrange(1, 13)
opcard2 = random.randrange(1, 13)
#print(str(opcard1) + " " + str(opcard2))
opcard1abv = 0
opcard2abv = 0
newcardabv = 0
opcards = []
opcard = 0
opscore = 0
# Opponent's card #1
if opcard1 == 1:
    opcard1abv = "A"
    if opscore + 11 > 21:
        opscore = opscore + 1
    else:
        opscore = opscore + 11
    opcards.append(str(opcard1abv))
elif opcard1 > 10:
    kqj = random.randrange(1, 4)
    opscore = opscore + 10
    if kqj == 1:
        opcard1abv = 'J'
    elif kqj == 2:
        opcard1abv = 'Q'
    else:
        opcard1abv = 'K'
    opcards.append(str(opcard1abv))
else:
    opcard1abv = str(opcard1)
    opscore = opscore + opcard1
    opcards.append(str(opcard1abv))
##Opponent's card #2
if opcard2 == 1:
    opcard2abv = "A"
    if opscore + 11 > 21:
        opscore = opscore + 1
    else:
        opscore = opscore + 11
    opcards.append(str(opcard2abv))
elif opcard2 > 10:
    kqj = random.randrange(1, 4)
    opscore = opscore + 10
    if kqj == 1:
        opcard2abv = 'J'
    elif kqj == 2:
        opcard2abv = 'Q'
    else:
        opcard2abv = 'K'
    opcards.append(str(opcard2abv))
else:
    opcard2abv = str(opcard2)
    opscore = opscore + opcard2
    opcards.append(str(opcard2abv))


def ophit():
    global opscore
    global opcard
    opcard = random.randrange(1, 12)
    if opcard == 1:
        opcards.append("A")
        if opscore + 11 > 21:
            opscore = opscore + 1
        else:
            opscore = opscore + 11
    elif opcard <= 10:
        opcards.append(str(opcard))
        opscore = opscore + opcard
    else:
        jqk = random.randrange(1, 4)
        if jqk == 1:
            opcards.append("J")
        elif jqk == 2:
            opcards.append("Q")
        else:
            opcards.append("K")
        opscore = opscore + 10


##Opponent's A.I.
if opscore >= 11:
    ophit()
elif opscore == 12:
    rng = random.randrange(1, 101)
    if rng <= 98:
        ophit()
    else:
        print("Opponent is standing.")
elif opscore == 13:
    rng = random.randrange(1, 101)
    if rng <= 93:
        ophit()
    else:
        print("Opponent is standing.")
elif opscore == 14:
    rng = random.randrange(1, 101)
    if rng <= 85:
        ophit()
    else:
        print("Opponent is standing.")
elif opscore == 15:
    rng = random.randrange(1, 101)
    if rng <= 75:
        ophit()
    else:
        print("Opponent is standing.")
elif opscore == 16:
    rng = random.randrange(1, 101)
    if rng <= 60:
        ophit()
    else:
        print("Opponent is standing.")
elif opscore == 17:
    rng = random.randrange(1, 101)
    if rng <= 38:
        ophit()
    else:
        print("Opponent is standing.")
elif opscore == 18:
    rng = random.randrange(1, 101)
    if rng <= 10:
        ophit()
    else:
        print("Opponent is standing.")
elif opscore == 19:
    rng = random.randrange(1, 101)
    if rng <= 6:
        ophit()
    else:
        print("Opponent is standing.")
elif opscore == 20:
    rng = random.randrange(1, 1001)
    if rng <= 5:
        ophit()
    else:
        print("Opponent is standing.")
else:
    print("Opponent is standing.")

opcardslabel.config(text="Opponent's cards: [" + str(opcards[0]) + ",?,???]")


# newcard Function
def newcard():
    global score
    card = random.randrange(1, 12)
    if card == 1:
        yougota.config(text="You got an Ace!")
        cardlist.append("A")
        if score + 11 > 21:
            score = score + 1
        else:
            score = score + 11
    elif card == 8:
        yougota.config(text="You got an 8!")
        cardlist.append("8")
        score = score + card
    elif card <= 10:
        yougota.config(text="You got a " + str(card) + "!")
        cardlist.append(str(card))
        score = score + card
    else:
        jqk = random.randrange(1, 4)
        if jqk == 1:
            yougota.config(text="You got a Jack!")
            cardlist.append("J")
        elif jqk == 2:
            yougota.config(text="You got a Queen!")
            cardlist.append("Q")
        else:
            yougota.config(text="You got a King!")
            cardlist.append("K")
        score = score + 10
    if score > 21:
        bust.config(text="You busted! 💀")
    elif score == 21:
        bust.config(text="You win!!")
    scoretext.config(text="Score: " + str(score))
    cards.config(text="Cards: " + str(cardlist))


def stand():
    if opscore > score:
        if opscore > 21:
            bust.config(text='You Win, Opponent busted!')
        else:
            bust.config(text='You Lose!')
    elif opscore == score:
        bust.config(text='Draw.')
    else:
        bust.config(text='You Win!!')
    opcardslabel.config(text="Opponent's cards: " + str(opcards))


ttk.Button(window, text="Hit!", command=newcard).pack()
ttk.Button(window, text="Stand.", command=stand).pack()
scoretext.pack()
yougota.pack()
cards.pack()
opcardslabel.pack()
lineskip1.pack()
bust.pack()
tk.mainloop()
