# Watson Computational Scientific Calculator
import sys
from termcolor import cprint
from colorama import init
from pyfiglet import figlet_format
import pyperclip

cprint(figlet_format('Watson Compute', font='small'), 'blue', attrs=['bold', 'blink'])
cprint('==============================================', 'white', attrs=['blink'])
cprint('Scientific Calculator v.0.0.0', 'blue', attrs=['bold'])
cprint('==============================================', 'white', attrs=['blink'])
print()
cprint('System Selection', 'red')
cprint('Basic[0]\nMechanics[1]\nLength and Area[2]\nSurface Area and Volume[3]\nArea Approximations[4]\n'
       'Trigonometry[5]\nGeometry[6]\nCo-ordinate Geometry[7]\nAlgebra[8]\nLogarithms[9]\nSeries and Sequences[10]\n'
       'Geometric Optics[11]\nLight and Sound[12]\nFinance[13]')
print()
cprint('INPUT: ', 'red')
selection = input(' ')

if selection == '0':
    import bsc_calc
if selection == '1':
    import mechanics
if selection == '2':
    import lengtharea
if selection == '3':
    import surfarea_vol
if selection == '4':
    import area_aprx
if selection == '5':
    import trig
if selection == '6':
    import geometry
if selection == '7':
    import coord_calc
if selection == '8':
    import algebra
if selection == '9':
    import logs
if selection == '10':
    import series_seq
if selection == '11':
    import optics
if selection == '12':
    import light_sound
if selection == '13':
    import finance
