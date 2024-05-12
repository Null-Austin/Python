import random
mph = 767.269148 #mph of speed of sound!
mpm = mph/60 #miles per minute sos
mps = mpm/60 #miles per sec sos
tips = [ "Avoid open fields and hilltops during a lightning storm.",
    "Stay away from tall, isolated trees or structures.",
    "If you're caught in an open area, crouch down on the balls of your feet to minimize contact with the ground.",
    "Avoid water bodies such as lakes, rivers, and pools during a lightning storm.",
    "Stay indoors during a lightning storm, and avoid using electrical appliances and plumbing fixtures.",
    "If you're driving, pull over to a safe location and stay in the car with the windows closed.",
    "Do not use corded phones or electronic devices connected to an outlet during a lightning storm.",
    "Wait at least 30 minutes after the last clap of thunder before going back outside.",
    "If someone is struck by lightning, call 911 immediately and perform CPR if necessary.",
    "Remember, when thunder roars, go indoors!"]
print(random.choice(tips)+"\n")
while(True):
        time = input("to get the distance, see lightning, count in sec how long it takes to\nget to you!\nSeconds: ")
        if time != "":
            if time.isdigit:
                time = float(time)
                print(time*mps + " Miles away")
                if input("do you want to continue? (y/n): ") == "n":
                    break
            else:
                print("Please put a real number!")