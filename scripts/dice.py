import random
from termcolor import colored, cprint #pip istall termcolor
import os
def roll():
    return((random.choice(dice)))
def clear():
    os.system('clear')
def color(text,color):
    return(colored(text,color))
def reset():
    total_file.seek(0)
dice = [1,2,3,4,5,6]
total_file = open("points.txt","r+")
rolls = ['You rolled an ',"Rooooooolled a ", 'ROLL THAT ', 'got a digit, ']

reset()
if total_file.read() == "":
    total_file.write("0")
while(True):
    reset()
    d = int(roll())
    total = int(total_file.read())
    total1 = sum([total,d])
    reset()
    total_file.write(str(total1))
    clear()
    reset()
    print(color(random.choice(rolls), "red") + color(str(d),'light_blue') + color("\ntotal rolled ",'red') + color(total_file.read(),'light_blue'))
    input()
