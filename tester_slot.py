import secrets
import sys
import string

sys.set_int_max_str_digits(0)

sys = ['🍇', '🍉', '🍒', '🍌', '🥥', '🫐', '🍐', '🥭', '🎱', '💎']

winnings = [500, 250, 100, 50, 20]

winning_combs = {
    '💎💎💎💎' : winnings[0],
    
    '🎱🎱💎💎' : winnings[1] , '💎💎🎱🎱' : winnings[1],
    
    '🍇🍇🍇🍇' : winnings[2], '🍉🍉🍉🍉' : winnings[2], '🍒🍒🍒🍒' : winnings[2], '🍌🍌🍌🍌' : winnings[2], '🥥🥥🥥🥥' : winnings[2], '🫐🫐🫐🫐' : winnings[2], '🍐🍐🍐🍐' : winnings[2], '🥭🥭🥭🥭' : winnings[2], '🎱🎱🎱🎱' : winnings[2], 
    
    '🍇🍇🍉🍉' : winnings[3], ' 🍇🍇🍒🍒' : winnings[3], '🍇🍇🍌🍌' : winnings[3], '🍇🍇🥥🥥' : winnings[3], '🍇🍇🫐🫐' : winnings[3], '🍇🍇🍐🍐' : winnings[3], '🍇🍇🥭🥭' : winnings[3], '🍇🍇🎱🎱' : winnings[3], ' 🍇🍇💎💎' : winnings[3], '🍉🍉🍇🍇' : winnings[3], '🍉🍉🍒🍒' : winnings[3], '🍉🍉🍌🍌' : winnings[3], '🍉🍉🥥🥥' : winnings[3], '🍉🍉🫐🫐' : winnings[3], '🍉🍉🍐🍐' : winnings[3], ' 🍉🍉🥭🥭' : winnings[3], '🍉🍉🎱🎱' : winnings[3], '🍉🍉💎💎' : winnings[3], '🍒🍒🍇🍇' : winnings[3], '🍒🍒🍉🍉' : winnings[3], '🍒🍒🍌🍌' : winnings[3], '🍒🍒🥥🥥' : winnings[3], ' 🍒🍒🫐🫐' : winnings[3], '🍒🍒🍐🍐' : winnings[3], '🍒🍒🥭🥭' : winnings[3], '🍒🍒🎱🎱' : winnings[3], '🍒🍒💎💎' : winnings[3], '🍌🍌🍇🍇' : winnings[3], '🍌🍌🍉🍉' : winnings[3], ' 🍌🍌🍒🍒' : winnings[3], '🍌🍌🥥🥥' : winnings[3], '🍌🍌🫐🫐' : winnings[3], '🍌🍌🍐🍐' : winnings[3], '🍌🍌🥭🥭' : winnings[3], '🍌🍌🎱🎱' : winnings[3], '🍌🍌💎💎' : winnings[3], ' 🥥🥥🍇🍇' : winnings[3], '🥥🥥🍉🍉' : winnings[3], '🥥🥥🍒🍒' : winnings[3], '🥥🥥🍌🍌' : winnings[3], '🥥🥥🫐🫐' : winnings[3], '🥥🥥🍐🍐' : winnings[3], '🥥🥥🥭🥭' : winnings[3], ' 🥥🥥🎱🎱' : winnings[3], '🥥🥥💎💎' : winnings[3], '🫐🫐🍇🍇' : winnings[3], '🫐🫐🍉🍉' : winnings[3], '🫐🫐🍒🍒' : winnings[3], '🫐🫐🍌🍌' : winnings[3], '🫐🫐🥥🥥' : winnings[3], ' 🫐🫐🍐🍐' : winnings[3], '🫐🫐🥭🥭' : winnings[3], '🫐🫐🎱🎱' : winnings[3], '🫐🫐💎💎' : winnings[3], '🍐🍐🍇🍇' : winnings[3], '🍐🍐🍉🍉' : winnings[3], '🍐🍐🍒🍒' : winnings[3], ' 🍐🍐🍌🍌' : winnings[3], '🍐🍐🥥🥥' : winnings[3], '🍐🍐🫐🫐' : winnings[3], '🍐🍐🥭🥭' : winnings[3], '🍐🍐🎱🎱' : winnings[3], '🍐🍐💎💎' : winnings[3], '🥭🥭🍇🍇' : winnings[3], ' 🥭🥭🍉🍉' : winnings[3], '🥭🥭🍒🍒' : winnings[3], '🥭🥭🍌🍌' : winnings[3], '🥭🥭🥥🥥' : winnings[3], '🥭🥭🫐🫐' : winnings[3], '🥭🥭🍐🍐' : winnings[3], '🥭🥭🎱🎱' : winnings[3], ' 🥭🥭💎💎' : winnings[3], '🎱🎱🍇🍇' : winnings[3], '🎱🎱🍉🍉' : winnings[3], '🎱🎱🍒🍒' : winnings[3], '🎱🎱🍌🍌' : winnings[3], '🎱🎱🥥🥥' : winnings[3], '🎱🎱🫐🫐' : winnings[3], ' 🎱🎱🍐🍐' : winnings[3], '🎱🎱🥭🥭' : winnings[3], '🎱🎱💎💎' : winnings[3], '💎💎🍇🍇' : winnings[3], '💎💎🍉🍉' : winnings[3], '💎💎🍒🍒' : winnings[3], '💎💎🍌🍌' : winnings[3], ' 💎💎🥥🥥' : winnings[3], '💎💎🫐🫐' : winnings[3], '💎💎🍐🍐' : winnings[3], '💎💎🥭🥭' : winnings[3], '💎💎🎱🎱' : winnings[3],

    '🍇🍇🍇' : winnings[4], '🍉🍉🍉' : winnings[4], '🍒🍒🍒' : winnings[4], '🍌🍌🍌' : winnings[4], '🥥🥥🥥' : winnings[4], '🫐🫐🫐' : winnings[4], '🍐🍐🍐' : winnings[4], '🥭🥭🥭' : winnings[4], '🎱🎱🎱' : winnings[4], '💎💎💎' : winnings[4]
}

def play():
    gen = ""

    for _ in range(4):
        gen+= sys[int(secrets.choice(string.digits))]

    return gen

def betterNumbers(number):
    number = str(number)[::-1]
    n = ""

    for x in range(len(number)):
        n+= "_" if x%3 == 0 and x!=0 else ""
        
        n+= number[x]
        
    return n[::-1]

INITIAL = 50_000
SPIN = 10**4

amount = INITIAL

rtp = 0

totalWinning = 0
totalLose = 0

bk = False

CYCLES = 1000

for _ in range(CYCLES):
    if(bk):
        break

    print(f"Cycle {_+1}\n")
    

    amount = INITIAL
    

    for _ in range(SPIN): #slot reels
        bet = secrets.choice([0.10, 0.20, 0.50, 1, 2, 5, 10])
        
        if(amount < 0):
            bk=True
            break
       

        amount+= bet
        totalLose+= bet

        g = play()

        for comb in winning_combs.keys():
            if comb in g:

                WIN = winning_combs[comb] * bet

                amount-= WIN
                totalWinning += WIN 

print(f"\nProfit => {betterNumbers(round(totalLose - totalWinning))} € -> (substract INITIAL: {betterNumbers(INITIAL)})")

print(f"\nWins => {betterNumbers(round(totalWinning))} €")
print(f"\nLoses => {betterNumbers(round(totalLose))} €")

print(f"\n\nBankRupt: {bk}")

print(f"\n\nRTP (Return To Player) => {round(totalWinning / totalLose, 4) * 100} %")