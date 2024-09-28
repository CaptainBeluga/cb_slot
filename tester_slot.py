from slot import *

SPIN = 140_000
CYCLES = 5

amount = slotMachine

bk = False

rtps=[]

for _ in range(CYCLES):
    rtp = 0

    totalWinning = 0
    totalBets = 0

    if(bk):
        break

    print(f"Cycle {_+1}\n")
    

    amount = slotMachine
    

    for _ in range(SPIN):
        bet = give_bet()
        
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
        raise Exception

    rtps.append(rtp)
        

print(f"\nProfit => {betterNumbers(round(totalBets - totalWinning))} €")

print(f"\nWins => {betterNumbers(round(totalWinning))} €")
print(f"\nLoses => {betterNumbers(round(totalBets))} €")

print(f"\n\nBankRupt: {bk}")

print(f"\n\nAvarage RTP (Return To Player) => {round(sum(rtps) / len(rtps),2)} %\n\nMIN RTP: {min(rtps)} %\nMAX RTP: {max(rtps)} %")