sys = ['🍇', '🍉', '🍒', '🍌', '🥥', '🫐', '🍐', '🥭', '🎱', '💎']

combs = "{"

#FOAK
for s in sys:
	combs+= f"'{s*4}' winnings[2], "

#TOAK	
for s in sys:
	combs+= f"'{s*3}' : winnings[4], "

#DOUBLE PAIR
for s in sys:
	for x in sys:
		if s != x:
			combs+= f"'{s*2}{x*2}' : winnings[3], "
	
combs = combs[:-2] + "}"
print(combs)
__import__("pyperclip").copy(combs)