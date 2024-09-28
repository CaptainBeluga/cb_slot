import secrets
import time
import sys

MOJITO_PASS = 500

slotMachine = 50_000

bets = [0.10, 0.20, 0.50, 1, 2, 5, 10]


symbols = ['🍇', '🍉', '🍒', '🍌', '🥥', '🫐', '🍐', '🥭', '🎱', '💎']

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
        gen+= secrets.choice(symbols)

    return gen

def slowprint(s, c):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 30)


def betterNumbers(number):
    number = str(number)[::-1]
    n = ""

    for x in range(len(number)):
        n+= "_" if x%3 == 0 and x!=0 else ""
        
        n+= number[x]
        
    return n[::-1]


def give_bet():
    return secrets.choice(bets)