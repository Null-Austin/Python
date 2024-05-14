tip = input("%: ") #tip percent
cost = input("%: ") #cost price
tax = input("tax%: ") #tax percent.


cost += (float(tip)/100)*cost
cost += (float(tax)/100)*cost
print("Cost after tip/tax: " + str(cost))