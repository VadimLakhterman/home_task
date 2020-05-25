#!/usr/bin/env python3

# File Name:    test.py
# Created by:   Vadim Lakhterman
# Date:         24.5.20
# Last Update:  25.5.20

import Controller
from Controller import *

FILE_NAME = ''
expretions = { '5D00008000': 'lzma',
  '27051956': 'uImage',
  '1F8B0800': 'gzip',
  '303730373031': 'cpio',
  '303730373032': 'cpio',
  '303730373033': 'cpio',
  '894C5A4F000D0A1A0A': 'lzo',
  '5D00000004': 'lzma',
  'FD377A585A00': 'xz',
  '314159265359': 'bzip2',
  '425A6839314159265359': 'bzip2',
  '04224D18': 'lz4',
  '02214C18': 'lz4',
  '1F9E08': 'gzip',
  '71736873': 'squashfs',
  '68737173': 'squashfs',
  '51434454': 'dtb',
  'D00DFEED': 'fit',
  '7F454C46': 'elf'
   }


def run_selection(controller, selection):
    global FILE_NAME

    if selection == 1:
        print("Running test")
        controller.find_zero_leading(FILE_NAME)
        print("Test finished")
        print("--------------------------------------------------")
        print()
        return False
    elif selection == 2:
        print("Running test")
        controller.find_expressions(FILE_NAME, expretions)
        print("Test finished")
        print("--------------------------------------------------")
        print()
        return False
    elif selection == 3:
        print(expretions.values())
        print("Which expression would you like to find?")
        name = input()
        print("Running test")
        controller.find_expressions(FILE_NAME, expretions, name)
        print("Test finished")
        print("--------------------------------------------------")
        print()
        return False
    elif selection == 4:
        print("Running test")
        controller.find_zero_leading("wrong_name")
        print("Test finished")
        print("--------------------------------------------------")
        print()
        return False
    elif selection == 5:
        print("Running test")
        controller.find_expressions(FILE_NAME, expretions, "test")
        print("Test finished")
        print("--------------------------------------------------")
        print()
        return False
    elif selection == 9:
        print("Please enter file name for test: ")
        FILE_NAME = input()
        return False
    elif selection == 0:
        controller.finish()
        return True
    else:
        print("Wrong selection, try again!")
        return False


def main():
    global FILE_NAME
    print("Please enter file name for test: ")
    FILE_NAME = input()
    exit = False
    controller = Controller()

    while not exit:
        print("Which test would you like to run?")
        print("Press 1 for find zero leading sequences")
        print("Press 2 for find all expressions in file from map")
        print("Press 3 for find single expression from map")
        print("Press 4 to test wrong file name")
        print("Press 5 to test wrong name")
        print("Press 9 to change file name")
        print("Press 0 for exit")

        try:
            selection = int(input())
            exit = run_selection(controller, selection)
        except Exception:
            print("Wrong input, use integer numbers only!")

    
if __name__ == "__main__":
    main()