# Watson Computational Scientific Calculator
# basic calculator

import sys
from termcolor import cprint
from colorama import init
from pyfiglet import figlet_format


def main():
    cprint(figlet_format('BASIC', font='small'), 'blue', attrs=['bold', 'blink'])
    cprint('==============================================', 'white', attrs=['blink'])
    cprint('Scientific Calculator v.0.0.0', 'blue', attrs=['bold'])
    cprint('==============================================', 'white', attrs=['blink'])
    print()
    cprint('Operators supported; +, -, *, /', 'red', attrs=['bold'])
    print()

    num1 = input('INPUT 1:\n')
    operator = input('Operator:')
    num2 = input('INPUT 2:\n')

    num1 = float(num1)
    num2 = float(num2)

    out = None

    if operator == "+":
            out = num1 + num2
    elif operator == "-":
            out = num1 - num2
    elif operator == "*":
            out = num1 * num2
    elif operator == "/":
            out = num1 / num2

    cprint('Answer: ' + str(out), 'red', attrs=['bold'])
    print()
    cprint('To return to BASIC, type "f"', 'red')
    fin = input(' ')

    if fin == 'f' or 'F':
        main()



main()
