#Modules.py
import os

def printStartupMSG():
    print("""This is an example of generation loss which is a
phenomenon in digital media where each time a file is
copied or saved,its quality decreases due to data
compression and loss of information.\n""")

def printBeforeInit():
    print('ATTENTION: IMAGE SHOULD ONLY BE A .jpeg TYPE')
    print('ATTENTION: NO NEED TO INCLUDE THE .JPEG EXTENSION')
    print('ATTENTION: IMAGE !!IN!! THE FOLDER IMAGE_DIRECTORY\n')
    
def printTotalSize(GenMax, GenCn):
    aboutTotalSize = 10^6 #~Bytes
    aboutTotalSizeB = aboutTotalSize *(GenMax*(GenCn + 2))
    aboutTotalSizeMB = ((aboutTotalSizeB *(GenMax*(GenCn))/ 1024)) / 8 #~MBytes
    aboutTotalSizeGB = aboutTotalSizeMB / 1024 #~GBytes 
    
    print(F"""\n
TOTAL GENERATIONS: {GenMax*GenCn}
TOTAL GENERATION SIZE MB: {aboutTotalSizeMB} 
TOTAL GENERATION SIZE GB: {aboutTotalSizeGB} """)

def printAdditionalOptions():
    print(f"""\n
[1] Delete Raw Files.
[2] Delete Exported Files.
[3] Exit Program""")

def printImageDirectory():
    print('Images in [ ./Image_Directory/ ]:\n')
    print('\n'.join(os.listdir('Image_Directory/')))
    print()
