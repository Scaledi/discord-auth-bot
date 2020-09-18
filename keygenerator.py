# region: Imports
import os
import re
import random
import string
# endregion
# region Number of keys to generate
keynumCorrect = False
while keynumCorrect == False:
    keynum = input("How many keys do you want to generate?: ")
    try: 
        int(keynum) 
    except: 
        #is not int
        print("Hmm, thats not right!")
    else:
        # is a int
        keynum = int(keynum)
        keynumCorrect = True
# endregion
# region: Overwrite file?
ovrCorrect = False
while ovrCorrect == False:
    ovrwrite = input("""Do you wish to overwrite the file? (Please Write "Yes" Or "No"): """)
    if (re.search(r'(Yes|1)', ovrwrite, re.IGNORECASE)):
        ovrwrite = True
        ovrCorrect = True
        keytxt = open("keys.txt","w")
    elif (re.search(r'(No|2)', ovrwrite, re.IGNORECASE)):
        ovrwrite = False
        ovrCorrect = True
        keytxt = open("keys.txt","a")
    else:
        print("Hmm, did'ent quite get that. lets try again!")
print("""great! we got all that. we will make changes inside a file in the same folder as this program. the file will be named "keys.txt"! for next steps, refer to "INSTRUCTIONS.md".""")
# endregion
# region: Output to file
def getrndstr(length):
    letters_and_digits = string.ascii_uppercase + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    keytxt.write(result_str + "\n")

while keynum > 0:
    getrndstr(int(6))
    keynum = keynum - 1
# endregion