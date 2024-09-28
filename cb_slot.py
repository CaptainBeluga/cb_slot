from slot import *

#BANKROLL
player = 1_000

bet = bets[0] #default (smaller bet)

totalWinning = 0
totalLose = 0

print("\n*** CB SLOT ***\n\n")

#gui soon
while True:
    print("1. PLAY\n2. BET CHANGE\n3. BALANCE\n4. PAYOUT TABLE\n5. LOAD MORE")

    try:
        c = int(input("\nChoose => "))
    except ValueError:
        c = 1
    
    except KeyboardInterrupt:
        slowprint("\nThanks for playing, CaptainBeluga bless you !")

    if c==1:
        if(player-bet >= 0):
            player-= bet
            slotMachine+= bet

            totalLose+= bet

            
            g = play()

            msg = "["

            for s in g:
                msg += f"  {s}  |"

            msg= msg[:-1] + "]"

            for comb in winning_combs.keys():
                
                if comb in g:
                    WIN = winning_combs[comb] * bet

                    slotMachine-= WIN
                    player += WIN

                    totalWinning+= WIN

                    msg+= f" !!!!! YOU WIN: {WIN} € !!!!!"
                    msg+= " ---> 🍹🍹🍹 FREE MOJITO PASS (só-le bar) 🍹🍹🍹" if WIN>=MOJITO_PASS else ""

                    break


            slowprint(f"\n\n{msg}", 0.5)
        else:
            print("Sei proprio rimasto attaccato alla canna del gas!!! (NOT_ENOUGH_MONEY_TO_BET)")
    
    if c==2:
        print(f"\nCurrent Bet: {bet} €\n")
        newBet = float(input("New BET => "))

        if(newBet in bets):
            bet = newBet
            print("\nBet Successfully Updated !")
        
        else:
            print("\nBet Invalid !")

    if c==3:
        print(f"\nYour Balance: {round(player,2)} €\n\nDEV SLOT: {round(slotMachine,2)} €\n\nRTP: {round(totalWinning / totalLose, 4) * 100} %")

    
    if c==4:
        print(f"\n* PAYOUT TABLE *\n\nCurrent Bet: {bet} €\n\n1. JACKPOT 💎💎💎💎 => {winnings[0] * bet} €\n\n2. MINI JACKPOT 💎💎🎱🎱 | 🎱🎱💎💎 => {winnings[1] * bet} €\n\n3. FOUR OF A KIND (FOAK) 🍇🍇🍇🍇 => {winnings[2] * bet} €\n\n4. DOUBLE PAIR 🍇🍇🍉🍉 | 🍉🍉🍇🍇 => {winnings[3] * bet} €\n\n5. THREE OF A KIND (TOAK) 🥥🍇🍇🍇 | 🍇🍇🍇🥥 => {winnings[4] * bet} €")


    if c==5:
        player+= float(input("Money to Add => "))

    print("\n")