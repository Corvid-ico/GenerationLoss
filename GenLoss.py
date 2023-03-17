#Globals
#Modules
import os
from PIL import Image
from Moduloso.Printer import *
from Moduloso.Imager import *
from Options import *

if (os.system("cls") == 0):
    os.system('cls');SystemHost = 'Win'
else:
    os.system('clear');SystemHost = 'Lin'

printStartupMSG()
DegreeRotation = 90 

try:
    def doLoop(system):
        while (True):
            print('Enter [Y] for Generarion Loss.')
            print('Enter [N] for other options.\n')
            Option = input('Option: ')

            if (Option.lower() == 'y'):
                printBeforeInit(); printImageDirectory()
                Title = input("Image name: ")
                GenCn = int(input("Gen count: "))
                Gens = (GenCn * (360//DegreeRotation))
    
                StartCreation(Title, GenCn, (360//DegreeRotation), Gens, DegreeRotation)
            elif (Option.lower() == 'n'):
                EXIT = OptionMenuUI()
                if (not EXIT):
                    break
                Option = ' '
        print('Generation Loss Done!')
        exit()
    doLoop(os.system)
except ValueError:
    print('ValueError!! Try again!'); doLoop(os.system)
except KeyboardInterrupt:
    print('Generation Loss Done!')
    exit()