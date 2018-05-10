#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""include filer and composenter"""
import marvin
import marvintwo
import config
import sys
import getopt

def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        marvin.menu()
        choice = input("--> ")


        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return

        elif choice == "1":
            marvin.myNameIs()

        elif choice == "2":
            marvin.old()

        elif choice == "3":
            marvin.tingd()

        elif choice == "4":
            marvin.minute()

        elif choice == "5":
            marvin.weather()

        elif choice == "6":
            marvin.word()

        elif choice == "7":
            marvin.slumpmassiga()

        elif choice == "8":
            marvin.summaMedel()

        elif choice == "9":
            marvin.cirkel()

        elif choice == "10":
            marvin.hypotenuse()
        elif choice == "11":
            marvin.betyg()
        elif choice == "12":
            marvin.guessa()
        elif choice == "13":
            marvin.timeNow()
        elif choice == "14":
            marvin.kasta()

        elif choice == "15":
            marvin.ask()

        elif choice == "16":
            marvintwo.filanalys()


        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")


"""Kommando för ryggsäcken"""

def usage():
    """prints usage"""
    print("\n")
    print("-h, --h                   display helptext")
    print("inv                       Visa vad som finns i inventoryt")
    print("inv pick flower           Visa vad som finns i inventoryt")
    print("inv drop flower           Visa vad som finns i inventoryt")



try:
    opts, args = getopt.getopt(sys.argv[1:], 't:h', ['test=', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-h", "--help"):
        usage()
        sys.exit(2)
    else:
        usage()
        sys.exit(2)

if len(args) == 1:
    if args[0] == 'inv':
        config.readinfo()
        sys.exit(2)
    else:
        usage()
        sys.exit(2)
if len(args) == 2:
    if args[0] == 'inv' and args[1] == 'drop':
        files = 'inv.data'
        config.dropAll(files)
        sys.exit(2)
    else:
        usage()
        sys.exit(2)
if len(args) == 3:
    if args[0] == 'inv' and args[1] == 'pick':
        pickflower = args[2]
        config.pick(pickflower)
        sys.exit(2)

    if args[0] == 'inv' and args[1] == 'drop':
        dropflower = args[2]
        config.drop(dropflower)
        sys.exit(2)

    else:
        usage()
        sys.exit(2)



if __name__ == "__main__":
    main()
