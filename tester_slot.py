import secrets
import sys
import string

sys.set_int_max_str_digits(0)

sys = ['🍇', '🍉', '🍒', '🍌', '🥥', '🫐', '🍐', '🥭', '🎱', '💎']

winnings = [350, 150, 100, 50, 20]

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
SPIN = 200_000

amount = INITIAL

bk = False

CYCLES = 50

rtps=[]

for _ in range(CYCLES):
    rtp = 0

    totalWinning = 0
    totalBets = 0

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
        totalBets+=bet
        
        g = play()

        for comb in winning_combs.keys():
            if comb in g:

                WIN = winning_combs[comb] * bet

                amount-= WIN
                totalWinning += WIN

                break


    rtp = round(totalWinning / totalBets, 4) * 100

    if(rtp > 97):
        print("RTP TOO HIGH !")
        int("b")

    rtps.append(rtp)
        

print(f"\nProfit => {betterNumbers(round(totalBets - totalWinning))} € -> (substract INITIAL: {betterNumbers(INITIAL)})")

print(f"\nWins => {betterNumbers(round(totalWinning))} €")
print(f"\nLoses => {betterNumbers(round(totalBets))} €")

print(f"\n\nBankRupt: {bk}")

print(f"\n\nAvarage RTP (Return To Player) => {sum(rtps) / len(rtps)} %\n\nMIN RTP: {min(rtps)} %\nMAX RTP: {max(rtps)} %")