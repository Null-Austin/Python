#a very very very very very very basic Check Book lol!





from os import system
from datetime import date
def clear():
    system('clear') #change to clr if on windows!!!
checkbook = open(r"checkbook.txt","w")#append and read
checkbook.close()
checkbook = open(r"checkbook.txt","a+")#append and read
balance = open(r"balance.txt","w+")#write and read
def remove(text,reason):
    balance.seek(0)
    checking = int(balance.read()) - int(text)
    balance.seek(0)
    checkbook.write("-----\n-" + text + "\nfor: " + reason + "\n" + str(date.today()) + "\n")
    balance.write(str(checking)) 
def add(text,reason):
    balance.seek(0)
    checking = int(balance.read()) + int(text)
    balance.seek(0)
    checkbook.write("-----\n+" + text + "\nfor: " + reason + "\n" + str(date.today()) + "\n")
    balance.write(str(checking)) 
def getcheck():
    checkbook.seek(0)
    return(checkbook.read())
clear()
while(True):
    balance.seek(0)
    if balance.read() == "":
        budget = (input("Whats your current balance?: "))
        balance.write(budget)
        checkbook.write("inital budget: " + str(budget) + "\n")
    balance.seek(0)
    print("Your balance is: "+"$"+balance.read())
    inputtext = input("change/show/exit: ")
    if inputtext == "change":
        if input("+/-: ") == "+":
            much1 = (input("how much, just a number?: "))
            reason1 = (input("Reason?: "))
            add(much1, reason1)
        else:
            much1 = (input("how much, just a number?: "))
            reason1 = (input("Reason?: "))
            remove(much1, reason1)
    clear()
    if inputtext == "show":
        clear()
        balance.seek(0)
        print(getcheck() + "\n---balance---\n" + "$" + balance.read())
    if inputtext == "exit":
        exit()