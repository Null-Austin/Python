import random
from termcolor import colored, cprint #pip install termcolor
import os
total_file = open("points.txt","r+")
total_file.seek(0)
if total_file.read() == "":
    total_file.write("0")
total_file.close()
while(True):
    os.system('clear')
    total_file = open("points.txt","r+")
    total_file.seek(0)
    x = random.choice([1,2,3,4,5,6])
    a = total_file.read()
    total_file.seek(0)
    total_file.write(str(sum([int(a),x])))
    total_file.seek(0)
    print(colored(random.choice(["You rolled an "]), "red") + colored(str(random.choice([x])),'light_blue') + colored("\ntotal rolled ", 'red') + colored(total_file.read(),'light_blue'))
    total_file.close()
    input()