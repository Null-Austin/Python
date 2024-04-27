tip = 20.0 #tip percent
cost = 45.0 #cost price
tax = 1.5 #tax percent.


cost += (float(tip)/100)*cost
cost += (float(tax)/100)*cost
print("Cost after tip/tax: " + str(cost))