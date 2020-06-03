import sys
from termcolor import cprint
from colorama import init
from pyfiglet import figlet_format
import pyperclip


def mechanics():
    cprint(figlet_format('Mechanics', font='small'), 'blue', attrs=['bold', 'blink'])
    cprint('==============================================', 'white', attrs=['blink'])
    cprint('Scientific Calculator v.0.0.0', 'blue', attrs=['bold'])
    cprint('==============================================', 'white', attrs=['blink'])
    print()
    cprint('To return to the main page, type "R" into INPUT', 'blue')
    print()
    cprint('Equation Selection', 'red')
    cprint('Force and Acceleration[0]\nLinear Motion with Constant Acceleration[1]\nConservation of Momentum[2]\n'
           'Energy and Work[3]\nGravitation[4]\nForces and Materials[5]')


def main():
    mechanics()
    print()
    cprint('INPUT: ', 'red')

    selection = input(' ')
    if selection == '0':
        fma()

    if selection == '1':
        lmwca()

    elif selection == 'R' or 'r':
        import main__calc


def fma():
    cprint("Find (F)orce, (M)ass or (A)cceleration", 'blue')
    cprint('==============================================', 'white', attrs=['blink'])
    cprint('Or (R)eturn', 'red')
    ans1 = input()

    # solve for Force
    if ans1 == 'f':
        print("Enter mass:")
        m = input()
        print("Enter acceleration:")
        a = input()
        print("Therefore Force = ")
        print(int(m) / int(a))
        print("N")
        cprint('"f" to finish', 'red')
        fin = input()
        if fin == 'f':
            return main()

    # solve for Mass
    elif ans1 == 'm':
        print("Enter force:")
        f = input()
        print("Enter acceleration::")
        a = input()
        print("Therefore Mass = ")
        print(int(f) / int(a))
        print("Kg")
        cprint('"f" to finish', 'red')
        fin = input()
        if fin == 'f':
            return main()

    # solve for Acceleration
    elif ans1 == 'a':
        print("Enter force:")
        f = input()
        print("Enter mass:")
        m = input()
        print("Therefore Acceleration = ")
        print(int(f) / int(m))
        print("m/s/s")
        cprint('"f" to finish', 'red')
        fin = input()
        if fin == 'f':
            return main()

    # return
    elif ans1 == 'R' or 'r':
        main()


def lmwca():
    cprint('Choose your Equation', 'blue')
    cprint('==============================================', 'white', attrs=['blink'])
    cprint('v=u+at [0]\ns=ut+1/2at^2 [1]\nv^2=u^2+2as [2]\ns=(u+v/2)t [3]', 'red')
    cprint('==============================================', 'white', attrs=['blink'])
    cprint('INPUT: ', 'red')
    equation = input('  ')

    if equation == '0':
        cprint('v=u+at', 'blue')
        cprint('==============================================', 'white', attrs=['blink'])
        cprint('Find:', 'red')
        cprint('Final velocity [v]', 'blue')
        cprint('Initial velocity [u]', 'blue')
        cprint('Acceleration [a]', 'blue')
        cprint('Time [t]', 'blue')
        cprint('Or (R)eturn', 'red')
        ans2 = input()

        # solve for final velocity
        if ans2 == 'v':
            print('Enter Initial velocity[u]')
            u = input()
            print('Enter Acceleration [a]')
            a = input()
            print('Enter Time [t]')
            t = input()
            print('Therefore Final Velocity = ')
            cprint(int(u) + int(a) * int(t), 'red')
            cprint('m/s', 'blue')

        # solve for initial velocity
        elif ans2 == 'u':
            print('Enter Final velocity[v]')
            v = input()
            print('Enter Acceleration [a]')
            a = input()
            print('Enter Time [t]')
            t = input()
            print('Therefore Initial Velocity = ')
            cprint(int(v) - int(a) * int(t), 'red')
            cprint('m/s', 'blue')


main()


