import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Titlebar

layout = [[sg.Text('Välkommen till illenbockens bank')], [sg.Button('Gå vidare till banken')],]

window = sg.Window('illenbockens bank', layout, margins=(500,300))

while True:
    event, values = window.read()
    if event == 'Gå vidare till banken' or event == sg.WIN_CLOSED:
        break

window.close()

from functions import *
from datetime import datetime
import os


move_transactions()
move_dates()
    
# Programloopen
while True:

    # Skriver ut menyn och frågar användar efter sitt val
    meny = ("\n############################"
    "\n#                          #"
    "\n#    illenbockens bank     #"
    f"\n#       Saldo: {balance()}kr    #"
    "\n#                          #"
    "\n############################"
    "\n "

    "\n   1: Visa transaktioner."
    "\n   2: Sätt in pengar."
    "\n   3: Ta ut pengar."
    "\n   4: Nollställ kontot"
    "\n   5: Avsluta applikationen."
    "\n   Gör ditt val (1-5):")


    val = validate_int(meny, "Felaktig inmatning! Gör om gör rätt.")            # Kollar om valet är ett giltigt svar


    if val == 1:            # Visa transaktionslistan
        print_transactions()


    elif val == 2:          # Sätta in pengar
        insättning = validate_float("Hur mycket pengar vill du sätta in (kr)?","Felaktig inmatning! Gör om gör rätt.")

        insättning = round(insättning,2)         # Avrundar talet till 2 decimaler

        if insättning > 0:
            add_transaction(insättning, True)
            datum2 = datetime.now()
            datum3 = datum2.strftime("%d/%m/%Y")
            add_date(datum3)
        else:
             print("insättningen kan inte vara negativ.")
    

    elif val == 3:          # Ta ut pengar
        uttag = validate_float("Hur mycket pengar vill du ta ut (kr)?", "Felaktig inmatning! Gör om gör rätt.")

        uttag = round(uttag,2)          # Avrundar talet till 2 decimaler

        if uttag > balance():
            print(f"Du kan inte ta ut mer än {balance()}kr just nu.")
        elif uttag < 0:
            print("uttaget kan inte vara negativt.")
        else:
            add_transaction(-uttag, True)
            datum1 = datetime.now()
            datum = datum1.strftime("%d/%m/%Y")
            add_date(datum)


    elif val == 4:          # Nollställa kontot
        nollställ= str(input("Är du säker detta nollställer hela kontot?\n1. Ja\n2. Nej\nVälj (1-2):"))
        if nollställ == '1':
            os.remove(filename)
            os.remove(filename2)
            transaktioner.clear()
            datumlista.clear()
            move_transactions()
            move_dates()
        else:
            continue


    elif val == 5:          # Avslutar programmet
        break

write_dates_to_file()