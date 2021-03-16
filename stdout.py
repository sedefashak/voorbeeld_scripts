#!/usr/bin/python3

import sys

if sys.stdin.isatty(): # the isatty method checks if input is from a terminal
    print('Interactively reading data')
    print('Press ^D (ctrl-d) to end input')

if sys.stdout.isatty():
    print('''Don't forget to reboot after installation''')

data = sys.stdin.readlines() # list of lines of text
data.reverse() # reverse the order of the lines
sys.stdout.writelines(data)
