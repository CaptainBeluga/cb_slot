from slot import *

combs = "{"

#FOAK
for s in symbols:
	combs+= f"'{s*4}' winnings[2], "

#TOAK	
for s in symbols:
	combs+= f"'{s*3}' : winnings[4], "

#DOUBLE PAIR
for s in symbols:
	for x in symbols:
		if s != x:
			combs+= f"'{s*2}{x*2}' : winnings[3], "
	
combs = combs[:-2] + "}"
print(combs)
__import__("pyperclip").copy(combs)