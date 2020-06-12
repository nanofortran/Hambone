###################################################
# FILE: ModuleController.py                       #
# AUTHOR: NotPike                                 #
# Function: Helper function for module selection. #
#           PIN comes in, function is ran if it   #
#           matches something in select().        #
###################################################

## Move back to root directory
import sys
sys.path.append("..")

### IMPORT MODULES ###
from modules.Audio import *

audio = Audio()

class ModuleController:

    def __init__(self):
        return

    def select(self, pin):
        if(pin == "123"):
            print("Test PIN")                    #Test
            return True

        elif(pin == "321"):
            audio.playWav("/wav/StarWars3.wav")  #Audio File
            return True

        else:
            return False                         # Invalid PIN return False        