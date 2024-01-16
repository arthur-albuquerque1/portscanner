from visual import visual
from calc import calc


#User interface
visual.banner()

#Mode selector
print('Mode 0: Calculate your notes')
print('Mode 1: Exit')
mode = int(input('Select the mode: '))

#Main 
if mode == 0:
    calc.calculate()
elif mode == 1:
    exit()
