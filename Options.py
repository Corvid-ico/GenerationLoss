#OptionMenu.py
from os import system
from Moduloso.Printer import *
def OptionMenuUI():
    printAdditionalOptions()
    Option = int(input('Option:'))
    if (Option == 1):
        system('del Exported\Raw_Generations')
        return True
    elif (Option == 2):
        system('del Exported\Indp_Generations')
        return True
    else:
        return False