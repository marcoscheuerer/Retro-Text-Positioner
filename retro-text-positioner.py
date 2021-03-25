#!/bin/python3
import random
from my_art import *
from my_color import *

################################################################################
# Global Variables, Dictionaries, Lists, etc.                                  #
################################################################################
# letter: art_letter
dictionary = {
    "A": A, "B": B, "C": C, "D": D, "E": E,
    "F": F, "G": G, "H": H, "I": I, "J": J,
    "K": K, "L": L, "M": M, "N": N, "O": O,
    "P": P, "Q": Q, "R": R, "S": S, "T": T,
    "U": U, "V": V, "W": W, "X": X, "Y": Y,
    "Z": Z, " ": EMPTY, "!": EXMARK, ",": COMMA,
    ".": DOT, "-": DASH
}

colors = {
    "RED": RED, "GREEN": GREEN, "BLUE": BLUE, 
    "YELLOW": YELLOW, "MAGENTA": MAGENTA,
    "CYAN": CYAN, "BLACK": BLACK, "WHITE": WHITE,
    "DEFAULT": DEFAULT
}

color_list = [ "RED", "GREEN", "BLUE", "YELLOW", "MAGENTA",
             "CYAN", "BLACK", "WHITE" ]

################################################################################
# Definition of Functions                                                      #
################################################################################
def clear():
    print(f"\x1b[2J\x1b[H")

def list_len_of_lines(letter, row=0):
    i = 0
    len_of_lines = []

    for element in dictionary[letter]:
        if element == '\n':
            len_of_lines.append(i)
            i = 0
        else:
            i += 1
    return len_of_lines

def setpos(x, y, letter, color):
    count = 0
    row = 0

    color = color.upper()

    if color == "MIXED":
        color = color_list[random.randint(0,7)]

    art_letter = dictionary[letter]
    art_color = colors[color]
    for element in art_letter:
        if element == '\n':
            row += 1
            count = 0
        x2 = x + row
        y2 = y + count
        print(f"\x1b[{x2};{y2}H{art_color}{element}{DEFAULT}", end="")
        count += 1

def settext(xpos, ypos, text, color):
    space = 1
    further_pos = 0
    x = int(xpos)
    y = int(ypos)
    for letter in text.upper():
        setpos(x, y + further_pos, letter, color)
        max_length = max(list_len_of_lines(letter))
        further_pos += (max_length + space)

###############################################################################
# Main Program                                                                #
###############################################################################
isFinish = False
while not isFinish:
    choice = ""

    clear()

    print("Funny Retro-Text-Positioner\n"
          "===========================\n\n")
    text = input(f"Text to print {BLUE}[default: Hello, World!!!]{DEFAULT}: ")
    color = input("Available Colors:\nred, green, blue, yellow, magenta, "
                  "cyan, black, white, mixed\n"
                  f"Please choose a color you like {BLUE}[default: mixed]{DEFAULT}: ")
    xpos = input(f"Row number to print {BLUE}[default: 20]{DEFAULT}: ")
    ypos = input(f"Column number to print {BLUE}[default: 1]{DEFAULT}: ")
    print(color)

    # Default Values
    if color == "":
        color = "mixed"
    if text == "":
        text = "Hello, World!!!"
    if xpos == "":
        xpos = "20"
    if ypos == "":
        ypos = "1"

    settext(xpos, ypos, text, color)
    while not (choice == 'n' or choice == 'y'):
        choice = input("Do you want to write a new text (y/n): ").lower()
        if choice == 'n':
            isFinish = True
        elif choice == 'y':
            isFinish = False

clear()
print("\n\nThanks for getting retro, after so many years!")
